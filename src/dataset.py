import kagglehub
from pandas import DataFrame, read_csv
from os import path

def get_data_frame () -> DataFrame:
  dataset_path = kagglehub.dataset_download("ankushpanday1/liver-cancer-predictions")
  dataset_path = path.join(dataset_path, "liver_cancer_prediction.csv")
  return read_csv(dataset_path)