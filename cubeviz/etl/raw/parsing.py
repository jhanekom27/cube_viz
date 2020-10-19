import base64
import io
import pandas as pd
import dash_html_components as html
from pandas import DataFrame
from typing import List

from cubeviz.config import cubeviz_config
from cubeviz.models import TimiksData, CVBase, CVEnhanced


# TODO: Refactor this to the right files
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


def get_relevant_windows(df: DataFrame, window_sizes: List[int]) -> List[int]:
    df_count = len(df)
    return [window for window in window_sizes if window <= df_count]


def enhance_base_data(df: CVBase, window_sizes: List[int]) -> CVEnhanced:
    window_sizes = get_relevant_windows(df, window_sizes)
    df["solve_num"] = df.index

    df["best_time"] = df["time_sec"].cummin()
    df["best_time_is_diff"] = df["best_time"] != df["best_time"].shift()
    df["best_time"] = df[df["best_time_is_diff"]]["best_time"]

    for window_size in window_sizes:
        df[f"Ao{window_size}"] = df.time_sec.rolling(window=window_size).mean()

    return df


def parse_upload_content(contents: str, filename: str, date) -> CVEnhanced:
    content_type, content_string = contents.split(",")
    window_sizes = cubeviz_config.window_sizes

    decoded = base64.b64decode(content_string)
    try:
        if "csv" in filename:
            # Assume that the user uploaded a CSV file
            df = pd.read_csv(io.StringIO(decoded.decode("utf-8")))
        elif "xls" in filename:
            # Assume that the user uploaded an excel file
            df = pd.read_excel(io.BytesIO(decoded))

        data_format = get_data_source_format(df)

        if data_format == UploadFormats.TIMIKS:
            df = parse_timiks_to_base(df)
        else:
            raise Exception("Uh oh!")

        df = enhance_base_data(df, window_sizes)

    except Exception as e:
        print(e)
        return html.Div(["There was an error processing this file."])

    return df
