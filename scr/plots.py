from plotnine import *
import pandas as pd
from datetime import date


def load_data():
    file = "../data/options_spx_data.csv"
    return pd.read_csv(file,index_col = 0)
    

def plot_prijs_strike(df):
    """
    plot de prijzen vs strike
    """
    print(ggplot(df, aes(color = "maturity")) 
            + geom_point(aes(x="strike", y ="prijs_call"),shape = ".")
            + geom_point(aes(x="strike", y ="prijs_put"), shape = ","))

def plot_put_call(df):
    df["put_call"]= df["prijs_call"] - df["prijs_put"]
    print(ggplot(df, aes(color= "maturity"))
        + geom_point(aes(x = "strike", y = "put_call")))


def calc_r_S(df):
    df["put_call"]= df["prijs_call"] - df["prijs_put"]
    for maturity, group in  df[["maturity", "strike","put_call"]].groupby("maturity"):
        print(group)

    

if __name__ == "__main__":
    df = load_data()
    calc_r_S(df)
    #plot_prijs_strike(df)
    #plot_put_call(df)
