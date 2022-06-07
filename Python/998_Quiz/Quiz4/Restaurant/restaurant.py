import random
restaurant=["Tacobell","BurgerKing","Dominos"]
Tacobell=["Taco","Chalupa","Baja Blast"]
BurgerKing=["Cheese Burger","Chicken Nugets","French Fries"]
Dominos=["Cheese Piza","Peporoni Pizza","Pepsi"]
print(restaurant)
int1=input("What restaurant do you want to go to:")

randfood=random.randrange(0,3)

if int1=="Tacobell":
    print("You choose Tacobell.  They have",Tacobell,".  But we sugest for you to buy",Tacobell[randfood])
elif int1=="BurgerKing":
    print("You choose Burger King.  They have",BurgerKing,".  But we sugest for you to buy",BurgerKing[randfood])
elif int1=="Dominos":
    print("You choose Dominos.  They have",Dominos,".  But we sugest for you to buy",Dominos[randfood])