from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.optimizers import SGD
import numpy
# for a single-input model with 2 classes (binary):
data = numpy.loadtxt('miku.txt')
size=data.shape[1]
x=data[:,0:2]
y=data[:,2:3]

model = Sequential()
model.add(Dense(output_dim=1000, input_dim=2, activation='relu'))
model.add(Dense(output_dim=1, input_dim=1000, activation='relu'))


model.compile(optimizer='rmsprop',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# train the model, iterating on the data in batches
# of 32 samples
model.fit(x, y, nb_epoch=30, batch_size=10)
predict= model.predict(x, batch_size=10)
ans = numpy.concatenate((x,predict),axis=1)
numpy.savetxt('miku_2_1000_1000_1_relu_epoch_30_batch_size_10.txt', ans)

