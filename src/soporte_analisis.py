import pandas as pd
import numpy as np 

def eda_preliminar(df):
  display(df.sample(5))
  print('________________')
  print('INFO')
  df.info()
  print('________________')
  print('NULOS')
  display(round(df.isnull().sum()/df.shape[0]*100,2))
  print('________________')
  print('DUPLICADOS')
  display(df.duplicated().sum())  
  print('________________')
  print('VALORES ÚNICOS')
  for col in df.select_dtypes(include='O').columns:
    print(df[col].value_counts())
    print('_______________')
    
def valores_minuscula(df):
  for col in df.select_dtypes(include='O').columns:
    df[col] = df[col].str.lower() 
    
def dolares (df, lista_col):
  for col in lista_col:
    df[col]=df[col].str.replace('$', ' ').str.replace(',', '')      

def comas (df, lista_col):
  for col in lista_col:
    df[col]=df[col].str.replace(',', '.')
    
def convertir_columnas (df, formato_fecha):
  for col in df.columns:
    for dtype in [float, int]:
      try:
       df[col]=df[col].astype(dtype)
      except:
       pass
    try:
       df[col]=pd.to_datetime(df[col], format=formato_fecha)
    except: 
      pass 