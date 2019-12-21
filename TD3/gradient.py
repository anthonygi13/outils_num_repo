#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File : gradient.py
# Created by Anthony Giraudo the 17/11/2019

"""
Function discretisation and gradient calculation from the discretisation
"""

# Modules

import numpy as np
import matplotlib.pyplot as plt


# Functions

def f(x, y):
    """
    :param x: scalar or numpy array
    :param y: scalar or numpy array
    :return: f(x, y)
    """
    return np.exp(-x**2)*np.sin(y)


def get_grid(func=f, xmin=-5, xmax=5, ymin=0, ymax=2*np.pi, nx=51, ny=51):
    """
    :param func: two variable function to be discretised
    :param xmin: lower bound of x variable
    :param xmax: upper bound of x variable
    :param ymin: lower bound of y variable
    :param ymax: upper bound of y variable
    :param nx: grid size along x
    :param ny: grid size along y
    :return: the discretised function, the discretisation step size for x, the discretisation step size for y
    """
    x, y = np.meshgrid(np.linspace(xmin, xmax, nx), np.linspace(ymin, ymax, ny))
    dx = (xmax-xmin)/nx
    dy = (ymax - ymin)/ny
    return func(x, y), dx, dy


def partial_x_center(grid, dx):
    """
    :param grid: discretised function
    :param dx: discretisation step size for x
    :return: the discretised partial derivative with respect to x (centered method)
    """
    return (np.roll(grid, -1, axis=0) - np.roll(grid, 1, axis=0)) / (2*dx)


def partial_x_forward(grid, dx):
    """
    :param grid: discretised function
    :param dx: discretisation step size for x
    :return: the discretised partial derivative with respect to x (forward method)
    """
    return (np.roll(grid, -1, axis=0) - grid) / dx


def partial_x_backward(grid, dx):
    """
    :param grid: discretised function
    :param dx: discretisation step size for x
    :return: the discretised partial derivative with respect to x (backward method)
    """
    return (grid - np.roll(grid, 1, axis=0)) / dx


def partial_y_center(grid, dy):
    """
    :param grid: discretised function
    :param dy: discretisation step size for y
    :return: the discretised partial derivative with respect to y (centered method)
    """
    return (np.roll(grid, -1, axis=1) - np.roll(grid, 1, axis=1)) / (2*dy)


def partial_y_forward(grid, dy):
    """
    :param grid: discretised function
    :param dy: discretisation step size for y
    :return: the discretised partial derivative with respect to y (forward method)
    """
    return (np.roll(grid, -1, axis=1) - grid) / dy


def partial_y_backward(grid, dy):
    """
    :param grid: discretised function
    :param dy: discretisation step size for y
    :return: the discretised partial derivative with respect to y (backward method)
    """
    return (grid - np.roll(grid, 1, axis=1)) / dy


# Main

if __name__ == "__main__":
    # get grid, dx, dy
    grid, dx, dy = get_grid()

    # calculate numpy gradient
    np_partial_x, np_partial_y = np.gradient(grid, dx, dy)

    to_plot = [grid, np_partial_x, np_partial_y, abs(np_partial_x - partial_x_center(grid, dx)),
               abs(np_partial_x - partial_x_forward(grid, dx)), abs(np_partial_x - partial_x_backward(grid, dx)),
               abs(np_partial_y - partial_y_center(grid, dy)), abs(np_partial_y - partial_y_forward(grid, dy)),
               abs(np_partial_y - partial_y_backward(grid, dy))]
    titles = ["Champ", "$\Delta_x$ (numpy)", "$\Delta_y$ (numpy)", "$|\Delta_x^{np}-\Delta_x^{center}|$",
              "$|\Delta_x^{np}-\Delta_x^{for}|$", "$|\Delta_x^{np}-\Delta_x^{back}|$",
              "$|\Delta_y^{np}-\Delta_y^{center}|$", "$|\Delta_y^{np}-\Delta_y^{for}|$",
              "$|\Delta_y^{np}-\Delta_y^{back}|$"]

    plt.figure(figsize=(10, 10))

    # show differences between my gradient and numpy's
    for i in range(9):
        plt.subplot(331+i)
        plt.imshow(to_plot[i])
        plt.contour(to_plot[i])
        plt.title(titles[i])

    plt.show()
