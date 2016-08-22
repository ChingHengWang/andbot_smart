import theano
import theano.tensor as T
import random
import numpy.random 
import numpy
#theano.config.optimizer='fast_compile'
#theano.config.exception_verbosity='high'
#theano.config.compute_test_value = 'warn'





x=T.matrix('x',dtype='float64')
x_p=theano.printing.Print('DBG x: ')(x)
y_hat=T.matrix('reference',dtype='float64')
N_L1=5
N_L2=5
N_L3=5
batch_size = 2

W1 = T.theano.shared(numpy.matrix(numpy.random.randn(5,2)))
W1_p=theano.printing.Print('DBG W1: ')(W1)
b1 = T.theano.shared(numpy.array(numpy.random.randn(5,1)))
b1_p=theano.printing.Print('DBG b1: ')(b1)

z1 = T.dot(W1_p,x_p) + b1_p
z1_p=theano.printing.Print('DBG z1: ')(z1)

fun = theano.function(
		inputs=[x],
		outputs=z1_p
		)

data = numpy.loadtxt('miku.save')
data = data.transpose()
idx = 0
xBatch=numpy.empty([2,batch_size])
yBatch=numpy.empty([1,batch_size])
xBatch[:,0] = data[0:2,1]
yBatch[:,0] = data[2:3,1]
xBatch[:,1] = data[0:2,2]
yBatch[:,1] = data[2:3,2]
exec("xBatchM%s = xBatch" % idx)
exec("yBatchM%s = yBatch" % idx)

fun(xBatchM0)
'''
W1 = T.theano.shared(numpy.matrix(numpy.random.randn(N_L1,batch_size)))
W2 = T.theano.shared(numpy.matrix(numpy.random.randn(N_L2,N_L1)))
W3 = T.theano.shared(numpy.matrix(numpy.random.randn(N_L3,N_L2)))
W1_p=theano.printing.Print('W1: ')(W1)
W2_p=theano.printing.Print('W2: ')(W2)
W3_p=theano.printing.Print('W3: ')(W3)

b1 = T.theano.shared(numpy.matrix(numpy.random.randn(N_L1,1)))
b2 = T.theano.shared(numpy.matrix(numpy.random.randn(N_L2,1)))
b3 = T.theano.shared(numpy.matrix(numpy.random.randn(N_L3,1)))

z1 = T.dot(W1_p,x) + b1.dimshuffle(0,1)
print "z1"
a1= 1/(1+T.exp(-z1))
z2 = T.dot(W2_p,a1) + b2.dimshuffle(0,1)
a2= 1/(1+T.exp(-z2))
z3 = T.dot(W3_p,a2) + b3.dimshuffle(0,1)
y= 1/(1+T.exp(-z3))
neuron = theano.function(
		inputs=[x],
		outputs=z1
		)
y_hat = T.matrix('y_hat',dtype='float64')

cost = T.sum((y-y_hat)**2)/batch_size
dW1,dW2,dW3,db1,db2,db3 = T.grad(cost,[W1,W2,W3,b1,b2,b3])
gradient = theano.function(
		inputs = [x,y_hat],
		updates = [(W1,W1-0.1*dW1),(W2,W2-0.1*dW2),(W3,W3-0.1*dW3),(b1,b1-0.1*db1),(b2,b2-0.1*db2),(b3,b3-0.1*db3)]
		)


data = numpy.loadtxt('miku.save')
data = data.transpose()
print data
size=data.shape[1]
#print numpy.random.randint(1,size)

index_array = [x for x in range(size)]
random.shuffle(index_array)
#print index_array

batch_number = len(index_array)/batch_size

#for idx,val in enumerate(index_array[::batch_size]):
idx = 0

xBatch=numpy.empty([2,batch_size])
yBatch=numpy.empty([1,batch_size])
xBatch[:,0] = data[0:2,index_array[idx*batch_size]]
yBatch[:,0] = data[2:3,index_array[idx*batch_size]]
xBatch[:,1] = data[0:2,index_array[idx*batch_size+1]]
yBatch[:,1] = data[2:3,index_array[idx*batch_size+1]]
exec("xBatchM%s = xBatch" % idx)
exec("yBatchM%s = yBatch" % idx)

x=xBatch
y_hat=yBatch
neuron(x,y_hat)
'''
 
