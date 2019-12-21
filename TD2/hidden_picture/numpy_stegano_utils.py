#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Definition de fonctions pour faire un plot d'images, a utiliser comme importation
de librairie (import numpy_stegano_utils with default name numpy_stegano_utils.py)
"""

# Importation des librairies
import matplotlib.pyplot as plt
                                   
# Definition des fonctions
def plot_stegano(*args, **kwargs):
   """ Routine de plot pour l'exercice de steganographie 
   Peut etre simplement appelee par plot_stegano(img1) pour visualiser l'image img1,
   ou plot_stegano(img1, img2) pour visualiser 2 images, ou plot(img1, img2, img3)
   pour visualiser 3 images, etc. **kwargs permet de passer les titres des plots
   sous la forme d'un dictionnaire, et eventuellement sauver le resultat """
   # Determine le nombre de plot
   nplot = len(args)
   # Recupere les clefs des commentaires
   if kwargs:
      keys = kwargs.keys()
   # Creation du support de l'oeuvre (unites = pouces!)
   fig = plt.figure(figsize=(4*nplot, 4))
   # Creation de l'oeuvre
   iplot = 1
   for arg in args:
      plt.subplot(1,nplot,iplot)
      plt.imshow(arg)
      # Les titres
      key_title = 'Title{}'.format(iplot)
      if kwargs and key_title in keys:
         plt.title(kwargs[key_title])
      iplot += 1
   # Sauvegarde
   if True:
      key_savepng = 'Pngname'
      if kwargs and key_title in keys:
         plt.savefig(kwargs[key_savepng])
   # Visualisation
   plt.show()
   return
      
# Programme principal
if __name__ == "__main__":
   pass
