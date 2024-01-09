#Marcin Zarkowski
#24225410
#marcinzarkowski5@gmil.com
#this program makes a list of names. It returns names in list like
# Epstein, Susan; St. John, Katherine; Vazquez-Abad, Felisa; Xu, Jia; Zamfirescu, Christina
# in first name, last name list structure.

names=input("write list of names")
names=names.split(";")
for i in names:
    item=i.split(",")
    print(item[-1],item[-2])
