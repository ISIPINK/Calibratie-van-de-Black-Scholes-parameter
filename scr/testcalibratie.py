from calibratie import load_data

def testload_data():
    dfs = load_data()
    for date,df in dfs.items():
        print(f"option prices with maturity on: {date}")
        print(df.head())

def alleTesten():
    testload_data()

if __name__ == "__main__":
    testload_data()
    

    
