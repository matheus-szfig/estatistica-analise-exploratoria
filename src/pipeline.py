import pandas as pd
from pandas import DataFrame

def pipeline_pre_process (df: DataFrame):
  df.drop(['EMPRESA (SIGLA)', 'ASK', 'RPK', 'ATK', 'RTK'], axis=1, inplace=True)

  df.replace({
    'HORAS VOADAS': { ',': '.' },
    'COMBUSTÍVEL (LITROS)': { ',': '.' }
  }, regex=True, inplace=True)

  df.dropna(axis=0, inplace=True)

  df['ANO'] = pd.to_numeric(df['ANO'], downcast='integer')
  df['MÊS'] = pd.to_numeric(df['MÊS'], downcast='integer')

  df['HORAS VOADAS'] = pd.to_numeric(df['HORAS VOADAS'])
  df['COMBUSTÍVEL (LITROS)'] = pd.to_numeric(df['COMBUSTÍVEL (LITROS)'])
  
  return df
