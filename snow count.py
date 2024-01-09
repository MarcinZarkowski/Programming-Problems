#Marcin Zarkowski
#24225410
#A program counting white pixels.
import matplotlib.pyplot as plt
import numpy as np

In=input("write file name of image")
img=plt.imread(In)
t=0.75
count=0
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        if (img[i,j,0]>t) and (img[i,j,1]>t) and (img[i,j,2]>t):
                               count= count+1
        


print("Snow count is", count) 
    
