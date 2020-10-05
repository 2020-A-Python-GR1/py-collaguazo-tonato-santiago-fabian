# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 07:58:39 2020

@author: Santiago
"""


# g_iloc_loc.py

import pandas as pd

path_guardado = path = "./data/artwork_data.pickle"

df = pd.read_pickle(path_guardado)

#loc

# primero = df.loc[1035]
# segundo = df.loc[1035, artist]

filtrado_horizontal = df.loc[1035] #Serie
print (filtrado_horizontal)
print(filtrado_horizontal['artist'])
print(filtrado_horizontal.index) #Indices columnas


serie_vertical = df['artist']

print(serie_vertical)
print(serie_vertical.index) #Indices son los Indices

# Filtrado por indice
df_1035 = df[df.index == 1035]

# loc -> acceder a un grupo de filas y columnas x LABEL (ARR TRUE FALSE)
segundo = df.loc[1035] #Filtrar por indice (1)
segundo = df.loc[[1035, 1036]] #Filtar por arr indices

segundo = df.loc[3:5] # Filtando desde x indice
                        #hasta y indice

segundo = df.loc[df.index == 1035] #Filtrar por
                                #Arreglo -> true Flase

segundo = df.loc[1035, 'artist'] #1 Indice

segundo = df.loc[1035, ['artist', 'medium']] #Varios inices

#print(df.loc[0]) # Indice dentro del Dataframe
#print(df[0]) #Indice dentro del Dataframe

# iloc - indices en 0

tercero = df.iloc[0]
tercero = df.iloc[[0,1]]
tercero = df.iloc[0:10]
tercero = df.iloc[df.index == 1035] 

tercero = df.iloc[0:10, 0:4] #Filtrado indices
                            #por rango de indice 0:4


#######################
datos = {
    "nota 1":{
        "Pepito": 7,
        "Juanita": 8,
        "Maria": 9
        },
    "nota 2":{
        "Pepito": 7,
        "Juanita": 8,
        "Maria": 9
        },
    "disciplina":{
        "Pepito": 4,
        "Juanita": 9,
        "Maria": 2
        },
    }
notas = pd.DataFrame(datos)

condicion_nota = notas["nota 1"] > 7
condicion_nota_dos = notas["nota 2"] > 7
condicion_disc = notas["disciplina"] >7

mayores_siete = notas.loc[condicion_nota,["nota 1"]]

pasaron = notas.loc[condicion_nota][condicion_nota_dos][condicion_disc]

notas.loc["Maria", "disciplina"] = 7
notas.loc[:, "disciplina"] = 7

##PRomedio de las 3 notas (no1+no2+disc)/3

prom=(notas["nota 1"]+notas["nota 2"] +notas["disciplina"])/3 





