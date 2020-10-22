from typing import List
from pandas import DataFrame


def get_relevant_windows(df: DataFrame, window_sizes: List[int]) -> List[int]:
    df_count = len(df)
    return [window for window in window_sizes if window <= df_count]
