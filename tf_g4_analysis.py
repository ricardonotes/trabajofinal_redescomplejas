# -*- coding: utf-8 -*-
"""TF-G4-Analysis.ipynb

Automatically generated by Colaboratory.

# Trabajo Final - Palabras de soporte complementarias a la calificación de un restaurant
## Grupo 4

### Importación de datasets originados por scrapping
"""

import pandas as pd

#Lectura de dataset de restaurantes de Lima
restaurants = pd.read_csv('./data/data/restaurants.csv', sep=',',engine='python')
restaurants.head()

#Lectura de reviews de restaurantes de Lima
reviews = pd.read_csv('./data/data/reviews.csv', sep=',',engine='python')
reviews.head()
