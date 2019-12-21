#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File : linfit.py
# Created by Anthony Giraudo the 17/11/2019

"""
Linear fitting and plotting
"""

# Modules

import numpy as np
import matplotlib.pyplot as plt


# Functions

def set1():
    x = np.array([10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5])
    y = np.array([8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68])
    return x, y


# Main

if __name__ == "__main__":
    x, y = set1()

    p = np.polyfit(x, y, deg=1)
    x_fit = np.linspace(np.amin(x), np.amax(x), 10000)
    y_fit = p[1] + p[0] * x_fit

    plt.figure(figsize=(10, 10))
    plt.scatter(x, y)
    plt.plot(x_fit, y_fit, label="y = {:.2f} x + {:.2f}".format(p[0], p[1]))

    plt.xlabel("axe X")
    plt.ylabel("axe Y")
    plt.title("Anscombe : set 1")
    plt.legend()

    plt.show()
