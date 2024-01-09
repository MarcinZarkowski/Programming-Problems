#Marcin Zarkowski
#marcinzarkowski5@gmail.com
#prints image of bridge in pruple filter.


import matplotlib.pyplot as plt
import numpy as np

In=input("write name of file to input")
out=input("write name of file to output")

img=plt.imread(In)


img2=img.copy()
img2[:,:,1]=0


plt.imsave(out, img2)
