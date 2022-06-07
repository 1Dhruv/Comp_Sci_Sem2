import numpy as np
import random
x=input("Please enter a size: ")
y=input("Please enter a minimum value: ")
z=input("Please enter a minimum value: ")
x=int(x)
y=int(y)
z=int(z)
a=np.random.randint(y,z,x)
b=a.min()
c=a.max()
d=a.sum()
e=a.size
f=(d/e)
print(a)
print(b)
print(c)
print(d)
print(f)