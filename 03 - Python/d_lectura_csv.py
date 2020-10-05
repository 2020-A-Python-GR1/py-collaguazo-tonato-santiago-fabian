# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 10:08:05 2020

@author: Santiago
"""


# d_lectura_csv.py

import pandas as pd
import os

path = "./data/artwork_data.csv"
# path = "c://users//usrbet//documents//.."

df1 = pd.read_csv(
    path,
    nrows=10)

columnas= ['id', 'artist', 'title',
           'medium', 'year',
           'acquisitionYear', 'height',
           'width', 'units']

df2 = pd.read_csv(
    path,
    nrows=10,
    usecols = columnas)

df3 = pd.read_csv(
    path,
    nrows=10,
    usecols = columnas,
    index_col = 'id')

df3 = pd.read_csv(
    path,
    usecols = columnas,
    index_col = 'id')

path_guardado = path = "./data/artwork_data.pickle"

df3.to_pickle(path_guardado)

df4 = pd.read_pickle(path_guardado)




