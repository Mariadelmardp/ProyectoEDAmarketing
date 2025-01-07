import pandas as pd
import numpy as np 

import seaborn as sns
import matplotlib.pyplot as plt 

def visualizacion_cat(df):
  #Seleccionar columnas categóricas
  col_cat=df.select_dtypes(include='O').columns
  
  if len(col_cat)== 0:
    print('No hay columnas categóricas')
    return
  
  #Configurar tamaño de la figura
  num_cols= len(col_cat)
  rows= (num_cols +2)//3
  fig, axes= plt.subplots(rows, 3, figsize=(15,rows*5))
  axes=axes.flatten() #Convertir los ejes a un array plano para facilitar la iteración
  
  # Generar gráficos para cada columna categórica
  for i, col in enumerate(col_cat):
    sns.countplot(data=df,
                      x=col,
                      ax=axes[i],
                      hue=col,
                      palette='tab10',
                      legend= False)
    axes[i].set_title(f'Distribución de {col}')
    axes[i].set_xlabel(col)
    axes[i].set_ylabel('Frecuencia')
    axes[i].tick_params(axis='x', rotation=90)
  for j in range(i+1, len(axes)):
        fig.delaxes(axes[j]);