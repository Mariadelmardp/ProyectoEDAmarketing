import pandas as pd
import numpy as np 

def preanalisis(ruta_archivo):
  df= cargar_datos(ruta_archivo)
  set_opciones(df)
  resumen_datos(df)
  return df

def cargar_datos(ruta_archivo):
  """Cargar los datos desde un archivo CSV, Parquet o Excel

  Args:
      ruta_artivo 
  """
  # Cargar archivos
  try:
      if ruta_archivo.endwith(".csv"):
        df = pd.read_csv(ruta_archivo)
      elif ruta_archivo.endswith(".parquet"):
        df= pd.read_parquet(ruta_archivo)
      elif ruta_archivo.endswith()(".xlsx"):
        df=pd.read_excel(ruta_archivo)
      else:
        raise ValueError ("Formato de archivo no soportado.")
  except Exception as e:
    print(f'Error al cargar los dtos: {e}')
    return None
  return df


def set_opcion(df):
  """ Normalizacionde texto

  Args:
      df 
  """
  pd.set_option('display.max.columns', None)
  df.columns =(df.columns.str.strip().str.replace(' ','_').str.lower())
  df = df.map(lambda x: x.strip().replace(' ', '_').lower() if isinstance(x, str) else x)
  return df 

def resumen_datos(df):
  
  """
  
  """
  
  #Resumen datos
  print('\n-----------Resumen de datos----------- \n-----------')
  print(f'El número de filas es: {df.shape[0]}\n----------')
  print(f'El número de columnas es: {df.shape[1]}\n----------')
  print('\nInformación general:')
  display(df.info())
  print('----------')
  num_dupl= df.duplicated().sum()
  print('El núemro de duplicados es: {num_dupl}')
  if num_dupl != 0:
    print(f'Eliminamos duplicados...')
    df.drop_duplicates(inplace=True)
    
  df_nulos = pd.DataFrame({'count':df.isnull().sum(), '%nulos': (df.isnull().sum() / df.shape[0].round(3) * 100)})
  df_nulos=df_nulos[df_nulos['count'] >0]
  df_nulos_sorted= df_nulos.sort_values(by='%nulos', ascending=False)
  print('Los nulos que tenemos en el conjunto de datos son:')
  display(df_nulos_sorted)
  
  columnas_por_tipo= {dtype: df.select_dtype(dtype).columns.tolist() for dtype in df.dtype.unique()}
  print(f'Los tipos de las columnas son:')
  display(pd.DataFrame(df.dtype, columns=['Tipo_dato']))
  print('\nColumnas agrupadas por tipo de dato:')
  for tipo, columnas in columnas_por_tipo.items():
    print(f'- {tipo}:, columnas')
  print('\n-----------------------------------------------\n')
  identificar_columnas_booleanas(df)
  print('---------------')
  display(df.head())
  
  return df

def identificar_columnas_booleanas(df):
  
  posibles_booleanas=[col for col in df.columns if set(df[col].dropna().unique()) <={0,1}]
  
  print(f'Columnas que podrían ser booleanas: {posibles_booleanas}' )
  return posibles_booleanas


def cambiar_tipo (df, formato_fecha):
  for col in df.columns:
    for dtype in [float, int]:
      try:
        df[col]=df[col].astype(dtype)
      except:
        pass
    try: 
      df[col] =pd.to_datetime(df[col], format=formato_fecha)
    except:
      pass               

def expan_fecha()


