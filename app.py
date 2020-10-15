import os
from dotenv import load_dotenv

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State


from cubeviz.charts import plot_solve_time_series
from cubeviz.io import parse_upload_content
from cubeviz.etl import process_timiks_data

load_dotenv()

window_sizes = [25, 50, 100]

app = dash.Dash(__name__)
server = app.server

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
    ],
)


@app.callback(
    Output("div-solve-time-series", "children"),
    [Input("upload-data", "contents")],
    [State("upload-data", "filename"), State("upload-data", "last_modified")],
)
def update_output(content, name, date):
    if content is not None:
        df_raw = parse_upload_content(content, name, date)
        # TODO: add another layer to not process timiks but process some standard form
        df_clean = process_timiks_data(df_raw, window_sizes)
        df_mins = df_clean[df_clean["is_diff"] == True]
        fig = plot_solve_time_series(df_clean, df_mins, window_sizes)
        return dcc.Graph("main-graph", figure=fig, className="big-plot")


if __name__ == "__main__":
    environment = os.getenv("ENVIRONMENT")
    if environment == "local":
        app.run_server(host="127.0.0.1", port=8000, debug=True)
    else:
        app.run_server()
