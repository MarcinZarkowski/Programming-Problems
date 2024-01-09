#Marcin Zarkowski
#24225410
#marcinzarkowski5@gmail.com
#This program prints a string pyramid from inputed message.

mess=input("write a message")

for i in range(len(mess)):
    print(mess[:i])
for i in range(len(mess)):
    print(mess[i:])
