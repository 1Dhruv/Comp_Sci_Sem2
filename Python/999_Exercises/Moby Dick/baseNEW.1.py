# moby = "whale hello there. Don't we all love whales ? I absolutely love whales! whales are so huge!!!"
# a=0
# b=1
# whalecount=0
# for i in range(0,100000):
#     if moby[a:b]=="w":
#         a=a+1
#         b=b+1
#         if moby[a:b]=="h":
#             a=a+1
#             b=b+1
#             if moby[a:b]=="a":
#                 a=a+1
#                 b=b+1
#                 if moby[a:b]=="l":
#                     a=a+1
#                     b=b+1
#                     if moby[a:b]=="e":
#                         whalecount=whalecount+1
#     elif moby[a:b]!="w":
#         a=a+1
#         b=b+1
                        
# print(whalecount)







# Did not work so used your code
# c=[]
# with open('moby.txt') as f:
#     for line in f:
#         r = line.strip()
#         c.append(r)
# x=0
# count=0
# print("hello")
# for i in range(len(c)):
#     if c[x]=="whale":
#         count=count+1
#     elif c[x]!="whale":
#         count=count+1
# print(count)
# print("hello")
count = 0
with open('moby.txt') as f:                         # This is given, open the text file.
    for line in f:                                  # For each line inside the file
        sentence = line.strip()                     # Sentence is equal to the entire line
        for i in range(0,len(sentence)):            # This is the EXACT SAME loop as above! Loops through the sentence!
            if sentence[i:i+5].lower() == "whale":
                count = count + 1
print(count)

f.close()