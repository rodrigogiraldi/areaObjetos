# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 22:04:27 2015

@author: rodrigo
"""

import numpy as np
import cv2
import sys
from matplotlib import pyplot as plt

sys.setrecursionlimit(100000)

img = cv2.imread('objetos2.png', 0)

tomInicial = 100
incrementoTom = 10


def visitar(x, y):

    visitados[x][y] = 1
    img[x][y] = contCor

    if(img[x-1][y] != 0 and visitados[x-1][y] == 0):
        visitar(x-1, y)
    if(img[x+1][y] != 0 and visitados[x+1][y] == 0):
        visitar(x+1, y)
    if(img[x][y-1] != 0 and visitados[x][y-1] == 0):
        visitar(x, y-1)
    if(img[x][y+1] != 0 and visitados[x][y+1] == 0):
        visitar(x, y+1)

visitados = np.zeros(img.shape)

contCor = tomInicial
    

for i in range (img.shape[0]):
    for j in range (img.shape[1]):
        if img[i][j] != 0:
            if visitados[i][j] == 0:
                contCor+=incrementoTom
                visitar(i, j)


plt.hist(img.ravel(), incrementoTom*2, [tomInicial, contCor+incrementoTom]);
plt.show();

cv2.imshow('output', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
