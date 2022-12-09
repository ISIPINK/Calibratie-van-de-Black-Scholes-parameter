import pandas as pd
from plots import load_data
from implied_volatility import find_vol
from datetime import date

def getT(maturity):
    date_of_Data = date(2022,12,3)
    year,month,day = [int(x) for x in maturity.split("-")]
    maturity_date = date(year,month,day)
    return  (maturity_date- date_of_Data).days/365


def add_estimated_rS_data(df_data, df_rS):
    rentes = [float(df_rS[df_rS["maturity"] == str(mat)]["rente"]) for mat in df_data["maturity"]  ]
    begin_prijzen = [float(df_rS[df_rS["maturity"] == str(mat)]["begin_prijs"]) for mat in df_data["maturity"]  ]
    df_data["rente"]= rentes
    df_data["begin_prijs"]= begin_prijzen
    return df_data


def calc_implied_vol(df_data, df_rS ):
    # ok dat is heel onleesbaar maar moet enkel 1 keer runnen ...
    vols =[find_vol(
            target_value=row[2],
            S = row[7],
            K = row[1],
            T = getT(row[0]),
            r = row[6])
        for _,row in df_data.iterrows()
        ]
    df_data["implied_volatility"]= vols
    return df_data


if __name__ == "__main__":
    df_data, df_rS =  load_data()
    df_data = add_estimated_rS_data(df_data, df_rS )
    df_data = calc_implied_vol(df_data,df_rS)
    df_data.to_csv('../data/options_spx_data_complete.csv')
