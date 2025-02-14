import matplotlib.pyplot as plt
from pandas import DataFrame

# def plot_box_by_region (df: DataFrame):

  # upper_out = df["Valor de Venda"].quantile(0.99)
  # lower_out = df["Valor de Venda"].quantile(0.01)

  # outliers1 = df.loc[df["Valor de Venda"] >= upper_out]
  # outliers2 = df.loc[df["Valor de Venda"] <= lower_out]
  
  # total_out = len(outliers1) + len(outliers2)
  # print(total_out / len(df["Valor de Venda"]))
  # # Exemplo: boxplot de Survival_Rate agrupado por country
  # df.boxplot(
  #   figsize=(10, 9),
  #   column='Valor de Venda', by='Regiao',
  #   patch_artist=True,
  #   medianprops=dict(color="orange"),
  #   boxprops=dict(facecolor="lightblue", color="black"),
  #   showfliers=False,
  #   grid=False
  # )

  # plt.grid(visible=True, color="black", alpha=0.05)

  # plt.title("Valor de Venda por Região 2024.2")
  # plt.suptitle("")  # Remove o título automático do método groupby boxplot
  # plt.xlabel("Região")
  # plt.ylabel("Valor de Venda (R$)")
  # plt.xticks(rotation=45)  # Rotaciona labels se necessário
  # plt.tight_layout()
  # plt.show()

def plot_scatter_hour_vs_litros (df: DataFrame):

  plt.figure(figsize=(16, 9))
  plt.scatter(x=df['COMBUSTÍVEL (LITROS)'], y=df['HORAS VOADAS'], alpha=0.1)
  plt.xlabel('COMBUSTÍVEL (LITROS)')
  plt.ylabel('HORAS VOADAS')
  plt.show()

def plot_box_psg (df: DataFrame):

  plt.figure(figsize=(6, 9))
  df.boxplot(
    column=['PASSAGEIROS PAGOS'],
    medianprops=dict(color="green"),
    boxprops=dict(facecolor="lightblue", color="black"),
    patch_artist=True,
    showfliers=False
  )
  plt.grid(alpha=0.2)
  plt.show()

  plt.figure(figsize=(6, 9))
  df.boxplot(
    column=['PASSAGEIROS GRÁTIS'],
    medianprops=dict(color="green"),
    boxprops=dict(facecolor="lightblue", color="black"),
    patch_artist=True,
    showfliers=False
  )
  plt.grid(alpha=0.2)
  plt.show()

def plot_top_airports(df, top_n=10):
  """
  Gera um gráfico de barras com os N aeroportos (siglas) mais movimentados,
  considerando tanto voos de origem quanto de destino.
  
  Parâmetros:
      df (pd.DataFrame): DataFrame que contém as colunas 
          'AEROPORTO DE ORIGEM (UF)' e 'AEROPORTO DE DESTINO (UF)'
      top_n (int): Número de aeroportos que serão exibidos no gráfico
  """
  # 1. Seleciona apenas as duas colunas que nos interessam
  df_temp = df[['AEROPORTO DE ORIGEM (UF)', 'AEROPORTO DE DESTINO (UF)']]
  
  # 2. Converte as duas colunas em uma única coluna "SIGLA" (empilhamento)
  df_melted = df_temp.melt(value_name='NOME')
  
  # 3. Conta quantas vezes cada sigla aparece (voos chegando ou saindo)
  airport_counts = df_melted['NOME'].value_counts()
  
  # 4. Pega os top N aeroportos mais movimentados
  top_airports = airport_counts.head(top_n)
  
  # 5. Plota o gráfico de barras
  plt.figure(figsize=(10, 6))
  top_airports.plot(kind='bar', color='royalblue')
  
  plt.title(f'Top {top_n} Estados Mais Movimentados')
  plt.xlabel('Estado')
  plt.ylabel('Total de Voos (Chegadas + Partidas)')
  plt.xticks(rotation=45)
  plt.tight_layout()
  plt.show()