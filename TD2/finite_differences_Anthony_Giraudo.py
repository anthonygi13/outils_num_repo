#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File : finite_differences_Anthony_Giraudo.py
# Created by Anthony Giraudo the 05/11/2019

"""
Function discretisation and gradient calculation from the discretisation
"""

# Modules

import numpy as np


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


def partial_x(grid, dx):
    """
    :param grid: discretised function
    :param dx: discretisation step size for x
    :return: the discretised partial derivative with respect to x
    """
    return (np.roll(grid, -1, axis=0) - np.roll(grid, 1, axis=0)) / (2*dx)


def partial_y(grid, dy):
    """
    :param grid: discretised function
    :param dy: discretisation step size for y
    :return: the discretised partial derivative with respect to y
    """
    return (np.roll(grid, -1, axis=1) - np.roll(grid, 1, axis=1)) / (2*dy)


# Main

if __name__ == "__main__":

    # calculate my gradient
    grid, dx, dy = get_grid()
    my_partial_x, my_partial_y = partial_x(grid, dx), partial_y(grid, dy)

    # calculate numpy gradient
    np_partial_x, np_partial_y = np.gradient(grid, dx, dy)

    # compare numpy gradient and mine
    print("Numpy gradient equal to mine (for non edge values): ", np.allclose(my_partial_x[1:-1], np_partial_x[1:-1])
          and np.allclose(my_partial_y[:, 1:-1], np_partial_y[:, 1:-1]))
