from plotnine import *
import pandas as pd
from datetime import date
from math import log

def load_data():
    file_data = "../data/options_spx_data_complete.csv"
    file_rS = "../data/options_spx_estimated_rS.csv"
    file_spx = "../data/INDEX_US_S&P US_SPX_fixed.csv"
    file_real_vol = "../data/spx_real_vol.csv"
    df_data = pd.read_csv(file_data,index_col = 0)
    df_rS = pd.read_csv(file_rS, index_col = 0)
    df_spx = pd.read_csv(file_spx)
    df_real_vol = pd.read_csv(file_real_vol)
    return  df_data, df_rS, df_spx , df_real_vol

def plot_prijs_strike(df):
    plot = (ggplot(df, aes(color = "maturity")) 
            + geom_point(aes(x="strike", y ="prijs_call"),shape = ".")
            + geom_point(aes(x="strike", y ="prijs_put"), shape = ",")
            + ggtitle("option_prices vs strikes"))
    plot.save("../plots/prijs_vs_strike.png",dpi = 200)
    print(plot)

def plot_put_call(df):
    df["put_call"]= df["prijs_call"] - df["prijs_put"]
    plot = (ggplot(df, aes(color= "maturity"))
        + geom_point(aes(x = "strike", y = "put_call"))
        + ggtitle("put_call_parity"))
    plot.save("../plots/put_call_parity.png",dpi = 200)
    print(plot)

def plot_estimated_r(df):
    plot = (ggplot(df, aes(x ="looptijd_jaar", y = "rente"))
            + geom_point(aes(size = "begin_prijs"))
            + geom_text(aes(label = "maturity"), nudge_y = 0.02)
            + ggtitle("estimated_rS"))
    plot.save("../plots/estimated_rS.png",dpi = 200)
    print(plot)

def plot_implied_vol(df_data):
    spx_02_22 = 4040.17
    plot = (ggplot(df_data, aes(x ="strike", y = "implied_volatility"))
            + geom_point(aes(color = "maturity", size = "foutenvlag_call" ))
            + geom_vline(aes(xintercept = spx_02_22))
            + ggtitle("implied_vol vs strike"))
    plot.save("../plots/implied_volatility.png",dpi = 200)
    print(plot)

def plot_spx(df_spx):
    plot = (ggplot(df_spx, aes(x ="Time", y = "Open"))
            + geom_line()
            + ggtitle("spx last half year"))
    plot.save("../plots/spx_prijs.png",dpi = 200)
    print(plot)
    
def plot_real_vol(df_real_vol):
    plot = (ggplot(df_real_vol, aes(x ="backwardtime", y = "real_vol"))
            + geom_point()
            + geom_text(aes(label = "backwardtime"), nudge_y = 0.05)
            + ggtitle("real_vol"))
    plot.save("../plots/real_vol.png",dpi = 200)
    print(plot)


def alle_plots():
    df_data, df_rS, df_spx, df_real_vol = load_data()
    plot_prijs_strike(df_data)
    plot_put_call(df_data)
    plot_estimated_r(df_rS)
    plot_implied_vol(df_data)
    plot_spx(df_spx)
    plot_real_vol(df_real_vol)

if __name__ == "__main__":
    alle_plots()
