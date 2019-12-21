import numpy as np
import matplotlib.pyplot as plt

from skimage import measure
from skimage import color
from skimage.io import imread


image = color.rgb2gray(imread("image_test.png"))

# Find contours at a constant value of 0.1
contours = measure.find_contours(image, 0.1)

# Display the image and plot all contours found
fig, ax = plt.subplots()
ax.imshow(image, cmap=plt.cm.gray)

for n, contour in enumerate(contours):
    ax.plot(contour[:, 1], contour[:, 0], linewidth=2)
    print((np.amax(contour[:, 1]) - np.amin(contour[:, 1])) / (np.amax(contour[:, 0]) - np.amin(contour[:, 0])))

ax.axis('image')
ax.set_xticks([])
ax.set_yticks([])
plt.show()
