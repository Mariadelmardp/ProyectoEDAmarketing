import pandas as pd
import numpy as np

def calcular_porcentaje_nulos(df):
  '''
  Función para calcular el número de nulos
  '''
  nulos = round(df.isnull().sum()/df.shape[0]*100,2)
  return nulos

def analisis_general_cat(df):
  col_cat=df.select_dtypes(include='O').columns
  if len(col_cat) == 0:
    print('No hay columnas categóricas')
  else:
    for col in col_cat:
      print(f'La distribución de la columna {col.upper()}')
      print(f'Esta columna tiene {len(df[col].unique())} valores únicos')
      display(df[col].value_counts(normalize=True))
      print('----------------- \n Describe')
      display(df[col].describe())
      print('__________________')