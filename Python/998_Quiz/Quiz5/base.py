age=[]
favnum=[]
favnum1=""
favnum2=""
count=0
s=0
q=0
inp=input("In a complete sentence please write your favorite number: ")
inp1=input("What is your age: ")
for r in range(0,len(inp)):
    x=inp[r]
    if x=="0":
        favnum.append(x)
        favnum2=inp[count:len(inp)]
        s=s+1
    elif x=="1":
        favnum.append(x)
        favnum2=inp[count:len(inp)]
        s=s+1
    elif x=="2":
        favnum.append(x)
        favnum2=inp[count:len(inp)]
        s=s+1
    elif x=="3":
        favnum.append(x)
        favnum2=inp[count:len(inp)]
        s=s+1
    elif x=="4":
        favnum.append(x)
        favnum2=inp[count:len(inp)]
        s=s+1
    elif x=="5":
        favnum.append(x)
        favnum2=inp[count:len(inp)]
        s=s+1
    elif x=="6":
        favnum.append(x)
        favnum2=inp[count:len(inp)]
        s=s+1
    elif x=="7":
        favnum.append(x)
        favnum2=inp[count:len(inp)]
        s=s+1
    elif x=="8":
        favnum.append(x)
        favnum2=inp[count:len(inp)]
        s=s+1
    elif x=="9":
        favnum.append(x)
        favnum2=inp[count:len(inp)]
        s=s+1
    if s==0:
        count=count+1
favnum2=int(favnum2)
inp1=int(inp1)
q=favnum2*inp1
print("The 2 numbers multiplies is",q)