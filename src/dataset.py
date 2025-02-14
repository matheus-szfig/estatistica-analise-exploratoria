import kagglehub
from pandas import DataFrame, read_csv
import pandas as pd
from os import path, listdir, getcwd

def get_data_frame() -> DataFrame:
    # Monta o caminho completo para o arquivo 'dados_aereos.csv'
    # usando a pasta atual de trabalho e a subpasta 'datasets'
    dataset_path = path.join(getcwd(), 'datasets', 'dados_aereos.csv')
    
    # Normaliza o caminho para o formato do sistema operacional em uso
    dataset_path = path.normpath(dataset_path)
    
    # Lê o arquivo CSV como um DataFrame
    df = read_csv(dataset_path, sep=';', encoding='utf-8')
    
    print("Columns:")
    for col in df.columns.tolist():
        print(col)
    
    return df