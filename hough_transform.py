import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2

# Grayscale image
image = mpimg.imread('exit-ramp.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

# Defining Kernal to apply Gaussian smooting
kernal_size = 5 
blue_gray = cv2.GaussianBlur(gray, (kernal_size, kernal_size), 0)

# Defining Canny
low_threshold = 50
high_threshold = 150
masked_edge = cv2.Canny(blue_gray, low_threshold, high_threshold)

# Defining Hough transform parameters
rho = 1
theta = np.pi/180
threshold = 1
min_line_length = 10
max_line_gap = 1
line_image = np.copy(image)*0  # Creating a blank image to draw lines.

lines = cv2.HoughLinesP(masked_edge, rho, theta, threshold, np.array([]), min_line_length, max_line_gap)

# Now we iterate over the output lines and draw the lines on the image
for line in lines:
    for x1, y1, x2, y2 in line:
        # line_image is the image on which we draw.
        # line starts at x1, y1 and ends at x2, y2
        # 4th argument is the color of the line
        # 5th argument is the size of the image. 
        cv2.line(line_image, (x1, y1),(x2, y2), (255, 0, 0), 10)
        
# Creating a color binary image to combine with line image
color_edges = np.dstack((masked_edge, masked_edge, masked_edge))

# the syntax is image 1, weight for the image 1 and image 2 and weight for image 2 and optional gamma value. 
combo = cv2.addWeighted(color_edges, 0.8, line_image, 1, 0)
plt.imshow(combo)


