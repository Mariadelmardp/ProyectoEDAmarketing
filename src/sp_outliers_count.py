import pandas as pd
import numpy as np 

import seaborn as sns
import matplotlib.pyplot as plt 


def count_outliers(df, columns):
  ''' 
  '''
  outliers_count={}
  outliers_percent={}
  for col in columns:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]
    outliers_count[col]= outliers.shape[0]
    outliers_percent[col]= round(outliers.shape[0]/df.shape[0],3)
  return outliers_count, outliers_percent

def analyze_ctr_witnout_outliers(df):
  # Análisis del CTR por campaña y canal
  ctr_by_campaign = df.groupby('campaign_type')['CTR'].mean().sort_values(ascending = False)
  ctr_by_channel = df.groupby('channel_used')['CTR'].mean().sort_values(ascending = False)
  
  print('CTR promedio por tipo de campaña:')
  display(ctr_by_campaign)
  print('CTR promedio por canal utilizado:')
  display(ctr_by_channel)
  
  # Crear el subplot
  fig, axes = plt.subplots(1, 2, figsize =(16 , 6))
  
  # Primer gráfico: CTR por tipo de campaña
  sns.barplot(x=ctr_by_campaign.index, y= ctr_by_campaign.values, palette='coolwarm', hue= ctr_by_campaign.index, ax=axes[0])
  axes[0].set_title('CTR promedio por tipo de campaña')
  axes[0].set_xticklabels(ctr_by_campaign.index, rotation = 45)
  axes[0].tick_params(axis='x', labelsize=10)  
  axes[0].tick_params(axis='y', labelsize=10) 
  
    # Segundo gráfico: CTR por canal utilizado
  sns.barplot(x=ctr_by_channel.index, y= ctr_by_channel.values, palette='viridis', hue= ctr_by_channel.index, ax=axes[1])
  axes[1].set_title('CTR promedio por canal utilizado')
  axes[1].set_xticklabels(ctr_by_channel.index, rotation = 45)
  axes[1].tick_params(axis='x', labelsize=10)  
  axes[1].tick_params(axis='y', labelsize=10) 
  
  # Ajustar el layout para los titulos y etiquetas no se solapen
  plt.tight_layout();
  
  
  
def filter_outliers(df, lista_columna):
  df_filter= df.copy()
  for col in lista_columna:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    df_filter = df_filter[(df_filter[col]>= lower_bound) & (df_filter[col]<= upper_bound)]
    return df_filter