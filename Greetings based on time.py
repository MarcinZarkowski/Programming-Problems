#Marcin Zarkowski
#24225410
#marcinzarkowski5@gmail.com
#this program greets the user based on time

time=int(input("What is the time"))

if time < 12:
    print("Good Morning")
elif time > 12 and time < 17:
    print("Good Afternoon")
else:
    print("Good Evening")
