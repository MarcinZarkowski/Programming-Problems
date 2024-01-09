#Marcin Zarkowski
#224225410
#marcinzarkowski5@gmail.com
#this program counts plural nouns

given=input("Give me nouns")
words=given.count(" ")+1
plurals=given.count("s ")
newgiv=given.split(" ")
item=newgiv[-1]
if "s" in item[-1]:
    plurals=plurals+1
else:
    print("number of words:", words)
    print("Fraction of plural", int(plurals)/int(words))

