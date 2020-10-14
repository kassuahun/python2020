#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 21:42:17 2020

@author: kassahundegena
"""

from PIL import Image
import numpy as np
#import cv2

#img = cv2.imread("oslomet.bmp")

img = Image.open("oslomet.bmp")
h,w= img.size
print('Question 1, The image size,  H = ', h, '  W = ', w )

#Read the pixels to numpy array 
imgarr = np.array(img)
b = imgarr.shape

print('Question 2: After copying the pixels to numpy array and read the size by imgarr.shape= ', imgarr.shape)
print("Lenght = " , b[0], "width = " , b[1], "depth = " , b[2])


smallimage = np.array(imgarr[200:,200:-200,:])
    
smallimg = Image.fromarray(smallimage)
l,h = smallimg.size
#smallimg.save('oslomet_small.bmp')
smallimg.show()


copyimgarr = imgarr.copy()

for i in range(b[0]):
    for j in range(b[1]):
        for k in range(b[2]):
            if imgarr[i][j][k]>150:
                imgarr[i][j][k]=255
 
newimg = Image.fromarray(imgarr)
img.save('oslomet_snow.bmp')
newimg.show()


for x in copyimgarr:
    for y in x:
        #both red and green byte values are higher than 130 and the blue value is less than 110 has to be modified:
        if y[0]>130 and y[1]>130 and  y[2] < 110:
            y[0], y[1] = y[1], y[0] # swap R and G
            if  y[0]>=50: 
                 y[0]-= 50
            else:
                y[0]=0 
                 
            if y[1]<206:
                y[1]+= 50
            else: 
                y[1]= 255

newimg = Image.fromarray(copyimgarr)
#img.save('oslomet_yellow.bmp')
newimg.show()









