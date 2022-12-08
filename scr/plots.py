from plotnine import *
import pandas as pd
from datetime import date
from math import log

def load_data():
    file_data = "../data/options_spx_data.csv"
    file_rS = "../data/options_spx_estimated_rS.csv"
    df_data = pd.read_csv(file_data,index_col = 0)
    df_rS = pd.read_csv(file_rS, index_col = 0)
    return  df_data, df_rS

def plot_prijs_strike(df):
    print(ggplot(df, aes(color = "maturity")) 
            + geom_point(aes(x="strike", y ="prijs_call"),shape = ".")
            + geom_point(aes(x="strike", y ="prijs_put"), shape = ","))

def plot_put_call(df):
    df["put_call"]= df["prijs_call"] - df["prijs_put"]
    print(ggplot(df, aes(color= "maturity"))
        + geom_point(aes(x = "strike", y = "put_call")))

def plot_estimated_r(df):
    print(ggplot(df, aes(x ="looptijd_jaar", y = "rente"))
            + geom_point(aes(size = "begin_prijs"))
            + geom_text(aes(label = "maturity"), nudge_y = 0.02))

def alle_plots():
    df_data, df_rS = load_data()
    plot_prijs_strike(df_data)
    plot_put_call(df_data)
    plot_estimated_r(df_rS)

if __name__ == "__main__":
    df_data, df_rS = load_data()
    plot_estimated_r(df_rS)
