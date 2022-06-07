import random
b=[]
with open('allow_words.txt') as f:
      for line in f:
         l= line.strip()
         b.append(l)

y=random.randrange(12972)
x=b[y]
print(x)
c = 0
for i in range (0,6):
    z=input("Guess a word: ")
    if z==x:
        print("You won good Job!")
        a = 1
        break
    else:
        print("Guess Again")
if c==0:
    print("You lost! The word was: "+ x)