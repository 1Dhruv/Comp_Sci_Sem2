import random
words=[]
dkletter=[]
fake=["","","","",""]
noletter=[]
posible=[]
wor=""
with open('allow_words.txt') as f:
      for line in f:
         l= line.strip()
         words.append(l)
for i in range(0,40):
    print("Do you know if there are any letters in the word.") 
    print("Please be very specific in what you want to type so be careful and when you enter a letter enter one at a time")
    inp=input("If you know what and where the letter is type yes.  If you know the letter but don't know where it goes type dk.  Lastly if you don't even know a word then type no: ")
    if inp == "yes":
        yes1=input("What is the letter: ")
        yes2=input("What place in the word does it go in: ")
        yes2=int(yes2)
        fake[yes2-1]=yes1
        for check in range(0,12972):
            print(check)
            yes3=0
            wor=words[check]
            for i in range(0,5):
                if wor[i]!=fake[i]:
                    yes3=yes3+1
            if yes3!=0:
                words.remove(words[check])
    elif inp =="dk":
         dk1=input("What is the letter that you are unsure where it goes: ")
         dkletter.append(dk1)
    elif inp == "no":
        no1=input("What is the letter that is deffenetliy not in the word: ")
        noletter.append(no1)
        for b in range(0,len(words)):
            no2=0
            wor1=words[b]
            for i in range(0,5):
                if wor1[i]==noletter:
                    no2=no2+1
            if no2 != 0:
                words.remove(words[check])
        print(words)
    elif inp=="end":
        break