import theano
import theano.tensor as T

a=T.matrix()
b=T.matrix()

c=a*b
d=T.dot(a,b)

F1=theano.function([a,b],c)
F2=theano.function([a,b],d)

A=[[1,2],[3,4]]
B=[[2,4],[6,8]]
C=[[1,2],[3,4],[5,6]]

