import theano
import theano.tensor as T
import random
import numpy.random 
import numpy
theano.config.exception_verbosity='high'
x=T.matrix('x',dtype='float64')
b=T.theano.shared(numpy.array([1]))

b=b.dimshuffle(0,'x')

b_printed = theano.printing.Print('b dimshuffle: ')(b)
y=x-x
y=x+b_printed
f = theano.function([x],y)

data=numpy.matrix([[1,2],[2,4],[3,6]])
print f(data)

