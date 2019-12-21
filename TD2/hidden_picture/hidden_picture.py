#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File : hidden_picture.py
# Created by Anthony Giraudo the 12/11/2019

"""ATTENTION: respecte pas les consignes du TD
"""

# Modules

from matplotlib.pyplot import imread
import numpy as np
from numpy_stegano_utils import plot_stegano


# Functions

def hide(foreground, background):
    if background.shape[0] > foreground.shape[0] or background.shape[1] > foreground.shape[1]:
        raise ValueError("Background image bigger than foreground image...")
    mix = np.array(foreground, copy=True)
    mix[:background.shape[0], :background.shape[1]] = np.left_shift(np.right_shift(foreground[:background.shape[0], :background.shape[1]], 4), 4) + np.right_shift(background, 4)

    return mix


# Main
if __name__ == "__main__":

    dragon = imread("dragon.jpeg")
    pika = imread("pika.jpg")
    plot_stegano(pika, dragon, hide(dragon, pika))
