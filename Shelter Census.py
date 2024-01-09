#Marcin Zarkowski
#24225410
#marcinzarkowski5@gmail.com
#Shelter Census hw

import pandas as pd
import matplotlib.pyplot as plt
fl=input("Write file name")
out=input("output file name")

homeless = pd.read_csv(fl)
homeless["Fraction Children"]=homeless["Total Children in Shelter"]/homeless["Total Individuals in Shelter"]

homeless.plot(x = "Date of Census", y = "Fraction Children")
fig=plt.gcf()
fig.savefig(out)




