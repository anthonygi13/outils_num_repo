#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File : slicing.py
# Created by Anthony Giraudo the 22/10/2019

"""
Some slicing examples
"""

# Modules

import numpy as np
from numpy_utils import generate_testarray


# Functions

def mid_value(a):
    """
    :param a: array numpy of dimension 3
    :return: mid value
    """
    imax, jmax, kmax = a.shape
    return a[(imax-1)//2, (jmax-1)//2, (kmax-1)//2]


def mean_pair_i(a):
    """
    :param a: array numpy of dimension 3
    :return: mean over pair indexes i
    """
    return np.mean(a[::2])


def mean_mult3_j(a):
    """
    :param a: array numpy of dimension 3
    :return: mean over divisible by 3 indexes j
    """
    return np.mean(a[:, 3::3])


def mean_firsthalf_k(a):
    """
    :param a: array numpy of dimension 3
    :return: mean over first half of k indexes
    """
    return np.mean(a[:, :, a.shape[2]//2])


def mean_nlast_k(a, n):
    """
    :param a: array numpy of dimension 3
    :param n: number of k indexes to take into account when calculating the mean
    :return: mean over the n last k indexes
    """
    return np.mean(a[:, :, -n:])


def mean_gtmed(a):
    """
    :param a: array numpy of dimension 3
    :return: mean over elements greater than the median
    """
    return np.mean(a[a >= np.median(a)])


# Main

if __name__ == "__main__":

    # random 3 dimensional array a
    a = generate_testarray(ndim=3)

    # print some properties of the array a
    print("Mid value :", mid_value(a))
    print("Mean over pair indexes i :", mean_pair_i(a))
    print("Mean over multiple of 3 j indexes :", mean_mult3_j(a))
    print("Mean over the first half of k indexes :", mean_firsthalf_k(a))
    print("Mean over the 3 last k indexes :", mean_nlast_k(a, 3))
    print("Mean over the 13 last k indexes :", mean_nlast_k(a, 13))
    print("Mean over elements greater than the median :", mean_gtmed(a))
