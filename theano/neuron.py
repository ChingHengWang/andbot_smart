#!/usr/bin/python

# run in gpu
# THEANO_FLAGS=mode=FAST_RUN,device=gpu python neuron.py 

# ReLU is more good than sigmoid
# a=T.switch(z<0,0,z)

import theano
import theano.tensor as T
import random
import numpy
example0='stop'
example01='stop'
SW_readfile_to_list='stop'
SW_readfile_to_ndarray='stop'
example1='stop'
example2='stop'
example3='stop'
example4='stop'
example5='stop'

example4='run'

def batch(iterable, n = 1):
   current_batch = []
   for item in iterable:
       current_batch.append(item)
       if len(current_batch) == n:
           yield current_batch
           current_batch = []
   if current_batch:
       yield current_batch


# y=x^2
if example0 == 'run':
  x=theano.tensor.scalar()
  y=theano.tensor.scalar()
  z = x**2+y**2
  f = theano.function(inputs=[x,y],outputs=z)
  print f(-2,-3)

# z=dot(x,w)
if example01 == 'run':
  x=T.vector()
  w=T.vector()
  z = T.dot(w,x)
  f = theano.function(inputs=[x,w],outputs=z)
  w=[-1,1]
  x=[-1,1]
  print f(w,x)

if SW_readfile_to_list == 'run':
  
  with open('miku.save') as f:
      content = f.readlines()
  print content

if SW_readfile_to_ndarray == 'run':
  data = numpy.loadtxt('miku.save')
  print type(data)

# create neuron function
# x,w,b as function input
if example1 == 'run':
	x=T.vector()
	w=T.vector()
	b=T.scalar()

	z = T.dot(w,x) + b
	y = 1/(1 + T.exp(-z))
	neuron = theano.function(
			inputs=[x,w,b],
			outputs=y
			)
	w = [-1,1]
	b = 0
	for i in range(5):
			x=[random.random(), random.random()]
			print x
			print neuron(x,w,b)

# shared variable
if example2 == 'run':
#only x is input
# w, b is shared variable
# any function in this program can access shared variable w,b
	x=T.vector()
	w=T.theano.shared(numpy.array([1.,1.]))
	b=T.theano.shared(0.)

	z = T.dot(w,x) + b
	y = 1/(1 + T.exp(-z))
	neuron = theano.function(
			inputs=[x],
			outputs=y
			)
	print w.get_value()
	w.set_value([0.,0.])
	for i in range(5):
			x=[random.random(), random.random()]
			print x
			print neuron(x)


# Cost function C
# comput dC/dw1 dC/dw2.....dC/dwN
if example3 == 'run':
	x=T.vector()
	w=T.theano.shared(numpy.array([1.,1.]))
	b=T.theano.shared(0.)

	z = T.dot(w,x) + b
	y = 1/(1 + T.exp(-z))
	neuron = theano.function(
			inputs=[x],
			outputs=y
			)
	#y_reference
	y_hat = T.scalar()
	# cost function
	cost = T.sum((y-y_hat)**2)
	# gradient 
	dw,db = T.grad(cost,[w,b])
	gradient = theano.function(
			inputs=[x,y_hat],
			outputs=[dw,db]
			)
	x = [1,-1]
	y_hat = 1
	print neuron(x)
	dw,db=gradient(x,y_hat)
	# w,b is shared variable, use get_value()
	print w.get_value()
	print dw
	print b.get_value()
	print db
	# 0.1 is learning rate
	# update parameter w and b
	w.set_value(w.get_value()-0.1*dw)
	b.set_value(b.get_value()-0.1*db)
	print w.get_value()
	print b.get_value()


if example4 == 'run':
	x=T.vector()
	w=T.theano.shared(numpy.array([1.,1.]))
	b=T.theano.shared(0.)

	z = T.dot(w,x) + b
	y = 1/(1 + T.exp(-z))
	neuron = theano.function(
			inputs=[x],
			outputs=y
			)
	y_hat = T.scalar()
	cost = T.sum((y-y_hat)**2)
	dw, db = T.grad(cost,[w,b])
	gradient = theano.function(
			inputs = [x,y_hat],
			updates = [(w,w-0.1*dw) , (b,b-0.1*db)]
			)
#	x = [1,-1]
	x=numpy.array([1,-1])
	y_hat = 1

	for i in range(100):
			print neuron(x)
			gradient(x,y_hat)

if example5 == 'run':
	batch_size = T.schalar()
	x=T.matrix('x',dtype='float32')
	y_hat=T.matrix('x',dtype='float32')
	batch_size=2
	W1 = theano.shared(numpy.matrix(numpy.random.randn(3,batch_size)))

	W2 = theano.shared(numpy.matrix(numpy.random.randn(2,3)))

	W3 = theano.shared(numpy.matrix(numpy.random.randn(1,2)))

	b1 = theano.shared(numpy.matrix(numpy.random.randn(3,1)))
	b2 = theano.shared(numpy.matrix(numpy.random.randn(2,1)))
	b3 = theano.shared(numpy.matrix(numpy.random.randn(1,1)))

	z1 = T.dot(W1,x) + b1.dimshuffle(0,'x')
	a1 = 1/(1+T.exp(-z1))
	z2 = T.dot(W2,a1) + b2.dimshuffle(0,'x')
	a2 = 1/(1+T.exp(-z2))
	z3 = T.dot(W3,a2) + b2.dimshuffle(0,'x')
	y = 1/(1+T.exp(-z3))
	



'''
if example5 == 'run':
	batch_size=T.schalar()
	miku_raw=numpy.transpose(numpy.loadtxt('miku.save'))
	print miku_raw
	x=miku_raw[0:2,:]
	y_hat=miku_raw[2,:]
	print x
	print y_hat
	index=numpy.arange(miku_raw.shape[1])
	index_rand=random.sample(index,index.shape[0])
	w=T.theano.shared(numpy.array([1.,1.]))

	for idx in batch(index_rand,batch_size):
'''		

'''
	x = [line.split() for line in f]
	print l

if example5 == 'run':

	batch_size=T.schalar()
	x=T.matrix('input',dtype='float32')
	y_hat=T.matrix('reference',dtype='float32')

	w=T.theano.shared(numpy.array([1.,1.]))
	print w.get_value()
	b=T.theano.shared(0.)

	z1 = T.dot(W1,x) + b1.dimshuffle(0,'x')
	a1= 1/(1+T.exp(-z1))
	z2 = T.dot(W2,a1) + b2.dimshuffle(0,'x')
	a2= 1/(1+T.exp(-z2))
	z3 = T.dot(W3,a12 + b2.dimshuffle(0,'x')
	y= 1/(1+T.exp(-z3))
	
	neuron = theano.function(
			inputs=[x],
			outputs=y
			)
	y_hat = T.scalar()
	cost = T.sum((y-y_hat)**2)
	dw, db = T.grad(cost,[w,b])
	gradient = theano.function(
			inputs = [x,y_hat],
			updates = [(w,w-0.1*dw) , (b,b-0.1*db)]
			)
	x = [1,-1]
	y_hat = 1

#	for i in range(100):
#			print neuron(x)
#			gradient(x,y_hat)
'''
