import tensorflow as tf
from tensorflow.keras.layers import Dense, Layer


class MultiHeadAttention(Layer):
    def __init__(self, d_model: int = 512, num_heads: int = 6):
        """
        Multi-Head Attention Layer

        Parameters:
        ----------
            d_model: int, the dimension of the input and output feature vectors
            num_heads: int, the number of attention heads
        
        Returns:
        ----------
        """
        super().__init__()
        
        assert d_model % num_heads == 0, "d_model must be divisible by num_heads"
        
        self.d_model = d_model
        self.num_heads = num_heads
        self.depth = d_model // num_heads
        
        self.wq = Dense(d_model)
        self.wk = Dense(d_model)
        self.wv = Dense(d_model)
        self.wo = Dense(d_model)


    def split_heads(self, x: tf.Tensor) -> tf.Tensor:
        """
        Splits the last dimension into (num_heads, depth) and transposes for attention computation.

        Parameters
        ----------
        x: tensor
            query/key/value
            shape: (..., length, d_model)

        Returns
        ----------
        xs: tensor
            splitted heads
            shape: (..., h, length, hd_v)

        """
        batch_size = tf.shape(x)[0]
        seq_length = tf.shape(x)[1]

        assert tf.shape(x)[-1] == self.d_model, "Input feature size must match d_model"
        
        x = tf.reshape(x, (batch_size, seq_length, self.num_heads, self.depth))
        return tf.transpose(x, perm=[0, 2, 1, 3])  # Shape: (batch_size, num_heads, seq_length, depth)


    def scaled_dot_product_attention(self, q, k, v, mask=None):
        """
        Calculate Attention score

        Parameters
        ----------
        q: tensor
            query
            shape: (..., q_length, d_k)
        k: tensor
            key
            shape: (..., k_lengh, d_k)
        v: tensor
            value
            shape: (..., v_length, d_v)
        k_lengh = v_length

        Returns
        ----------
        attention_weights: tensor 
            Attention Scores between Query and Key
            shape: (..., q_length, k_lengh)
        out: tensor
            Attention Weights on Value
            shape: (..., q_length, k_lengh)
        """

        dk = tf.cast(tf.shape(k)[-1], dtype=tf.float32)
        
        scores = tf.matmul(q, k, transpose_b=True) / tf.math.sqrt(dk)
        
        if mask is not None:
            scores += (mask * -1e9)  # Large negative value for masked positions
        
        attention_weights = tf.nn.softmax(scores, axis=-1)
        output = tf.matmul(attention_weights, v)
        
        return output, attention_weights
        

    def call(self, q: tf.Tensor, k: tf.Tensor, v: tf.Tensor, mask: tf.Tensor = None):
        """
        Forward pass for Multi-Head Attention.
        """
        batch_size = tf.shape(q)[0]
        
        q, k, v = self.wq(q), self.wk(k), self.wv(v)  # Linear projections
        
        print("After linear projections:", q.shape, k.shape, v.shape)
        
        q, k, v = self.split_heads(q), self.split_heads(k), self.split_heads(v)
        
        print("After splitting into heads:", q.shape, k.shape, v.shape)
        
        attention_output, attention_weights = self.scaled_dot_product_attention(q, k, v, mask)
        
        print("After attention mechanism:", attention_output.shape)
        
        attention_output = tf.transpose(attention_output, perm=[0, 2, 1, 3])  # Reassemble heads
        attention_output = tf.reshape(attention_output, (batch_size, -1, self.d_model))  # Concatenate heads
        
        print("After concatenation:", attention_output.shape)
        
        final_output = self.wo(attention_output)  # Final linear layer
        
        print("Final output shape:", final_output.shape)
        
        return final_output, attention_weights
    

    def call_test(self):
        # init parameters
        batch_size = 64
        q_length = 100
        k_length = 200 
        v_length = 200
        d_k = 64
        d_v = 64

        q = tf.ones((batch_size, q_length, d_k))
        print(q.shape)
        k = tf.ones((batch_size, k_length, d_k))
        print(k.shape)
        v = tf.ones((batch_size, v_length, d_v))
        print(v.shape)
        print('d_k (a sub-dimension of the model) is used for projection consistency. Since both q and k are projected from the input sequence, they must have the same dimension for proper dot product computation.')
        
        q, k, v = self.wq(q), self.wk(k), self.wv(v)  # Linear projections
        
        print("After linear projections:", q.shape, k.shape, v.shape)
        
        q, k, v = self.split_heads(q), self.split_heads(k), self.split_heads(v)
        
        print("After splitting into heads:", q.shape, k.shape, v.shape)
        
        attention_output, attention_weights = self.scaled_dot_product_attention(q, k, v, None)
        
        print("After attention mechanism:", attention_output.shape)
        
        attention_output = tf.transpose(attention_output, perm=[0, 2, 1, 3])  # Reassemble heads
        attention_output = tf.reshape(attention_output, (batch_size, -1, self.d_model))  # Concatenate heads
        
        print("After concatenation:", attention_output.shape)
        
        final_output = self.wo(attention_output)  # Final linear layer
        
        print("Final output shape:", final_output.shape)
        
        return final_output, attention_weights

