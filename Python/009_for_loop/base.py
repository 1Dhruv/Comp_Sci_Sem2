x=input("Please enter line lenght: ")
y=input("Do you want it to go vertical or horizonal: ")
x=int(x)
if y=="horizontal":
    for x in range(0,x):
        print("*",end="")
if y=="vertical":
    for x in range(0,x):
        print("*")