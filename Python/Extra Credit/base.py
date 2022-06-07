import random
b=[]
wordguess=[]
fake=["blank","blank","blank","blank","blank"]
with open('allow_words.txt') as f:
      for line in f:
         l= line.strip()
         b.append(l)
a=8
password=0
q=0
hacker=0
x=random.randrange(12972)
y=b[x]
print("Hello you are know going to play my version of Hangman")
print("You will have to guess the letters of the 5 letter word.  PLEASE PUT ALL LOWER CASE")
print("If you ever want to see all of the commands then type index")

name=input("What is your name:")
if name=="Dhruv":
    password=input("Welcome Dhurv what is your password:")
    if password!="91214":
        print("Sorry the password that you have entered is wrong")
        print("Hacker detected")
        print("know terminating game")
        hacker=hacker+1
        # inp2=input("type yes if you would like to write your password again Dhruv: ")
        # if inp2=="yes":
        #     password=input("Welome Dhruv again please enter your password: ")
        #     if password!="91214":
        #         print("Sorry the password that you have entered is wrong")
        #     elif password=="91214":
        #         print("Welcome Dhruv identy has know been conformined")
    elif password=="91214":
        print("Welcome Dhruv identy has know been conformined")
elif name=="mr.Poole":
    print("Hello mr.Poole.  Dhruv deserves full points on this project.  Just so we mean that we will give you the word.  The word is",y)
else:
    print("Welcome",name,".  Hope you have a fun time playing")



for i in range(0,30000):
    if hacker==1:
        break
    num=0
    r=0
    c=input("guess a letter: ")

    if c=="index":
        print("If you ever want to see the letters you have entered type bank")
        print("If you want to see how many tries you have left then type tries")
        print("If you would like to guess the word then type guess")
        print("If you want to see what the word looks like then type word ")
        print("If you want the game to end then type end")
        num=num=1
        r=r+1
        
    if name !="Dhruv":
        if c=="hack":
            print("Sorry don't know what you are taking about")
            num=num+1
            r=r+1
        if c=="override":
            print("Sorry don't know what you are taking about")
            num=num+1
            r=r+1
        if c=="wordletter":
            print("Sorry don't know what you are taking about")
            num=num+1
            r=r+1
        if c=="awnser":
            print("Sorry don't know what you are taking about")
            num=num+1
            r=r+1
        if c=="guessawn":
            print("Sorry don't know what you are taking about")
            num=num+1
            r=r+1
    
    if c=="change user":
        name=input("What is your name:")
        if name=="Dhruv":
            password=input("Welcome Dhurv what is your password:")
            if password!="91214":
                print("Sorry the password that you have entered is wrong.")
                print("Hacker detected")
                print("know terminating game")
                break
                # inp2=input("type yes if you would like to write your password again Dhruv: ")
                # if inp2=="yes":
                #     password=input("Welome Dhruv again please enter your password: ")
                #     if password!="91214":
                #         print("Sorry the password that you have entered is wrong")
                #     elif password=="91214":
                #         print("Welcome Dhruv identy has know been conformined")
            elif password=="91214":
                print("Welcome Dhruv identy has know been conformined")
        else:
            print("Welcome",name,".  I see you changed user so.  Hope you have a fun time playing")
        num=num+1
        r=r+1
   #Cheats (illegal unles Dhruv) 
    if password=="91214":
        if c=="hack":
            a=50
            num=num+1
            r=r+1
        if c=="override":
            inp=input("How many lives would you like to have: ")
            inp=int(inp)
            a=inp
            r=r+1
            num=num+1
        if c=="wordletter":
            inp1=input("Which letter in the word would you like.")
            awn=int(inp1)
            awn=awn-1
            print(y[awn])
            num=num+1
            r=r+1
        if c=="awnser":
            print(y)
            num=num+1
            r=r+1
        if c=="guessawn":
            gue3=input("Guess the word.  Rembember when you guess a life will go away: ")
            a=a-1
            r=r+1
            for i in range(0,5):
                gue4=0
                num=num+1
                if gue3[i]==y[i]:
                    gue4=gue4+1
                print(gue4,end="")
            print("")
    
    
    #Good (legal)
    if c=="bank":
        for i in range(0,q-1):
            print(wordguess[i],end=",")
        print(wordguess[q-1])
        num=num+1
        r=r+1
    if c=="word":
        for i in range(0,4):
            print(fake[i],end = ",")
        print(fake[4])
        num=num+1
        r=r+1
    if c=="tries":
        print(a)
        num=num+1
        r=r+1
    if c=="guess":
        gue=input("Guess the word.  Rembember when you guess a life will go away: ")
        a=a-1
        gue1=0
        r=r+1
        for i in range(0,5):
            num=num+1
            if gue[i]==y[i]:
                gue1=gue1+1
        if gue1==5:
            print("Congrats you guessed the word!!!")
            break
        elif gue1 != 5:
            print("Sorry you didn't guess the word")
    if c=="end":
        print("Thank you for playing and know goodbye")
        break
            
    for i in range(len(wordguess)):
            if c==wordguess[i]:
                print("Sorry the letter you have entered has already been used so please use another letter")
                print()
                num=num+1
                r=r+1
    if r==0:
        if len(c)!=1:
            print("It has to be a letter not a word if you are trying to guess the word then write guess")
            num=num+1
                
    if num==0:
        wordguess.append(c)
        count=0
        counter=0
        q=int(q)
        q=q+1
        for i in range(0,5):
            if c==y[i]:
                fake[i]=c
                counter=counter+1
            if count==4:
                if counter != 0:
                    print("Good Job the letter was in the word")
                    print()
                else:
                    print("Nice try but the letter was not in the word")
                    print()
                    
                    a=a-1
            count=count+1
        num1=0       
        for i in range(0,5):
            
            if fake[i]==y[i]:
                num1=num1+1
        if num1==5:
            print("Winner good job you solved the word!!! YAY!!!")
            print("Good job again.  The word was",y)
            break
        if a==0:
            print("Hello sorry there but you lost since you ran out of lives")
            print("The word was ",y)
            break