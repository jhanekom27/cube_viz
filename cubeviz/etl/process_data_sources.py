from pandas import DataFrame
import pandas as pd

from cubeviz.models import TimiksData, CVBase


class UploadFormats:
    TIMIKS = "timiks"


def parse_timiks_to_base(df: TimiksData) -> CVBase:
    df["solve_date"] = pd.to_datetime(df.date)
    df["time_sec"] = df.ms / 1000
    return df


def get_data_source_format(df: DataFrame):
    timiks_columns = ["id", "ms", "date", "puzzle"]
    data_columns = df.columns

    if all(col in data_columns for col in timiks_columns):
        return UploadFormats.TIMIKS
    else:
        raise Exception("Uh oh!")
