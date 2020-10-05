# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 07:33:09 2020

@author: Santiago
"""


# f_indices_filtrado.py

import pandas as pd

path_guardado = path = "./data/artwork_data.pickle"

df = pd.read_pickle(path_guardado)

serie_artista_dup = df['artist']

artistas = pd.unique(serie_artista_dup)

print(type(artistas))

print (artistas.size)

print(len(artistas))

blake = df['artist'] == 'Blake, William' #serie

print (blake.value_counts())

df_blake = df[blake]

