# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 19:34:29 2020

@author: holla
"""
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np

# Reading the image and printing the stats
image = mpimg.imread('test.jpg')
print("This image is: ", type(image), "with dimentions: ", image.shape)

# Grabing x and y copy
ysize = image.shape[0]
xsize = image.shape[1]

# Making a copy of the image
img_copy = np.copy(image)

red_threshold = 195
blue_threshold = 195
green_threshold = 195
rgb_threshold = [red_threshold, blue_threshold, green_threshold]

# Identifying the pixels below threshold
thresholds = (image[:,:,0] < rgb_threshold[0]) | (image[:,:,1] < rgb_threshold[1]) | (image[:,:,2] < rgb_threshold[2])

img_copy[thresholds] = [0,0,0]

plt.imshow(img_copy)
plt.show()