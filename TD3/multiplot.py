#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File : multiplot.py
# Created by Anthony Giraudo the 17/11/2019

"""
Linear fitting and multiplotting
"""

# Modules

import numpy as np
import matplotlib.pyplot as plt


# Functions

def set1():
    x = np.array([10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5])
    y = np.array([8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68])
    return x, y


def set2():
    x = np.array([10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5])
    y = np.array([9.14, 8.14, 8.74, 8.77, 9.26, 8.1, 6.13, 3.1, 9.13, 7.26, 4.74])
    return x, y


def set3():
    x = np.array([10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5])
    y = np.array([7.46, 6.77, 12.74, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73])
    return x, y


def set4():
    x = np.array([8, 8, 8, 8, 8, 8, 8, 19, 8, 8, 8])
    y = np.array([6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25, 12.5, 5.56, 7.91, 6.89])
    return x, y


# Main

if __name__ == "__main__":
    sets = [set1, set2, set3, set4]

    plt.figure(figsize=(10, 10))
    for i in range(4):
        plt.subplot(221+i)

        x, y = sets[i]()

        p = np.polyfit(x, y, deg=1)
        x_fit = np.linspace(np.amin(x), np.amax(x), 10000)
        y_fit = p[1] + p[0] * x_fit

        plt.scatter(x, y)
        plt.plot(x_fit, y_fit, label="y = {:.2f} x + {:.2f}".format(p[0], p[1]))

        plt.xlabel("axe X")
        plt.ylabel("axe Y")
        plt.title("Anscombe : set {}".format(i+1))
        plt.legend()

    plt.show()
