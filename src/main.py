from dataset import get_data_frame
from pipeline import pipeline_run
from plot import plot_scatter_date_price

def main():
    df = get_data_frame()

    mean = df['Valor de Venda'].mean()
    median = df['Valor de Venda'].median()
    mode = df['Valor de Venda'].mode()

    variance = df['Valor de Venda'].var()

    standard_deviation = df['Valor de Venda'].std()
    var_coef = (standard_deviation / mean) / 100

    quartile25 = df['Valor de Venda'].quantile(0.25)
    quartile50 = df['Valor de Venda'].quantile(0.5)
    quartile75 = df['Valor de Venda'].quantile(0.75)

    max = df['Valor de Venda'].max()
    min = df['Valor de Venda'].min()

    corr = df[['Valor de Venda', 'Data da Coleta']].corr(method='pearson').loc['Valor de Venda', 'Data da Coleta']

    # df = pipeline_run(df)
    df = plot_scatter_date_price(df)

if __name__ == "__main__":
    main()
