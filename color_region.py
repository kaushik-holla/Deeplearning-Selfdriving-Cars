import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

# Reading the image
image = mpimg.imread('test.jpg')

# Getiing the size and making two copies
ysize = image.shape[0]
xsize = image.shape[1]
color_select = np.copy(image)
line_image = np.copy(image)

# Defining the color criteria
red_threshold = 200
green_threshold = 200
blue_threshold = 200
rgb_threshold = [red_threshold, green_threshold, blue_threshold] 

# Defining the triangle region of interest
left_bottom = [200, 539] 
right_bottom = [800, 539]
apex = [400, 0]

# Finding the co-effecients for fitting the line
fit_left = np.polyfit((left_bottom[0], apex[0]), (left_bottom[1], apex[1]), 1)
fit_right = np.polyfit((right_bottom[0], apex[0]), (right_bottom[1], apex[1]), 1)
fit_bottom = np.polyfit((left_bottom[0], right_bottom[0]), (left_bottom[1], right_bottom[1]), 1)

# MAsking pixels below the threshold
color_threshold = (image[:,:,0] < rgb_threshold[0]) | (image[:, :, 1] < rgb_threshold[1]) | (image[:, :, 2] < rgb_threshold[2])

# Finding the region of interest
XX, YY = np.meshgrid(np.arange(0, xsize), np.arange(0, ysize))
# The equation os of the form y = mx + c
region_threshold = (YY > (XX*fit_left[0] + fit_left[1])) & \
                    (YY > (XX*fit_right[0] + fit_right[1])) & \
                    (YY < (XX*fit_bottom[0] + fit_bottom[1]))

# Masking color selection
color_select[color_threshold] = [0,0,0]

line_image[~color_threshold & region_threshold] = [255, 0, 0]

#plt.imshow(color_select)
plt.imshow(line_image)

plt.show()