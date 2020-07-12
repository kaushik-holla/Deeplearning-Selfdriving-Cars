import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2

# Reading in the image and converting to grayscale
image = mpimg.imread('exit-ramp.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

# Defining Kernal size for Gaussian Smoothing
kernal_size = 5
blur_gray = cv2.GaussianBlur(gray, (kernal_size, kernal_size), 0)

# Defining parameters for canny
low_threshold = 50
high_threshold = 150
edges = cv2.Canny(blur_gray, low_threshold, high_threshold)

plt.imshow(edges, cmap = 'Greys_r') 