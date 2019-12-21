#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File : documentations.py
# Created by Anthony Giraudo the 16/10/2019

"""
Affiche longueur de la doc numpy, matplotlib et scipy
"""

# Modules

import importlib
import inspect


# Functions

def print_info(module_name):
    """
    Print taille de la doc et version d'un module
    :param module_name: nom du module
    """
    module = importlib.import_module(module_name)  # objet module
    taille = 0
    for f in inspect.getmembers(module, inspect.isfunction):  # pour chaque fonction du module
        doc = inspect.getdoc(f[1])  # recupere la doc
        taille += len(doc) if doc else 0  # somme sa longueur si la doc existe
    print("Documentation de %s (version %s): %d caracteres"%(module_name, module.__version__, taille))


# Main
if __name__ == "__main__":
    for module_name in {"numpy", "scipy", "matplotlib"}:
        print_info(module_name)
