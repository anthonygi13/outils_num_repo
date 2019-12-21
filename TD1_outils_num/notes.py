#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File : notes.py
# Created by Anthony Giraudo the 16/10/2019

"""
Affiche moyennes de resultats d'eleves
"""

# Modules

import random


# Functions

def moyenne(min_nb_note=3, max_nb_note=5):
    """
    :param min_nb_note: nombre minimal de notes pour l'eleve
    :param max_nb_note: nombre maximal de notes pour l'eleve
    :return: moyenne d'un eleve ayant eu un nombre aleatoire de notes aleatoires
    """
    somme = 0
    nb_notes = random.randint(min_nb_note, max_nb_note + 1)
    for i in range(nb_notes):
        somme += random.randint(0, 21)
    return somme/nb_notes


def print_moyennes(eleves, min_nb_note=3, max_nb_note=5):
    """
    Affiche les resulats des eleves
    :param min_nb_note: nombre minimal de notes pour chaque eleve
    :param max_nb_note: nombre maximal de notes pour chaque eleve
    :param eleves: liste de nom d'eleves
    """
    taille_max1 = 0
    taille_max2 = 0
    chaines1 = []
    chaines2 = []

    for eleve in eleves:

        chaines1 += ["Resultat de %s " % eleve]
        taille_max1 = len(chaines1[-1]) if len(chaines1[-1]) > taille_max1 else taille_max1

        res = moyenne(min_nb_note, max_nb_note)
        chaines2 += ["moyenne = %.2f" % res] if res >= 10 else ["moyenne =  %.2f (*)" % res]

    chaines = [chaine1 + (taille_max1 - len(chaine1)) * " " + ": " + chaine2 for chaine1, chaine2 in zip(chaines1, chaines2)]
    print("\n".join(chaines))


# Main
if __name__ == "__main__":
    print_moyennes({"Christophe", "David", "Ruben", "Stephane"})
