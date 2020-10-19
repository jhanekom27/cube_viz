from typing import List

from cubeviz.models import CVBase, CVEnhanced
from cubeviz.etl.helpers import get_relevant_windows


def enhance_base_data(df: CVBase, window_sizes: List[int]) -> CVEnhanced:
    window_sizes = get_relevant_windows(df, window_sizes)
    df["solve_num"] = df.index

    df["best_time"] = df.time_sec.cummin()
    df["best_time_is_diff"] = df.best_time != df.best_time.shift()
    df["best_time"] = df[df.best_time_is_diff].best_time

    for window_size in window_sizes:
        df[f"Ao{window_size}"] = df.time_sec.rolling(window=window_size).mean()

    return df
