import pandas as pd
from pandas import DataFrame

def remove_outliers_by_col(df, col, factor=1.5):

  q1 = df[col].quantile(0.25)
  q3 = df[col].quantile(0.75)
  iqr = q3 - q1
  
  lower_bound = q1 - (factor * iqr)
  upper_bound = q3 + (factor * iqr)
  
  return df[(df[col] >= lower_bound) & (df[col] <= upper_bound)]

def pipeline_pre_process (df: DataFrame):

  df.drop(['EMPRESA (SIGLA)', 'ASK', 'RPK', 'ATK', 'RTK'], axis=1, inplace=True)
  df.dropna(axis=0, inplace=True)

  df['ANO'] = pd.to_numeric(df['ANO'], downcast='integer')
  df['MÊS'] = pd.to_numeric(df['MÊS'], downcast='integer')

  df.replace({
    'HORAS VOADAS': { ',': '.' },
    'COMBUSTÍVEL (LITROS)': { ',': '.' }
  }, regex=True, inplace=True)
  df['HORAS VOADAS'] = pd.to_numeric(df['HORAS VOADAS'])
  df['COMBUSTÍVEL (LITROS)'] = pd.to_numeric(df['COMBUSTÍVEL (LITROS)'])
  df['PASSAGEIROS PAGOS'] = pd.to_numeric(df['PASSAGEIROS PAGOS'])
  df['PASSAGEIROS GRÁTIS'] = pd.to_numeric(df['PASSAGEIROS GRÁTIS'])

  df = df.loc[df['HORAS VOADAS'] > 0.5]
  df = df.loc[df['COMBUSTÍVEL (LITROS)'] > 1.0]
  df = df.loc[(df['PASSAGEIROS PAGOS'] + df['PASSAGEIROS GRÁTIS']) > 1.0]

  df = remove_outliers_by_col(df, 'COMBUSTÍVEL (LITROS)')
  df = remove_outliers_by_col(df, 'HORAS VOADAS')
  df = remove_outliers_by_col(df, 'PASSAGEIROS PAGOS')
  df = remove_outliers_by_col(df, 'PASSAGEIROS GRÁTIS')
  
  return df

def get_descritive_values (df: DataFrame, col:str):
  mean = df[col].mean()
  median = df[col].median()
  mode = df[col].mode()

  variance = df[col].var()

  standard_deviation = df[col].std()
  var_coef = (standard_deviation / mean) / 100

  quartile25 = df[col].quantile(0.25)
  quartile50 = df[col].quantile(0.5)
  quartile75 = df[col].quantile(0.75)

  max = df[col].max()
  min = df[col].min()

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
  return corr