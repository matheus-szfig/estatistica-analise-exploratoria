from dataset import get_data_frame
from pipeline import pipeline_pre_process, get_descritive_values, get_correlation
from plot import plot_scatter_hour_vs_litros, plot_box_psg, plot_top_airports

def main():
    df = get_data_frame()
    df = pipeline_pre_process(df)

    desc_psg_free = get_descritive_values(df, 'PASSAGEIROS PAGOS')
    desc_psg_paid = get_descritive_values(df, 'PASSAGEIROS GRÁTIS')
    desc_fuel = get_descritive_values(df, 'COMBUSTÍVEL (LITROS)')
    desc_hours = get_descritive_values(df, 'HORAS VOADAS')

    corr_paid_free = get_correlation(df, 'PASSAGEIROS GRÁTIS', 'PASSAGEIROS PAGOS')
    corr_fuel_hour = get_correlation(df, 'COMBUSTÍVEL (LITROS)', 'HORAS VOADAS')

    plot_box_psg(df)
    plot_scatter_hour_vs_litros(df)
    plot_top_airports(df)
    

if __name__ == "__main__":
    main()
