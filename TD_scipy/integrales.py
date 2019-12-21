#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File : integrales.py
# Created by Anthony Giraudo the 03/12/2019

"""FIXME: INCOMPLET
"""

# Modules

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erf


# Functions

def f1(t):
    return np.exp(-t**2)

"""
def get_tn_yn(f, tmin, tmax, n):
    tn = np.linspace(tmin, tmax, 2**n)
    dt = tn[1] - tn[0]
    yn = f(tn)
    return tn, yn, dt
"""

def trapeze(tn, f):
    dt = tn[1:] - tn[:-1]
    x1, x2 = tn[:-1] + dt/3, tn[:-1] + 2*dt/3
    return np.sum(dt/2 * (f(x1) + f(x2)))


def milne(tn, f):
    dt = (tn[1:] - tn[:-1])
    x1, x2, x3 = tn[:-1] + dt/4, tn[:-1] + 2*dt/4, tn[:-1] + 3*dt/4
    return np.sum(dt/3 * (2*f(x1) - f(x2) + 2*f(x3)))


def mid_point(tn, f):
    dt = tn[1:] - tn[:-1]
    x = tn[:-1] + dt / 2
    return np.sum(dt*f(x))


# Main
if __name__ == "__main__":
    tmin, tmax = 0, 1
    nmax = 20

    plt.subplot(221)
    x1 = np.linspace(0, 5, 10000)
    y1 = np.sqrt(np.pi)/2 * erf(x1)
    plt.plot(x1, y1)
    plt.title("Solution analytique")
    plt.xlabel("x")
    plt.ylabel("$\int_0^xdte^{-t^2}$")  # TODO: pas beau latex

    plt.subplot(222)
    x2 = np.linspace(tmin, tmax, 10000)
    y2 = f1(x2)
    plt.plot(x2, y2)
    plt.title("Integrande sur [{:.2f};{:.2f}]".format(tmin, tmax))

    plt.subplot(223)
    list_n = np.arange(nmax)
    list_resn_trap = []
    list_resn_mid = []
    list_resn_milne = []
    list_dtn = []
    for n in range(nmax):
        tn = np.linspace(tmin, tmax, 2**n+1)
        list_dtn += [tn[1] - tn[0]]
        list_resn_trap += [trapeze(tn, f1)]
        list_resn_milne += [milne(tn, f1)]
        list_resn_mid += [mid_point(tn, f1)]
    plt.plot(list_n, list_resn_trap)

    plt.subplot(224)
    list_resn_trap = np.array(list_resn_trap)
    list_resn_mid = np.array(list_resn_mid)
    list_resn_milne = np.array(list_resn_milne)
    list_errn_trap = abs(np.sqrt(np.pi) / 2 * erf(1) - list_resn_trap)
    list_errn_mid = abs(np.sqrt(np.pi) / 2 * erf(1) - list_resn_mid)
    list_errn_milne = abs(np.sqrt(np.pi) / 2 * erf(1) - list_resn_milne)

    plt.plot(list_dtn, list_errn_trap, label="trapeze")
    plt.plot(list_dtn, list_errn_mid, label="mid point")
    plt.plot(list_dtn, list_errn_milne, label="milne")
    plt.legend()

    plt.loglog()

    plt.show()
