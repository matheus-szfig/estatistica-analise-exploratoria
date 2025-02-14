import kagglehub
from pandas import DataFrame, read_csv
import pandas as pd
from os import path, listdir, getcwd

def get_data_frame () -> DataFrame:
  dataset_path = path.join(getcwd(), 'datasets/dados_aereos.csv')
  dataset_path = path.normpath(dataset_path)

  df = read_csv(dataset_path, sep=';', encoding='utf-8')
  
  # df.rename(columns={ 'Estado - Sigla': 'Estado', 'Regiao - Sigla': 'Regiao' }, inplace=True)
  
  # # Dropar a coluna 'Valor de Compra' pois ela está toda em branco
  # df.drop('Valor de Compra', axis=1, inplace=True)

  # # Processar os dados e dar replace em valores
  # df.replace({
  #   'Valor de Venda': { ',': '.' },
  #   'Regiao': {
  #       '^N$':'Norte',
  #       '^NE$': 'Nordeste',
  #       '^CO$':'Centro-Oeste',
  #       '^SE$': 'Sudeste',
  #       '^S$': 'Sul'
  #   }
  # }, regex=True, inplace=True)

  # # Transformar a coluna 'Valor de Venda' em numérico
  # df['Valor de Venda'] = pd.to_numeric(df['Valor de Venda'])
  # df['Data da Coleta'] = pd.to_datetime(df['Data da Coleta'], format='%d/%m/%Y')
  # df.sort_values(by=['Data da Coleta'],inplace=True)

  return df