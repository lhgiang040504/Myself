4.1 MHA mechanism (Multi-head Attention):

4.1.0 Input: 
Computer dont understand natural language, the only language they understand is that matrices and numbers.
With a line of code, we assign a numeric index to each vocab.
Denote by x 
4.1.1 Input Embedding
Against each of those indices, a vector is attached. Initially, these vector are filled up with random number. Later on, during trainning phase, the model update them with value that better. (the original Transformer went with embedding size of 512) Vector representation of a given word, each dimension of the vector tries to capture some linguistic feature about that vocab.
Linguistic feature: It can be non-trival to find out exactly what information do each of these dimensions represent.
If two vocab have the same linguistic features, during training process, they will get closer and closer in linguistic feature hyper dimension graph.
Denote again by e
	4.1.2 Position Embedding (Transformer)
LSTM vs Transformer:
LSTM: To take up these inputs embedding, it would do sequentially (one embedding at a time) in their designated order, so they know which vocab come at first and so on,
Transformer: On the other hand, taking up all the embedding at once. Even though this is a huge plus and make Transformer much faster, the downside is that they lose the critical information (the order).
Solution for Transformer: Introduce a new set of vector containing the position information.
Create a new order aware vocab simple enough: 
Denote p
How about we start by literally filling in the vocab position number. [0, 0, 0, …]
	    [1, 1, 1, …]
	    [2, 2, 2, …]
			Not really, adding the position information like that may significantly distort the embedding. If the number of p will change the information that linguistic carried on. Therefor, we dont want that.
What if instead we add fraction: position * (1 / length-1)
    
		So the maximum position embedding val will never surpass 1.
		Nah! That doesnt work either, because making position embeddings a fraction of length of code would mean if codes differs in length, each vocab in them will be assigned a different position embedding despite of same position index.
Ideally the position embedding values at a given position should remain the same irrespective of the code total length or any other factor.
The author came up with the clever idea, they used wave frequencies to capture position embedding.
			
			The problem when build this method is that what happen went we get same of height of sinusoidal curve of two points with different position index, use index of each dimension so having curve of each frequency..
			The idea behind having that is at each frequency, two random point will allway remain identity, but the height is not same with all of frequencies.
			Use a alternative combination of sin and cousin formular.
4.1.3 MHA mechanism(Multi-head Attention):
Attention Mechanism help the model to focus in important vocab in give input and they use self-attention.
Simple-attention vs self-sttention:
SimpleA: attention vicab respective.
SelfA: vocab to vocab. 


One Query will point to many Key
The informations affiliated with Key are called Value
Q, K, V mean different thing and have very different contents but we feed them the same input, this is where the self-attention come into play.

Three Linear layer: At Linear layer simply composed of a bunch of fully connected neurons without the activation function for Query & Key & Value position embedding.
The purpose: Mapping inputs on to the outputs and changing the dimension of matrix input.

Matmul:
 So as to find the best matches, it will have to do some soft of similarity between Query and Key.
they also are vector, we will get the angle between them (cosine similarity)

Similarity(Q, K) = Q * K.Transpose => we get similar score (attention score).

Scale and Softmax: We then get the final attention filter 
Concatenate and Last Linear: All of our head will be attached in this step and we pass it through a linear layer to shrink its size back.


	4.1.4 Why? What the point of all of this?
They filt out the unnecessary background information and zoom in to focus on what truly matter in that moment
Each head focusing different linguistic feature.

