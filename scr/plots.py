from plotnine import *
import pandas as pd
from datetime import date
from math import log

date_of_Data = date(2022,12,3)

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
        year,month,day = [int(x) for x in maturity.split("-")]
        maturity_date = date(year,month,day)
        T = (maturity_date - date_of_Data).days/365
        PC5 = group["put_call"].iloc[5]
        PC6 = group["put_call"].iloc[6]
        exprt = (PC6-PC5)/(group["strike"].iloc[6]-group["strike"].iloc[5])
        print(exprt)
        r = -log(-exprt)/T
        #print(r)
        """"
        K = group["put_call"][0]+ group["strike"][0]*exprt
        print(r,K)
        """
    

if __name__ == "__main__":
    df = load_data()
    calc_r_S(df)
    #plot_prijs_strike(df)
    plot_put_call(df)
