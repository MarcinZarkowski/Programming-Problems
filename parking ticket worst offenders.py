#Marcin Zarkowski
#24225410
#marcinzarkowski5@gmail.com
#this program counts the worst offenders in a csv file containing a list of fined persons.
#this program can be implemented to any csv file structured respectively by changing the splicing column title. 

import pandas as pd
csvFile = input('Enter CSV file name: ')  
search=input("What attribute?")
      
tickets = pd.read_csv(csvFile)     #Read in the file to a dataframe
print("The 10 worst offenders are:")
print(tickets[search].value_counts()[:10]) #Print out the dataframe
