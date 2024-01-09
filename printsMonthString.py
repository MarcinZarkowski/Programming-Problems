#Marcin Zarkowski
#24225410
#marcinzarkowski5@gmail.com
#monthString() definition


    
def monthString(monthNum):
    monthString = ""
    months=["January","Febuary","March","April","May","June","July","August","September","October","Novemeber", "December"]
    monthString= months[monthNum-1]
    return(monthString)

def main():
     n = int(input('Enter the number of the month: '))
     mString = monthString(n)
     print('The month is', mString)

#Allow script to be run directly:
if __name__ == "__main__":
     main()
                   
