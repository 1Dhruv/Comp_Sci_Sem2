x=input("How many items will you be purchasing: ")
a=[]
b=[]
d=int(0)
e=int(0)
x=int(x)
c=int(1)
t=0
for i in range (0,x):
    y=input("what will you be purchasing: ")
    z=input("how much is the item that you are purcasing: ")
    z=float(z)
    b.append(y)
    a.append(z)
    t=t+z
    print("Thank You for purchasing: ", y,"!")
for i in range(0,x):
    
    c=str(c)
    print("Item ",c, " ",b[d]," -$",a[e])
    e=e+1
    d=d+1
    c=int(c)
    c=c+1
print("for ",x," items ", "your total is ",t)
print("have a nice day")