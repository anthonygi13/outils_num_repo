#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File : electricite.py
# Created by Anthony Giraudo the 24/11/2019

"""FIXME: INCOMPLET
"""

# Modules

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.mlab import _csv2rec
from datetime import datetime
from scipy.optimize import least_squares


# Functions

def get_data(filename):
    data = _csv2rec("electricite.csv")
    return data.date, data.twh


def fit_poly(seconds, twh):
    p = np.polyfit(seconds, twh, deg=2)
    return p[0], p[1], p[2]


def f_to_fit(x, seconds, p):
    return (p[0]*seconds**2 + p[1]*seconds + p[2]) + x[0]*np.sin(x[1]*seconds)


# Main
if __name__ == "__main__":
    date, twh = get_data("electricite.csv")
    seconds = date.astype("datetime64[s]").astype(int)

    plt.subplot(121)
    p = fit_poly(seconds, twh)
    plt.plot(date, twh, label='data')
    plt.ylabel("Consommation (TWh/mois)")

    x = np.linspace(np.amin(seconds), np.amax(seconds), 10000)
    y = p[0]*x**2 + p[1]*x + p[2]
    x = x.astype("datetime64[s]")
    plt.plot(x, y, label="polynomial comp.")

    plt.subplot(122)
    freqs = abs(np.fft.fftfreq(twh.shape[0]))
    fft = np.fft.fft(twh)
    plt.plot(freqs, fft)

    plt.legend()
    plt.show()
