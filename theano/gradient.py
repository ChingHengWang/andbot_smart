#!/usr/bin/python
import theano
import theano.tensor as T

example1='stop'
example2='stop'
example3='run'

if example1 == 'run':
	x = theano.tensor.scalar('x')
	y = x**2
	g = T.grad(y,x)
	f = theano.function([x],y)
	f_prime = theano.function([x],g)

	print f(-2)
	print f_prime(-2)

if example2 == 'run':
	x1=T.scalar()
	x2=T.scalar()
	y=x1*x2
	g=T.grad(y,[x1,x2])

	f=theano.function([x1,x2],y)
	f_prime=theano.function([x1,x2],g)

	print f(2,4)
	print f_prime(2,4)

if example3 == 'run':
	A=T.matrix()
	B=T.matrix()
	C=A*B
	D=T.sum(C)
	g=T.grad(D,A)
	y_prime=theano.function([A,B],g)

	A=[[1,2],[3,4]]
	B=[[2,4],[6,8]]
	print y_prime(A,B)
