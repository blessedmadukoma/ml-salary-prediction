import pandas as pd


def header_manipulation(df: pd.DataFrame):
    # put all columns into lowercase, replace spaces with underscores
    df.columns = df.columns.str.lower().str.replace(" ", "_")

    return df.columns
