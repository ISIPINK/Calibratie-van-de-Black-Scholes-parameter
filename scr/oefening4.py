import pandas as pd
from math import sqrt,log
from datetime import date
import numpy as np


def getT(maturity):
    date_of_Data = date(2022,12,3)
    month,day,year = [int(x) for x in maturity.split("/")]
    maturity_date = date(year,month,day)
    return  (maturity_date- date_of_Data).days/365

def proces_price_format(price):
    thous, un = price.split(",")
    i , d = un.split(".")
    return float(thous)*1000 + float(i) + float(d)*0.01

def proces_spx(df_spx):
    df_spx["Time"] =[getT(date) for date in df_spx["Date"]]
    df_spx["Open"] = [proces_price_format(price) for price in df_spx["Open"]]
    return df_spx


def average(l:list):
    if len(l)==0:
        raise Exception("len(l)==0")
    return sum(l)/len(l)
    

def calc_realized_vol(df_spx):
    prices = df_spx["Open"]
    backwardtimes = [3,7,14,30,60,90,180]
    hist_vols = []

    for backwardtime in backwardtimes:
        prices_backward = prices[-backwardtime:]
        returns = [log(P_i)- log(P_i1) 
                for P_i,P_i1 in zip(prices_backward[1:], prices_backward[:-1])]
        hist_vols.append(sqrt(sum(r**2 for r in returns))*252/backwardtime) 
    
    data= [[-b for b in backwardtimes], hist_vols]
    cols = ["backwardtime","real_vol"]

    df_real_vol= pd.DataFrame(data).transpose()
    df_real_vol.columns = cols
    return df_real_vol

    

if __name__ == "__main__":
    file_spx = "../data/INDEX_US_S&P US_SPX.csv"
    df_spx = pd.read_csv(file_spx)
    df_spx = proces_spx(df_spx)
    df_real_vol = calc_realized_vol(df_spx)
    df_spx.to_csv("../data/INDEX_US_S&P US_SPX_fixed.csv")
    df_real_vol.to_csv("../data/spx_real_vol.csv")
    
