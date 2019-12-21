#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File : ode2.py
# Created by Anthony Giraudo the 10/12/2019

"""FIXME: INCOMPLET
"""

# Modules

import numpy as np
from scipy_utils import Cx
from scipy.integrate import odeint
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


def func(Y, t0, rho, nu, R, m):
    x, y, vx, vy = Y[0], Y[1], Y[2], Y[3]
    S = np.pi * R ** 2
    v = np.sqrt(vx**2+vy**2)
    f = 1/2*rho*S*Cx(Re(v, nu, R))*v**2
    cos = vy / v
    fx = f * vx/v
    fy = f * vy/v
    return [vx, vy, -fx/m, -g()-fy/m]


# Main
if __name__ == "__main__":
    # problem parameters
    rho = 1.2
    nu = 1.6e-5
    R = (43 / 2) * 1e-3
    m = 45e-3
    v0 = 80

    t = np.linspace(0, 10, 100)

    # solve ode
    for theta in range(10, 90, 10):
        Y0 = np.array([0, 0, np.cos(np.pi*theta/180) * v0, np.sin(np.pi*theta/180) * v0])
        Y = odeint(func, Y0, t, args=(rho, nu, R, m))
        x, y, vx, vy = Y[:, 0], Y[:, 1], Y[:, 2], Y[:, 3]
        plt.subplot(121)
        plt.plot(x[y>=0], y[y>=0])
        plt.subplot(322)
        plt.plot(t[y>=0], Re(np.sqrt(vx**2+vy**2), nu, R)[y>=0])
        plt.subplot(324)
        plt.plot(t[y >= 0], vx[y >= 0])
        plt.subplot(326)
        plt.plot(t[y >= 0], vy[y >= 0])
    plt.show()
