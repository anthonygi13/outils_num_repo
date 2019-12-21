#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File : gammaray.py
# Created by Anthony Giraudo the 24/11/2019

"""Plot histogram and fit the distribution by 2 different ways
"""

# Modules

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


# Functions

def get_data(filename):
    """
    :param filename: file name with T90 data to be extracted
    :return: 1D numpy array containin the different T90 values
    """
    data = np.loadtxt(filename, comments='#', delimiter="    ")
    T90 = data[:, 4]
    return T90


def bi_normal(x, mean1, mean2, std1, std2, high1, high2):
    """
    :param x: x value
    :param mean1: mean of the first gaussian
    :param mean2: mean of the second gaussian
    :param std1: standard deviation for the first gaussian
    :param std2: standard deviation for the second gaussian
    :param high1: high for the first gaussian
    :param high2: high for the second gaussian
    :return: value of the specified bi-gaussian for value x
    """
    return high1 * np.exp(-(x-mean1)**2/(2*std1**2)) + high2 * np.exp(-(x-mean2)**2/(2*std2**2))


def bi_lognormal(x, mean1, mean2, std1, std2, high1, high2):
    """
    Notice that the meani and stdi parameters do not actually correspond to the real mean and std of the log-gaussians
    but to the mean and std of the gaussians defined by taking log10(x) as a variable instead of x.
    :param x: x value
    :param mean1: mean characterising the first log-gaussian
    :param mean2: mean characterising the second log-gaussian
    :param std1: standard deviation characterising the first log-gaussian
    :param std2: standard deviation characterising the second log-gaussian
    :param high1: high characterising the first log-gaussian
    :param high2: high for the second log-gaussian
    :return: value of the specified bi-log-gaussian for value x
    """
    return bi_normal(np.log10(x), mean1, mean2, std1, std2, high1, high2)


def fit_bi_normal(data, nbins=23):
    """
    :param data: T90 data to be fitted
    :param nbins: number of bins for the histogram
    :return: fitted parameters when fitting the log10(T90) histogram with a bi-gaussian
    """
    hist, bin_edges = np.histogram(np.log10(data), np.linspace(np.log10(np.amin(data)), np.log10(np.amax(data)), nbins))
    x = (bin_edges[1:] + bin_edges[:-1]) / 2
    # plt.scatter(10**x, np.ones(x.shape[0])*60, color='red')
    popt, pcop = curve_fit(bi_normal, x, hist, p0=(-0.5, 1.5, 0.75, 0.5, 60, 160))
    mean1, mean2, std1, std2, high1, high2 = popt[0], popt[1], abs(popt[2]), abs(popt[3]), popt[4], popt[5]
    return mean1, mean2, std1, std2, high1, high2


def fit_bi_lognormal(data, nbins=23):
    """
    :param data: T90 data to be fitted
    :param nbins: number of bins for the histogram
    :return: fitted parameters when fitting the T90 histogram with a bi-log-gaussian
    """
    hist, bin_edges = np.histogram(data, np.logspace(np.log10(np.amin(T90)), np.log10(np.amax(T90)), nbins))
    x = np.sqrt(bin_edges[1:] * bin_edges[:-1])
    # plt.scatter(x, np.ones(x.shape[0])*60, color='orange')
    popt, pcop = curve_fit(bi_lognormal, x, hist, p0=(-0.5, 1.5, 0.75, 0.5, 60, 160))
    mean1, mean2, std1, std2, high1, high2 = popt[0], popt[1], abs(popt[2]), abs(popt[3]), popt[4], popt[5]
    return mean1, mean2, std1, std2, high1, high2


# Main
if __name__ == "__main__":
    # extract data and plot histogram
    T90 = get_data("4br_grossc.duration")
    plt.hist(T90, np.logspace(np.log10(np.amin(T90)), np.log10(np.amax(T90)), 23), edgecolor='black')
    plt.xscale("log")
    plt.title("Histogram with 23 bins")
    plt.xlabel("T_90 (s)")
    plt.ylabel("# events")

    # fit the log10(T90) histogram with a bi-gaussian and plot the result
    mean1, mean2, std1, std2, high1, high2 = fit_bi_normal(T90)
    x = np.linspace(np.log10(np.amin(T90)), np.log10(np.amax(T90)), 10000)
    y = bi_normal(x, mean1, mean2, std1, std2, high1, high2)
    plt.plot(10**x, y, label="Bimodal normal fit\nMax at {:.2f} and {:.2f} s".format(10**mean1, 10**mean2))

    # fit the T90 histogram with a bi-log-gaussian
    mean1, mean2, std1, std2, high1, high2 = fit_bi_lognormal(T90)
    x = np.logspace(np.log10(np.amin(T90)), np.log10(np.amax(T90)), 10000)
    y = bi_lognormal(x, mean1, mean2, std1, std2, high1, high2)
    plt.plot(x, y, label="Bimodal lognormal fit\nMax at {:.2f} and {:.2f} s".format(10**mean1, 10**mean2))

    plt.legend()
    plt.show()
