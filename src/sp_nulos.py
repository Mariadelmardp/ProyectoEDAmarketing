import pandas as pd
import numpy as np

def gestion_nulos (df, umbral=10):
  
  columns_with_nulls= df.columns[df.isnull().any()]
  null_columns_info = pd.DataFrame(
    {'Column': columns_with_nulls,
     'Datatype': [df[col].dtype for col in columns_with_nulls],
     'NullCount': [df[col].isnull().sum() for col in columns_with_nulls],
     'Null%': [((df[col].isnull().sum() / df.shape[0]) *100) for col in columns_with_nulls]
      
    }
  )
  display(null_columns_info)
  high_null_cols= null_columns_info[null_columns_info['Null%']>umbral]['Column'].to_list()
  low_null_cols= null_columns_info[null_columns_info['Null%']<=umbral]['Column'].to_list()
  return high_null_cols, low_null_cols