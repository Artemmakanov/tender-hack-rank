from tqdm import tqdm

import pandas as pd

def bin(pos):
    if pos == 1:
        return 10

    elif pos == 2:
        return 9

    elif pos == 3:
        return 8

    elif pos <= 5:
        return 7

    elif pos <= 10:
        return 6

    elif pos <= 20:
        return 5
    
    elif pos <= 35:
        return 4
    
    elif pos <= 55:
        return 3
    
    elif pos <= 80:
        return 2

    elif pos <= 130:
        return 1

    elif pos <= 200:
        return 0

def split_train_test(df: pd.DataFrame, p: int = 0.8):
    df_train = pd.DataFrame()
    df_test = pd.DataFrame()
    for _, df_group in tqdm(df.groupby(['label', 'queries'])):
        r, _ = df_group.shape
        df_group = df_group.sample(frac=1.)
        r = int(p * r)
        df_train = pd.concat([df_train, df_group.iloc[:r]])
        df_test = pd.concat([df_test, df_group.iloc[r:]])
    return df_train, df_test