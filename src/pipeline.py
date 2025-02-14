import pandas as pd
from pandas import DataFrame

def remove_outliers_by_col(df, col, factor=1.5):

  # calculo da relação interquartil (iqr)
  q1 = df[col].quantile(0.25)
  q3 = df[col].quantile(0.75)
  iqr = q3 - q1
  
  # definição dos limites inferiores e superiores
  lower_bound = q1 - (factor * iqr)
  upper_bound = q3 + (factor * iqr)
  
  # remoção do dataset
  return df[(df[col] >= lower_bound) & (df[col] <= upper_bound)]

def pipeline_pre_process (df: DataFrame):

  # remoção de colunas não utilizadas
  df.drop([
    'EMPRESA (SIGLA)',
    'ASK',
    'RPK',
    'ATK',
    'RTK',
    'EMPRESA (NOME)',
    'EMPRESA (NACIONALIDADE)',
    'AEROPORTO DE ORIGEM (SIGLA)',
    'AEROPORTO DE ORIGEM (NOME)',
    'AEROPORTO DE ORIGEM (REGIÃO)',
    'AEROPORTO DE ORIGEM (PAÍS)',
    'AEROPORTO DE ORIGEM (CONTINENTE)',
    'AEROPORTO DE DESTINO (SIGLA)',
    'AEROPORTO DE DESTINO (NOME)',
    'AEROPORTO DE DESTINO (REGIÃO)',
    'AEROPORTO DE DESTINO (PAÍS)',
    'AEROPORTO DE DESTINO (CONTINENTE)',
    'NATUREZA',
    'GRUPO DE VOO',
    'CARGA PAGA (KG)',
    'CARGA GRÁTIS (KG)',
    'CORREIO (KG)',
  ], axis=1, inplace=True)
  df.dropna(axis=0, inplace=True)

  # ajuste do formato de inteiros
  df['ANO'] = pd.to_numeric(df['ANO'], downcast='integer')
  df['MÊS'] = pd.to_numeric(df['MÊS'], downcast='integer')

  # ajuste do formato de floats
  df.replace({
    'HORAS VOADAS': { ',': '.' },
    'COMBUSTÍVEL (LITROS)': { ',': '.' }
  }, regex=True, inplace=True)
  df['HORAS VOADAS'] = pd.to_numeric(df['HORAS VOADAS'])
  df['COMBUSTÍVEL (LITROS)'] = pd.to_numeric(df['COMBUSTÍVEL (LITROS)'])
  df['PASSAGEIROS PAGOS'] = pd.to_numeric(df['PASSAGEIROS PAGOS'])
  df['PASSAGEIROS GRÁTIS'] = pd.to_numeric(df['PASSAGEIROS GRÁTIS'])

  # remoção de valores não realisticos
  df = df.loc[df['HORAS VOADAS'] > 0.5]
  df = df.loc[df['COMBUSTÍVEL (LITROS)'] > 1.0]
  df = df.loc[(df['PASSAGEIROS PAGOS'] + df['PASSAGEIROS GRÁTIS']) > 1.0]

  # remoção de outliers
  df = remove_outliers_by_col(df, 'COMBUSTÍVEL (LITROS)')
  df = remove_outliers_by_col(df, 'HORAS VOADAS')
  df = remove_outliers_by_col(df, 'PASSAGEIROS PAGOS')
  df = remove_outliers_by_col(df, 'PASSAGEIROS GRÁTIS')
  
  return df

def get_descritive_values (df: DataFrame, col:str):

  print (col, '-', 'metrics')

  mean = df[col].mean()
  print ("mean", mean)
  
  median = df[col].median()
  print ("median", mean)
  mode = df[col].mode()
  print ("mode", mode)

  variance = df[col].var()
  print ("variance", variance)

  standard_deviation = df[col].std()
  print ("standard_deviation", standard_deviation)
  var_coef = (standard_deviation / mean) / 100
  print ("var_coef", var_coef)

  quartile25 = df[col].quantile(0.25)
  print ("quartile25", quartile25)
  quartile50 = df[col].quantile(0.5)
  print ("quartile50", quartile50)
  quartile75 = df[col].quantile(0.75)
  print ("quartile75", quartile75)

  max = df[col].max()
  print ("max", max)
  min = df[col].min()
  print ("min", min)

  return {
    "mean": mean,
    "median": median,
    "mode": mode,
    "var": variance,
    "std": standard_deviation,
    "coef_var": var_coef,
    "q25": quartile25,
    "q50": quartile50,
    "q75": quartile75,
    "max": max,
    "min": min
  }

def get_correlation (df: DataFrame, col:str, corr_col:str):

  corr = df[[col, corr_col]].corr(method='pearson').loc[col, corr_col]
  print(col, 'x', corr_col, 'correlation:', corr)
  return corr