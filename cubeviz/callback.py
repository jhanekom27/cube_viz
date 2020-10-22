from dash.dependencies import Input, Output, State
import pandas as pd

from cubeviz.server import app
from cubeviz.charts import get_solve_times_graph, get_all_frequency_heatmaps
from cubeviz.etl import (
    enhance_base_data,
    parse_timiks_to_base,
    parse_upload_content,
    group_enhanced_by_day,
)
from cubeviz.layout import get_title_value
from cubeviz.config import cubeviz_config


@app.callback(
    [
        Output("h2-uploaded-file-name", "children"),
        Output("div-solve-time-series", "children"),
        Output("div-frequency-heatmaps", "children"),
    ],
    [Input("upload-data", "contents")],
    [State("upload-data", "filename"), State("upload-data", "last_modified")],
)
def update_output(content, name, date):
    window_sizes = cubeviz_config.window_sizes

    if content is not None:
        df_base = parse_upload_content(content, name, date)
    else:
        name = "sample.csv"
        data_path = cubeviz_config.default_data_path
        df_timiks_raw = pd.read_csv(data_path)
        df_base = parse_timiks_to_base(df_timiks_raw)

    df_cv_enhanced = enhance_base_data(df_base, window_sizes)
    df_grouped_daily = group_enhanced_by_day(df_cv_enhanced)

    file_name_display = get_title_value(name)
    solve_times_graph = get_solve_times_graph(df_cv_enhanced, window_sizes)
    div_frequency_heatmaps = get_all_frequency_heatmaps(df_grouped_daily)

    return (file_name_display, solve_times_graph, div_frequency_heatmaps)
