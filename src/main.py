from dataset import get_data_frame
from pipeline import run_pipeline
from plot import run_plot

def main():
    df = get_data_frame()
    df = run_pipeline(df)
    df = run_plot(df)

if __name__ == "__main__":
    main()
