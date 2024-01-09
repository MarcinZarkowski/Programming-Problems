#Marcin Zarkowski
#marcinzarkowski5@gmail.com
#24225410
#This program asks for input and outputs the message backwards in two columns.

mess=input("Write message to recieve backwards.")

for i in range(len(mess)):
    print (mess[-i-1], mess[-i-1]) 
  
    
