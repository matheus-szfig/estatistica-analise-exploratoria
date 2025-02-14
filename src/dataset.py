import kagglehub
from pandas import DataFrame, read_csv
import pandas as pd
from os import path, listdir, getcwd

def get_data_frame () -> DataFrame:
  dataset_path = path.join(getcwd(), 'datasets/dados_aereos.csv')
  dataset_path = path.normpath(dataset_path)

  df = read_csv(dataset_path, sep=';', encoding='utf-8')

  print("Columns:")
  for col in df.columns.tolist():
    print(col)

  return df