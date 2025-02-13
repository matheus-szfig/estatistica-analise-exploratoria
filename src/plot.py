import matplotlib.pyplot as plt
from pandas import DataFrame

def plot_box_by_region (df: DataFrame):

  upper_out = df["Valor de Venda"].quantile(0.99)
  lower_out = df["Valor de Venda"].quantile(0.01)

  outliers1 = df.loc[df["Valor de Venda"] >= upper_out]
  outliers2 = df.loc[df["Valor de Venda"] <= lower_out]
  
  total_out = len(outliers1) + len(outliers2)
  print(total_out / len(df["Valor de Venda"]))
  # Exemplo: boxplot de Survival_Rate agrupado por country
  df.boxplot(
    figsize=(10, 9),
    column='Valor de Venda', by='Regiao',
    patch_artist=True,
    medianprops=dict(color="orange"),
    boxprops=dict(facecolor="lightblue", color="black"),
    showfliers=False,
    grid=False
  )

  plt.grid(visible=True, color="black", alpha=0.05)

  plt.title("Valor de Venda por Região 2024.2")
  plt.suptitle("")  # Remove o título automático do método groupby boxplot
  plt.xlabel("Região")
  plt.ylabel("Valor de Venda (R$)")
  plt.xticks(rotation=45)  # Rotaciona labels se necessário
  plt.tight_layout()
  plt.show()

def plot_scatter_date_price (df: DataFrame):

  plt.figure(figsize=(16, 9))
  plt.scatter(x=df['Data da Coleta'], y=df['Valor de Venda'], alpha=0.01)
  plt.show()
