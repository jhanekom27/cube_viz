from dash.dependencies import Input, Output, State
import pandas as pd
import dash_core_components as dcc

from cubeviz.server import app
from cubeviz.charts import plot_solve_time_series
from cubeviz.etl import enhance_base_data, parse_timiks_to_base, parse_upload_content
from cubeviz.config import cubeviz_config


# TODO: change this to update multiple outputs
@app.callback(
    Output("div-solve-time-series", "children"),
    [Input("upload-data", "contents")],
    [State("upload-data", "filename"), State("upload-data", "last_modified")],
)
def update_output(content, name, date):
    window_sizes = cubeviz_config.window_sizes

    if content is not None:
        df_base = parse_upload_content(content, name, date)
    else:
        data_path = cubeviz_config.default_data_path
        df_timiks_raw = pd.read_csv(data_path)
        df_base = parse_timiks_to_base(df_timiks_raw)

    df_cv_enhanced = enhance_base_data(df_base, window_sizes)
    fig = plot_solve_time_series(df_cv_enhanced, window_sizes)
    return dcc.Graph("main-graph", figure=fig, className="big-plot")
