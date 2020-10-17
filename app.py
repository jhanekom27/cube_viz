import pandas as pd
import os
from dotenv import load_dotenv

import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State


from cubeviz.charts import plot_solve_time_series
from cubeviz.io import parse_upload_content
from cubeviz.etl import process_timiks_data
from cubeviz.server import app
import cubeviz.callback

load_dotenv()

window_sizes = [25, 50, 100]


def get_app(app):
    app.layout = html.Div(
        [
            dcc.Upload(
                id="upload-data",
                children=html.Div(["Drag and Drop or ", html.A("Select Files")]),
                style={
                    "width": "100%",
                    "height": "60px",
                    "lineHeight": "60px",
                    "borderWidth": "1px",
                    "borderStyle": "dashed",
                    "borderRadius": "5px",
                    "textAlign": "center",
                    "margin": "10px",
                },
                multiple=False,
            ),
            html.Div(id="div-solve-time-series"),
            dcc.Dropdown(
                id="dropdown",
                options=[{"label": i, "value": i} for i in ["LA", "NYC", "MTL"]],
                value="LA",
            ),
            html.Div(id="display-value"),
        ],
    )
    return app


def plot_thing(df_clean):
    df_mins = df_clean[df_clean["is_diff"] == True]
    fig = plot_solve_time_series(df_clean, df_mins, window_sizes)
    return fig


if __name__ == "__main__":
    app = get_app(app)

    environment = os.getenv("ENVIRONMENT")
    if environment == "local":
        app.run_server(host="127.0.0.1", port=8000, debug=True)
    else:
        app.run_server()
