from plotnine import *

import pandas as pd
from datetime import date


def load_data():
    dates = [
        date(2022,12,7),
        date(2022,12,14),
        date(2023,1,3),
        date(2022,2,17)
        ]
    files = [
        "../data/$spx-options-exp-2022-12-07-weekly-near-the-money-stacked-12-03-2022.csv",
        "../data/$spx-options-exp-2022-12-14-weekly-near-the-money-stacked-12-03-2022.csv",
        "../data/$spx-options-exp-2023-01-03-weekly-near-the-money-stacked-12-03-2022.csv",
        "../data/$spx-options-exp-2023-02-17-monthly-near-the-money-stacked-12-03-2022.csv"
           ]
    dfs = {date : pd.read_csv(file) for file, date in zip(files, dates) }
    return dfs

def plotStrike(df):
    tmp = (ggplot(df, aes(x="Strike", y ="Midpoint", color = "IV")) + geom_point())
    print(tmp)

def tmp():
    print(dfs[date(2022,12,7)].columns)
    print(dfs[date(2022,12,7)]["Strike"].head())
    for df in dfs.values():
        print(df["Midpoint"].tail())
    print(dfs[date(2022,12,7)].iloc[-1][0:5])

if __name__ == "__main__":
    dfs = load_data()
    df = dfs[date(2022,12,7)][0:-1]
    plotStrike(df)
    

    
