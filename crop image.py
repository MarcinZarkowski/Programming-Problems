#Marcin Zarkowski
#24225410
#marcinzarkowski5@gmail.com
#this program crops an image

import matplotlib.pyplot as plt
import numpy as np
fl=input("file name:")
out=input("output file:")

img=plt.imread(fl)
height=img.shape[0]
width=img.shape[1]
img2=img[height//2:,:width//2]

plt.imsave(out, img2)
