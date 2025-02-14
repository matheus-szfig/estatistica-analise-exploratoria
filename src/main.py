from dataset import get_data_frame
from pipeline import pipeline_pre_process, get_descritive_values, get_correlation
from plot import plot_scatter_hour_vs_litros, plot_box_psg, plot_top_states, plot_scatter_psg_luggage

def main():
    df = get_data_frame()
    df = pipeline_pre_process(df)

    get_descritive_values(df, 'PASSAGEIROS PAGOS')
    get_descritive_values(df, 'PASSAGEIROS GRÁTIS')
    get_descritive_values(df, 'COMBUSTÍVEL (LITROS)')
    get_descritive_values(df, 'HORAS VOADAS')

    get_correlation(df, 'PASSAGEIROS GRÁTIS', 'PASSAGEIROS PAGOS')
    get_correlation(df, 'COMBUSTÍVEL (LITROS)', 'HORAS VOADAS')

    plot_box_psg(df)
    plot_scatter_psg_luggage(df)
    plot_scatter_hour_vs_litros(df)
    plot_top_states(df)
    

if __name__ == "__main__":
    main()
