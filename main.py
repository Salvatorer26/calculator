import numpy as np

from std_operation import Add, Substract

from linalg import ScalProd

a=-1
b=3.14

c=Add(a,b)

c= Add(a,b)
d = Substract(a,b)

print("{}+{}={}\n[{}-{}".format(a,b,c,a,b,d))
u = np.array((1, 0.5, -3.14))
v = np.array((-4,0,6.73))

udotv = ScalProd(u,v)

