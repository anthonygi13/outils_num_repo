#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File : lifegame.py
# Created by Anthony Giraudo the 16/12/2019

"""Attempt to get a boolean numpy array, easy to use to initialise a lifegame simulation, from an image.
"""

# Modules

import numpy as np
from matplotlib import pyplot as plt
import matplotlib.cm as cm

from skimage import color
from skimage.util import view_as_blocks
from skimage.io import imread
from skimage import measure


# Main
if __name__ == "__main__":

    image = color.rgb2gray(imread("vaisseau.png"))
    print(image.shape)

    # Find contours
    black_contours = np.array(measure.find_contours(image, 0.05), dtype=object)
    white_contours = np.array(measure.find_contours(image, 0.95), dtype=object)

    contours = np.append(black_contours, white_contours)

    block_pos = np.zeros((contours.shape[0], 2))
    block_size = np.zeros((contours.shape[0], 2))

    for i, contour in enumerate(contours):
        block_pos[i][:] = np.mean(contour, axis=0)
        block_size[i][:] = np.amax(contour, axis=0) - np.amin(contour, axis=0)

    mean_size = np.mean(block_size, axis=0)

    # remove wrong detection
    rtol = 2e-1
    filter = np.logical_and(np.isclose(block_size[:, 0], mean_size[0], rtol=rtol), np.isclose(block_size[:, 1], mean_size[1], rtol=rtol))

    block_pos = block_pos[filter]
    block_size = block_size[filter]
    contours = contours[filter]
    black_contours = black_contours[filter[:black_contours.shape[0]]]
    white_contours = white_contours[filter[-white_contours.shape[0]:]]

    # number of blocks
    atolx = mean_size[0] / 2
    atoly = mean_size[1] / 2

    ny_block = np.count_nonzero(np.isclose(block_pos[:, 0], block_pos[0, 0], atol=atolx))
    nx_block = np.count_nonzero(np.isclose(block_pos[:, 1], block_pos[0, 1], atol=atoly))

    print("Total blocks:", block_pos.shape[0])
    print("nx blocks:", nx_block)
    print("ny blocks:", ny_block)

    # shape of blocks

    block_shape = (image.shape[0] // nx_block, image.shape[1] // ny_block)

    # calculate the few pixels to be removed to have a good size
    toRemove_xsize = image.shape[0] % nx_block
    toRemove_ysize = image.shape[1] % ny_block

    # see the image as a matrix of blocks (of shape block_shape)
    new_image = image[toRemove_xsize:, toRemove_ysize:]
    view = view_as_blocks(new_image, block_shape)

    # collapse the last two dimensions in one
    flatten_view = view.reshape(view.shape[0], view.shape[1], -1)

    # resample the image by taking the mean value of each blocks
    mean_view = np.mean(flatten_view, axis=2)
    cells = mean_view > 0.5

    # display results
    plt.subplot(131)
    plt.imshow(image, cmap=cm.Greys_r)
    plt.title("Original")
    plt.axis('off')

    plt.subplot(132)
    plt.imshow(image, cmap=cm.Greys_r)
    for contour in contours:
        plt.plot(contour[:, 1], contour[:, 0], linewidth=2)
    plt.title("Contours")
    plt.axis('off')

    plt.subplot(133)
    plt.imshow(cells, cmap=cm.Greys_r, aspect='equal')
    plt.title("Result, {} cells detected".format(np.count_nonzero(cells)))
    plt.axis('off')

    plt.show()
