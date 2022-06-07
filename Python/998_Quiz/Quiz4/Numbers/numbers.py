Max=0
Min=0
x=0
Average=0
mynumbers=[6,9,32,28,15,22,3,18]
total=0
a=0
for x in range(0,len(mynumbers)-1):
    if mynumbers[x]>mynumbers[x+1]:
        Max=mynumbers[x]
    elif mynumbers[x]<mynumbers[x+1]:
        Max= mynumbers[x]
for x in range(0,len(mynumbers)-1):
    if mynumbers[x]<mynumbers[x+1]:
        Min=mynumbers[x]
    elif mynumbers[x]>mynumbers[x+1]:
        Min= mynumbers[x]

for x in range(len(mynumbers)):
    total=total+ mynumbers[x]
Average=total/8

print("Your minimum number is ", Min,".")
print("Your maximum number is ", Max,".")
print("Your average number is ", Average,".")