#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File : non_lin_eq.py
# Created by Anthony Giraudo the 01/12/2019

"""Resolution of a non linear equation.
"""

# Modules

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq
from scipy.special import lambertw
from scipy.optimize import curve_fit


# Functions

def f(i, u, isat, rdyn, u0):
    """Function for which we want to find the roots
    :param i: the unknown variable i, the intensity
    :param u: the voltage for which we want i
    :param isat: saturation current
    :param rdyn: dynamical resistance of the diode
    :param u0: thermical tension
    :return: the value of the function we want to find the roots
    """
    return rdyn*(i + isat)/u0 * np.exp(rdyn*(i + isat)/u0) - rdyn*isat/u0 * np.exp((u+rdyn*isat)/u0)


def f_fit(u, us):
    """Function to fit the pass band
    :param u: voltage at the diode terminals
    :param us: voltage at the junction terminals
    :return: value of the function we want to fit the pass band
    """
    global rdyn  # TODO: how to avoid this ?
    return (u - us)/rdyn


# Main
if __name__ == "__main__":
    isat, rdyn, u0 = 10e-9, 25e-3, 26e-3

    fig = plt.figure()

    # linear scale
    plt.subplot(121)
    # numerical solution
    u = np.geomspace(1e-2, 3, 10)
    i = np.array(tuple(brentq(f, 0, 100, args=(v, isat, rdyn, u0)) for v in u))
    plt.scatter(u, i, marker='*', color='green', label="Numerical solution (root finding)")
    # analytical solution
    x = np.linspace(np.amin(u), np.amax(u), 10000)
    y = lambertw(rdyn*isat/u0*np.exp((x+rdyn*isat)/u0))*u0/rdyn - isat
    plt.plot(x, y, label="Analytical solution")
    # fitting over pass band
    popt, pcov = curve_fit(f_fit, u[i>1], i[i>1])
    us = popt[0]
    y_fit = f_fit(x, us)
    plt.plot(x, y_fit, color='red', label="Fitting over pass band\nRI=U-U_s with U_s={:.2f} V".format(us))
    # visual settings
    plt.xlim(np.amin(u), np.amax(u))
    plt.xlabel("U (V)")
    plt.ylabel("I (A)")
    plt.legend()

    # log10 scale
    plt.subplot(122)
    plt.scatter(u, i, marker='*', color='green', label="Numerical solution (root finding)")
    plt.plot(x, y, label="Analytical solution")
    # visual settings
    plt.xlim(np.amin(u), np.amax(u))
    plt.yscale("log")
    plt.xlabel("U (V)")
    plt.ylabel("I (A)")
    plt.legend()

    # show results
    fig.suptitle("Diode caracteristic")
    plt.show()
