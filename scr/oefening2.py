import pandas as pd
from datetime import date
from math import log

def calc_r_S(df):
    date_of_Data = date(2022,12,3)
    df["put_call"]= df["prijs_call"] - df["prijs_put"]
    data_rS=[]

    for maturity, group in  df[["maturity", "strike","put_call"]].groupby("maturity"):
        year,month,day = [int(x) for x in maturity.split("-")]
        maturity_date = date(year,month,day)
        T = (maturity_date - date_of_Data).days/365
         
        put_call_first = group["put_call"].iloc[0]
        put_call_last = group["put_call"].iloc[-1]
        exprt = (put_call_last-put_call_first)/(group["strike"].iloc[-1]-group["strike"].iloc[0])

        r = -log(-exprt)/T
        S = group["put_call"].iloc[0]+ group["strike"].iloc[0]*exprt
        S = -S 
        data_rS.append((maturity_date,T,r,S))

    cols = ["maturity","looptijd_jaar","rente","begin_prijs"]
    return  pd.DataFrame(data_rS, columns= cols)

if __name__ == "__main__":
    file = "../data/options_spx_data.csv"
    df =  pd.read_csv(file,index_col = 0)
    df_rS = calc_r_S(df)
    df_rS.to_csv("../data/options_spx_estimated_rS.csv")

