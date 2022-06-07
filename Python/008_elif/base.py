x=input("Give me a number: ")
op=input("Give me a operator: ")
y=input("Give me another number: ")
x=int(x)
y=int(y)
if op=="+":
    op1=str(x+y)
    print(op1)
elif op=="*":
    op2=str(x*y)
    print(op2)
elif op=="/":
    op3=str(x/y)
    print(op3)
elif op=="-":
    op4=str(x-y)
    print(op4)