import pandas as pd


def process_timiks_data(df, window_sizes):
    df["num"] = df.index

    df["date"] = pd.to_datetime(df["date"])
    df["time"] = df["ms"] / 1000

    df["best_time"] = df["time"].cummin()
    df["is_diff"] = df["best_time"] != df["best_time"].shift()
    df["best_time"] = df[df["is_diff"]]["best_time"]

    for window_size in window_sizes:
        df[f"{window_size}_avg"] = df["time"].rolling(window=window_size).mean()
        df[f"{window_size}_std"] = df["time"].rolling(window=window_size).std()

    return df
