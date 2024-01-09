#Marcin Zarkowski
#24225410
#transit Fare Program

def computeFare(zone, ticketType):
    fare = 0
    if zone == 1:
        if ticketType =="peak":
            fare= 8.75
        else:
            fare=6.25
    if zone == 2 or 3:
        if ticketType =="peak":
            fare= 10.25
        else:
            fare= 7.50
    if zone ==4:
        if ticketType =="peak":
            fare= 12.00
        else:
            fare= 8.75
    if zone == 5 or 6 or 7:
        if ticketType =="peak":
            fare= 13.50
        else:
            fare= 9.75
    if zone > 8:
        fare= -1
    return(fare)

def main():
     z = int(input('Enter the number of zones: '))
     t = input('Enter the ticket type (peak/off-peak): ').lower()
     fare = computeFare(z,t)
     print('The fare is', fare)

#Allow script to be run directly:
if __name__ == "__main__":
     main()
                   
