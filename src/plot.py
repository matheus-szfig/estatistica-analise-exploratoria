import pandas as pd
import matplotlib.pyplot as plt
from pandas import DataFrame

def plot_scatter_hour_vs_litros(df: DataFrame):
    
    plt.figure(figsize=(16, 9))
    
    plt.scatter(x=df['COMBUSTÍVEL (LITROS)'], y=df['HORAS VOADAS'], alpha=0.1)
    
    plt.xlabel('COMBUSTÍVEL (LITROS)')
    plt.ylabel('HORAS VOADAS')
    
    plt.show()


def plot_box_psg(df: DataFrame):

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


def plot_top_states(df: DataFrame, top_n=10):
    
    # Seleciona apenas UF de origem e UF de destino
    df_states = df[['AEROPORTO DE ORIGEM (UF)', 'AEROPORTO DE DESTINO (UF)']]
    
    # "Empilha" as duas colunas em uma só (coluna 'UF'), unindo origem e destino
    df_melted = df_states.melt(value_name='UF')
    
    # Conta quantas vezes cada UF aparece
    uf_counts = df_melted['UF'].value_counts()
    
    # Seleciona os top_n estados mais movimentados
    top_ufs = uf_counts.head(top_n)
    
    plt.figure(figsize=(10, 6))
    
    top_ufs.plot(kind='bar', color='royalblue')
    
    plt.title(f'Top {top_n} Estados (UF) Mais Movimentados')
    plt.xlabel('Estado (UF)')
    plt.ylabel('Total de Voos (Chegadas + Partidas)')
    plt.xticks(rotation=45)
    
    plt.tight_layout()
    plt.show()
