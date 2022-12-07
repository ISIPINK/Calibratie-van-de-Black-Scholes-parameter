from plotnine import *
import pandas as pd
from datetime import date


def load_data():
    dates = [
        date(2022,12,7),
        date(2022,12,14),
        date(2023,1,3),
        date(2023,2,17)
        ]
    files = [
        "../data/$spx-options-exp-2022-12-07-weekly-near-the-money-stacked-12-03-2022.csv",
        "../data/$spx-options-exp-2022-12-14-weekly-near-the-money-stacked-12-03-2022.csv",
        "../data/$spx-options-exp-2023-01-03-weekly-near-the-money-stacked-12-03-2022.csv",
        "../data/$spx-options-exp-2023-02-17-monthly-near-the-money-stacked-12-03-2022.csv"
           ]
    # laatste rij is nutteloos
    dfs = {date : pd.read_csv(file)[0:-1] for file, date in zip(files, dates) }
    return dfs

def clean_data(dfs:"komt uit load_data")->"clean df":
    data_calls = []
    prijzen_puts = []
    foutenvlag_puts = []

    for date, df in dfs.items():
        for x in df.iterrows():
            if x[1][11] == "Call":
                data_calls.append((date, x[1][0], x[1][3], x[1][4]-x[1][3]))
            else:
                prijzen_puts.append(x[1][3])
                foutenvlag_puts.append(x[1][4]-x[1][3])


    cols = ["maturity", "strike", "prijs_call", "foutenvlag_call"]
    data_df = pd.DataFrame(data_calls, columns=cols)
    data_df["strike"] = pd.to_numeric(data_df["strike"].apply(lambda x : x.split(".")[0].replace(",","")))
    data_df["prijs_put"] = prijzen_puts
    data_df["foutenvlag_put"] = foutenvlag_puts
    return data_df

if __name__ == "__main__":
    dfs = load_data()
    df = clean_data(dfs)
    df.to_csv('../data/options_spx_data.csv')
    

    

