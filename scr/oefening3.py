import pandas as pd
from plots import load_data
from implied_volatility import find_vol

def getT(maturity):
    date_of_Data = date(2022,12,3)

    return  (maturity- date_of_Data).days/365


def calc_implied_vol():
    df_data, df_rS =  load_data()
    spx_02_22 = 4040.17


'''
    vol  = [find_vol(
        target_value=row[2],
        S = df_rS[row],
        K = strike,
        T =,
        r = rente
        )
        for _,row in df_data.iterrows() ]
'''

if __name__ == "__main__":
    calc_implied_vol()
    
