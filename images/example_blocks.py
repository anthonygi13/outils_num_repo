import numpy as np
from scipy import ndimage as ndi
from matplotlib import pyplot as plt
import matplotlib.cm as cm

from skimage import data
from skimage import color
from skimage.util import view_as_blocks
from skimage.io import imread


# get astronaut from skimage.data in grayscale
l = color.rgb2gray(imread("image_test.png"))[:228, :308]

print(l.shape)
# size of blocks
block_shape = (76, 77)

# see astronaut as a matrix of blocks (of shape block_shape)
view = view_as_blocks(l, block_shape)
print(view.shape)

# collapse the last two dimensions in one
flatten_view = view.reshape(view.shape[0], view.shape[1], -1)

# resampling the image by taking either `mean` value of each blocks.
mean_view = np.mean(flatten_view, axis=2)
cells = mean_view > 0.5
print(cells)


# display resampled images

ax = plt.imshow(cells, cmap=cm.Greys_r)
plt.title("Block view with\n local mean pooling")
plt.axis('off')

plt.show()