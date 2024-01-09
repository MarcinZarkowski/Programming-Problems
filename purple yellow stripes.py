#Marcin Zarkowski
#24225410
#marcinzarkowski5@gmail.com
#Draws image of purple and yellow stripes based on input from user.

import matplotlib.pyplot as plt
import numpy as np

size=int(input("Write the size of the image as a number"))
name=input("write the name of the final image file")

img=np.ones((size,size,3))
img[1:size:2,0:size,2]=0
img[0:size:2,0:size,1:-1]=0

plt.imshow()
plt.show()

plt.imsave(name, img)



 
