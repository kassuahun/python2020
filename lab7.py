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

#Copy the 3D array for question 3, 4 
copyimgarr = imgarr.copy()
smallimgarr = imgarr.copy()

for idx, x in np.ndenumerate(imgarr):
    if x > 150:
        imgarr[idx] = 255

newimg = Image.fromarray(imgarr)
#img.save('oslomet_snow.bmp')
newimg.show()


'''
for i in range(b[0]):
    for j in range(b[1]):
        for k in range(b[2]):
            if imgarr[i][j][k]>150:
                imgarr[i][j][k]=255
 '''       

'''
Copy the 3D array and manipulate the pixels in a way that every pixel where 
both the red and the green component byte values are higher than 130 
and the blue component byte value is less than 110 has to be modified: 

The red and the green values has to be exchanged, 
the green value has to be increased with 50 (if possible) and 
the red values has to be decreased by 50 (if possible). 
Save a new image with the name “oslomet_yellow.bmp” 
'''
#Copy the 3D array

for x in copyimgarr:
    for y in x:
        #both red and green byte values are higher than 130 and the blue value is less than 110 has to be modified:
        if y[0]>130 and y[1]>130 and  y[2] < 110:
            #y[0], y[1] = y[1], y[0] # swap R and G
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


'''
Cut the upper 200 pixels and 200 pixels from both edges. 
Modify the header accordingly. 
Save the new bitmap with the name “oslomet_small.bmp” 
'''

smallimage = smallimgarr[200:,200:-200,:]

     
smallimg = Image.fromarray(smallimage)
#smallimg.save('oslomet_small.bmp')
smallimg.show()







