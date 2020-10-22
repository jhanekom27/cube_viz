from typing import List
import pandas as pd

from cubeviz.models import CVBase, CVEnhanced, CVGroupedDaily
from cubeviz.etl.helpers import get_relevant_windows


def enhance_base_data(df: CVBase, window_sizes: List[int]) -> CVEnhanced:
    window_sizes = get_relevant_windows(df, window_sizes)
    df["solve_num"] = df.index

    df["best_time"] = df.time_sec.cummin()
    df["best_time_is_diff"] = df.best_time != df.best_time.shift()
    df["best_time"] = df[df.best_time_is_diff].best_time
    df["solve_date"] = df.solve_date_time.dt.date

    for window_size in window_sizes:
        df[f"Ao{window_size}"] = df.time_sec.rolling(window=window_size).mean()

    return df


def group_enhanced_by_day(df_cv_enhanced: CVEnhanced) -> CVGroupedDaily:
    df_grouped_daily = (
        df_cv_enhanced.groupby("solve_date")
        .agg(
            num_solves=("time_sec", "count"),
            time_sec_mean=("time_sec", "mean"),
            time_sec_std=("time_sec", "std"),
        )
        .reset_index()
    )

    # Add date features for heatmap
    df_grouped_daily["solve_date"] = pd.to_datetime(df_grouped_daily["solve_date"])
    df_grouped_daily["year"] = df_grouped_daily["solve_date"].dt.year
    df_grouped_daily["month"] = df_grouped_daily["solve_date"].dt.month
    df_grouped_daily["day"] = df_grouped_daily["solve_date"].dt.day

    return df_grouped_daily
