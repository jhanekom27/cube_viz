from cubeviz.server import app
from dash.dependencies import Input, Output, State
import pandas as pd
from cubeviz.io import parse_upload_content
from cubeviz.etl import process_timiks_data
from cubeviz.charts import plot_solve_time_series
import dash_core_components as dcc

from cubeviz.config import cubeviz_config


@app.callback(
    Output("div-solve-time-series", "children"),
    [Input("upload-data", "contents")],
    [State("upload-data", "filename"), State("upload-data", "last_modified")],
)
def update_output(content, name, date):
    window_sizes = cubeviz_config.window_sizes
    if content is not None:
        df_raw = parse_upload_content(content, name, date)
        # TODO: add another layer to not process timiks but process some standard form
        df_clean = process_timiks_data(df_raw, window_sizes)
        df_mins = df_clean[df_clean["is_diff"] == True]
        fig = plot_solve_time_series(df_clean, df_mins, window_sizes)
        return dcc.Graph("main-graph", figure=fig, className="big-plot")
    else:
        df_raw = pd.read_csv("data/sample.csv")
        df_clean = process_timiks_data(df_raw, window_sizes)
        df_mins = df_clean[df_clean["is_diff"] == True]
        fig = plot_solve_time_series(df_clean, df_mins, window_sizes)
        return dcc.Graph("main-graph", figure=fig, className="big-plot")
