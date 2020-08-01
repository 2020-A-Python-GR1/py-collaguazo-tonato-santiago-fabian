# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 09:23:53 2020

@author: Santiago
"""


# c_dataframes.py

import numpy as np
import pandas as pd

arr_pand = np.random.randint(0,10,6).reshape(2,3)

df1 = pd.DataFrame(arr_pand)

s1 = df1[0]

#operacion con la seria

s2 = df1[1]

s2 = df1[2]

df1[3] = s1

df1[4] = s1 * s2

datos_fisicos_uno = pd.DataFrame(
    arr_pand,
    columns = [
    'Estatura (cm)',
    'Peso (kg)',
    'Edad (anios)'])

datos_fisicos_dos = pd.DataFrame(
    arr_pand,
    columns = [
    'Estatura (cm)',
    'Peso (kg)',
    'Edad (anios)'],
    index = [
        'Santiago',
        'Fabian'])

serie_peso = datos_fisicos_dos ['Peso (kg)']
datos_santiago = serie_peso['Santiago']
print(serie_peso)
print (datos_santiago)

df1.index = ['Santiago', 'Fabian']
df1.index = ['Wendy', 'carolina']
df1.columns = ['A', 'B', 'C', 'D', 'E']  

  
