# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 09:36:57 2020

@author: Santiago
"""


#e_output_data
import pandas as pd
import numpy as np

import os
import sqlite3
import xlsxwriter

path_guardado = "./data/artwork_data.pickle"
df = pd.read_pickle(path_guardado)
sub_df = df.iloc[49980:50519,:].copy()

# Tipos Archivos
#JSON
#Excel
#SQL

#artwork_data.xlsx
path_excel = "./data/artwork_data.xlsx"

#Con el indice como columna
sub_df.to_excel(path_excel)

#Sin el indice como columna
sub_df.to_excel(path_excel, index = False)

columnas = ['artist', 'title', 'year']
sub_df.to_excel(path_excel, columns = columnas)

#Multiples hojas de trabajo
path_excel_mt = "./data/artwork_data_mt.xlsx"

writer = pd.ExcelWriter(path_excel_mt,
                         engine = 'xlsxwriter')

sub_df.to_excel(writer, sheet_name = 'Primera')
sub_df.to_excel(writer, sheet_name = 'Segunda')
sub_df.to_excel(writer, sheet_name = 'Tercera')
writer.save()

#Formato condicional#


path_excel_colores = "./data/artwork_data_colores.xlsx"

writer = pd.ExcelWriter(path_excel_colores,
                        engine='xlsxwriter') 
#series
num_artistas = sub_df['artist'].value_counts()
#print(type(num_artistas))
#print(num_artistas)

num_artistas.to_excel(writer, sheet_name = 'Artistas')

#Seleccionar la hoja de trabajo
hoja_artistas = writer.sheets['Artistas']


#formato
ultimo_numero = len(num_artistas.index) +1

#rango de celdas B2:B{}.format()


rango_celdas = f'B2:B{ultimo_numero}' #B2:B85
print (rango_celdas)
formato_artistas = {
    "type":'2_color_scale',
    "min_value": "18",
    "min_type": "percentile",
    "max_value": "99",
    "max_type": "percentile"}

hoja_artistas.conditional_format(rango_celdas, formato_artistas)
writer.save()



workbook = xlsxwriter.Workbook('artistas_chart.xlsx')
worksheet = workbook.add_worksheet()

# Add the worksheet data to be plotted.
data = [10, 40, 50, 20, 10, 50]
worksheet.write_column('A2', num_artistas.index)
worksheet.write_column('B2', num_artistas)

# Create a new chart object.
chart = workbook.add_chart({'type': 'column'})

# Add a series to the chart.
custom_labels =num_artistas.index
chart.add_series({'values': '=Sheet1!B2:B85',
                  'fill':   {'color': '#FF9900'},
                      'name':       'Artistas',
                   'categories': '=Sheet1!$A$2:$A$84',
                      'data_labels': {'value': True, 'custom': custom_labels, 'position': 'below'},
})
                    
# Insert the chart into the worksheet.
worksheet.insert_chart('D2', chart)

workbook.close()

print(num_artistas.index)
 
