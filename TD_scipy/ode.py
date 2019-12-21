#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File : ode.py
# Created by Anthony Giraudo the 09/12/2019

"""ODE solving
"""

# Modules

import numpy as np
from scipy.integrate import odeint
from scipy_utils import Cx
import matplotlib.pyplot as plt


# Functions

def g():
    """
    :return: constant g
    """
    return 9.81


def Re(v, nu, R):
    """
    :param v: velocity
    :param nu: kinematic viscosity
    :param R: radius
    :return: computed reynold number
    """
    return abs(v)*R/nu


def func(v, t0, rho, nu, R, m):
    """
    Compute the derivative of v at t0
    :param v: velocity
    :param t0: time
    :param rho: volumic mass
    :param nu: kinematic velocity
    :param R: radius
    :param m: mass
    :return: computed derivative of v at t0
    """
    S = np.pi*R**2
    return -g() + 1/(2*m)*rho*S*Cx(Re(v, nu, R))*v**2   # TODO: +/- ???


# Main
if __name__ == "__main__":
    # problem parameters
    rho = 1.2
    nu = 1.6e-5
    R = (43/2)*1e-3
    m = 45e-3

    t = np.linspace(0, 10, 100)
    v0 = 1e-5

    # solve ode
    v = odeint(func, v0, t, args=(rho, nu, R, m))

    # plot velocity
    plt.subplot(224)
    plt.plot(t, v)
    plt.xlabel("t(s)")
    plt.ylabel("v (m/s)")

    # plot Re
    plt.subplot(222)
    plt.plot(t, Re(v, nu, R))
    plt.xlabel("t (s)")
    plt.ylabel("Re")

    # plot Cx
    plt.subplot(121)
    re = np.logspace(-2, 8, 100)
    plt.plot(re, Cx(re), marker='*')
    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel("Re")
    plt.ylabel("$C_x$")

    plt.show()
