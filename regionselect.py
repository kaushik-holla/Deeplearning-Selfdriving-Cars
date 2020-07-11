# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 20:51:53 2020

@author: holla
"""

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

# Reading the image
image = mpimg.imread('test.jpg')
print("The image is", type(image), "With dimension", image.shape)

# Making a copy of the image and getting x and y size
ysize = image.shape[0]
xsize = image.shape[1]
region_select = np.copy(image)

# Defining a triangle region of interest 
left_bottom = [0, 539]
right_bottom = [900, 300]
apex = [400, 0]

#Fitting line to create a tringle in the region of interest using np.polyfit()
fit_left = np.polyfit((left_bottom[0], apex[0]), (left_bottom[1], apex[1]), 1)
fit_right = np.polyfit((right_bottom[0], apex[0]), (right_bottom[1], apex[1]), 1)
fit_bottom = np.polyfit((left_bottom[0], right_bottom[0]), (left_bottom[1], right_bottom[1]), 1)

# Finding the regions inside the lines
XX, YY = np.meshgrid(np.arange(0, xsize), np.arange(0, ysize))
region_threshold = (YY > (XX*fit_left[0] + fit_left[1])) & (YY > (XX*fit_right[0] + fit_right[1])) & (YY > (XX*fit_bottom[0] + fit_bottom[1]))

# Coloring the region of interest with red.
region_select[region_threshold] = [255, 0, 0]

# Displaying the image
plt.imshow(region_select)

