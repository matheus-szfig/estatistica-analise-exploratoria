import matplotlib.pyplot as plt
from pandas import DataFrame

def run_plot (df: DataFrame):
  fig = plt.figure(figsize=(10, 7))
  ax = fig.add_subplot(111)
  ax.set_yticklabels(['Age', 'Survival_Rate', 'Mortality_Rate'])
  plt.boxplot(data=df, x=df[['Age', 'Survival_Rate', 'Mortality_Rate']], label=['Age', 'Survival_Rate', 'Mortality_Rate'], orientation="horizontal")

  plt.show()

  return df
