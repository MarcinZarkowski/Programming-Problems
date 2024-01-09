#Marcin Zarkowski
#24225410
#marcinzarkowski5@gmail.com
#Makes plot from data.

import matplotlib.pyplot as plt
import pandas as pd


pop = pd.read_csv('nycHistPop.csv',skiprows=5)
borough=input("What borough do you want to display?")
name=input("write name of file")
pop['Fraction'] = pop[borough]/pop['Total']

#Create a plot of year versus fraction of pop. in Bronx (with labels):
pop.plot(x = 'Year', y = 'Fraction')

#Save to the file:  fractionBX.png
fig = plt.gcf()
fig.savefig(name)

plt.show()
