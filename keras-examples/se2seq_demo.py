import keras
from keras.models import Sequential
from keras.layers.embeddings import Embedding
from seq2seq.seq2seq import Seq2seq
from keras.preprocessing import sequence

vocab_size = 20000 #number of words
maxlen = 100 #length of input sequence and output sequence
embedding_dim = 200 #word embedding size
hidden_dim = 500 #memory size of seq2seq

embedding = Embedding(vocab_size, embedding_dim, input_length=maxlen)
seq2seq = Seq2seq(input_length=maxlen, input_dim=embedding_dim,hidden_dim=hidden_dim,
                  output_dim=embedding_dim, output_length=maxlen, batch_size=10, depth=4)

model = Sequential()
model.add(embedding)
model.add(seq2seq)