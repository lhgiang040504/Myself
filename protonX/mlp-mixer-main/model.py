import numpy as np
import tensorflow as tf
from tensorflow.keras import models, layers

# This defines a new class Patches that inherits from layers.Layer, typically used in TensorFlow to create custom layers.
class Patches(layers.Layer):
  def __init__(self, patch_size):
    # Ensure proper initialization
    super(Patches, self).__init__()
    self.patch_size = patch_size

  def call(self, images):
    batch_size = tf.shape(images)[0]
    patches = tf.image.extract_patches(
        images= images,
        sizes = [1, self.patch_size, self.patch_size, 1],
        strides = [1, self.patch_size, self.patch_size, 1],
        # The dilation rates for the height and width dimensions
        rates = [1, 1, 1, 1],
        padding = 'VALID',
    )
    dim = patches.shape[-1]
    patches = tf.reshape(patches, (batch_size, -1, dim))
    #print('patches.shape: {}'.format(patches.shape))

    return patches 
    
class MLPBlock(layers.Layer):
  def __init__(self, S, C, DS, DC):
    super(MLPBlock, self).__init__()
    self.layerNorm1 = layers.LayerNormalization()
    self.layerNorm2 = layers.LayerNormalization()
    w_init = tf.random_normal_initializer()
    self.DS = DS
    self.DC = DC
    self.W1 = tf.Variable(
            initial_value=w_init(shape=(S, DS), dtype="float32"),
            trainable=True,
    )
    self.W2 = tf.Variable(
            initial_value=w_init(shape=(DS, S), dtype="float32"),
            trainable=True,
    )
    self.W3 = tf.Variable(
            initial_value=w_init(shape=(C, DC), dtype="float32"),
            trainable=True,
    )
    self.W4 = tf.Variable(
            initial_value=w_init(shape=(DC, C), dtype="float32"),
            trainable=True,
    )

  def call(self, X):
    # patches (..., S, C)
    #print('X.shape: {}'.format(X.shape))
    batch_size, S, C = X.shape

    # Token-mixing
    # (..., C, S)
    X_T = tf.transpose(self.layerNorm1(X), perm=(0, 2, 1))

    # assert X_T.shape == (batch_size, C, S), 'X_T.shape: {}'.format(X_T.shape)

    W1X = tf.matmul(X_T, self.W1) # (..., C, S) . (S, DS) = (..., C, DS)

    # (..., C, DS) . (DS, S) == (..., C, S)
    # (..., C, S). T == (..., S, C)
    # (..., S, C) + (..., S, C) = (..., S, C)
    U = tf.transpose(tf.matmul(tf.nn.gelu(W1X), self.W2), perm=(0, 2, 1)) + X # skip connection

    # Channel-minxing

    W3U = tf.matmul(self.layerNorm2(U), self.W3) # (...,S, C) . (C, DC) = (..., S, DC)

    Y = tf.matmul(tf.nn.gelu(W3U), self.W4) + U  # (..., S, DC) . (..., DC, C) + (..., S, C) = (..., S, C) # skip connection

    return Y
  
@tf.keras.utils.register_keras_serializable(package="CustomModels")
class MLPMixer(models.Model):
  def __init__(self, patch_size, S, C, DS, DC, num_of_mlp_blocks, image_size, batch_size, num_classes, **kwargs):
    super(MLPMixer, self).__init__(**kwargs)
    self.projection = layers.Dense(C)
    self.mlpBlocks = [MLPBlock(S, C, DS, DC) for _ in range(num_of_mlp_blocks)]
    self.patches_layer = Patches(patch_size)

    self.batch_size = batch_size
    self.patch_size = patch_size
    self.S = S
    self.C = C
    self.DS = DS
    self.DC = DC
    self.image_size = image_size
    self.num_classes = num_classes

    self.classificationLayer = models.Sequential([
          layers.GlobalAveragePooling1D(),
          layers.Dropout(0.2),
          layers.Dense(num_classes, activation='softmax')
    ])

  def call(self, images):
    # input
    # images shape: (batch_size, image_size, image_size, 3) = (32, 64, 64, 3)
    batch_size = images.shape[0]

    #augumented_images = self.data_augmentation(images)
    # assert augumented_images.shape == (batch_size, self.image_size, self.image_size, 3)

    X = self.patches_layer(images)

    # Per-patch Fully-connected
    # X shape: (batch_size, S, C)
    X = self.projection(X)

    #assert X.shape == (batch_size, self.S, self.C)
    for block in self.mlpBlocks:
      X = block(X)

    # out shape: (batch_size, C)
    out = self.classificationLayer(X)

    #print('output.shape: {}'.format(out.shape))
    assert out.shape == (batch_size, self.num_classes), "Oops, wrong output shape"

    return out

  def get_config(self):
    # Return a config dictionary with all necessary parameters to rebuild the model.
    config = super().get_config()
    config.update({
      "patch_size": self.patch_size,
      "S": self.S,
      "C": self.C,
      "DS": self.DS,
      "DC": self.DC,
      "num_of_mlp_blocks": len(self.mlpBlocks),
      "image_size": self.image_size,
      "batch_size": self.batch_size,
      "num_classes": self.num_classes,
    })
    return config