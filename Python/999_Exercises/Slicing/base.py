x=input("Hello user give me your First name and last name please: ")
# y=0
# z=1
# for i in range(len(x)):
#     print(x[y:z])
#     y=y+1
#     z=z+1
a=0
b=1
for i in range(len(x)):
    if x[a:b] == " ":
        c=(x[b:len(x)])
        d=(x[0:a])
        print(c,d)
    a=a+1
    b=b+1