from typing import List, Tuple
from pandas import DataFrame
import pandas as pd

from cubeviz.models import CVBase
from cubeviz.config import cubeviz_config
from cubeviz.etl import parse_timiks_to_base


def get_base_from_sample() -> Tuple[str, CVBase]:
    name = "sample.csv"
    data_path = cubeviz_config.default_data_path
    df_timiks_raw = pd.read_csv(data_path)
    df_base = parse_timiks_to_base(df_timiks_raw)
    return name, df_base


def get_relevant_windows(df: DataFrame, window_sizes: List[int]) -> List[int]:
    df_count = len(df)
    return [window for window in window_sizes if window <= df_count]
