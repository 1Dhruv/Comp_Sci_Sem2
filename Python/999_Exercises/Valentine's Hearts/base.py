import random
people=["mom","dad","grandpa","grandma","sister","uncle"]
compliment=["is smart!","has good personality","is nice!","rocks!"]
peoprand=random.randrange(0,len(people))
comprand=random.randrange(0,len(compliment))
print(people[peoprand] + " "+ compliment[comprand])