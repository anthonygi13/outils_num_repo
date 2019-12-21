#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Definition de fonctions pour faire des tests, a utiliser comme importation
de librairie (import numpy_utils with default name numpy_utils.py)
"""

# Importation des librairies
import numpy as np


# Definition des fonctions
def generate_testarray(ndim=3):
    """ Genere un numpy array de test pour l'exercice de slicing """
    # Definition du seed
    seed = 1523265419
    # Initialisation du random generator
    np.random.seed(seed)
    # Initialisation du format
    shape = np.random.randint(10,20,size=ndim)
    # Initialisation du numpy array
    arr = np.random.standard_normal(shape)
    return arr


def print_arrayspec(arr):
    """ Imprime rang et format de l'array """
    print("Le numpy array est de rang {} et de format {}"\
           .format(arr.ndim, arr.shape))
    return


# Programme principal
if __name__ == "__main__":
    # Test de la fonction sans specification de l'argument optionnel
    arr = generate_testarray()
    # Imprime les specifications de l'array
    print_arrayspec(arr)
    # Test de la fonction avec specification de l'argument optionnel
    arr = generate_testarray(ndim=5)
    # Imprime les specifications de l'array
    print_arrayspec(arr)

