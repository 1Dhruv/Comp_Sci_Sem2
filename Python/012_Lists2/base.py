import random
x=input("Tell me how many random numbers you want to make appear: ")
x=int(x)
y=[]

for z in range (0,x):
    z=random.randrange(1,11)
    y.append(z)

for i in range(0,x-1):
    print(y[i],end = ",")
print(y[x-1])