import os
from dotenv import load_dotenv

load_dotenv()


import base64
import datetime
import io
import pandas as pd

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_table
import plotly.graph_objects as go

window_sizes = [25, 50, 100]
colors = {"background": "#111111"}
theme = "plotly_dark"

# external_stylesheets = ["viz_cube_styles.css"]

# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app = dash.Dash(__name__)

server = app.server

style = ({"backgroundColor": colors["background"]},)
app.layout = html.Div(
    style={"backgroundColor": colors["background"]},
    children=[
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
        html.Div(id="output-data-upload"),
    ],
)


def process_data(df, window_sizes):
    df["num"] = df.index

    df["date"] = pd.to_datetime(df["date"])
    df["time"] = df["ms"] / 1000

    df["best_time"] = df["time"].cummin()
    df["is_diff"] = df["best_time"] != df["best_time"].shift()
    df["best_time"] = df[df["is_diff"]]["best_time"]

    for window_size in window_sizes:
        df[f"{window_size}_avg"] = df["time"].rolling(window=window_size).mean()
        df[f"{window_size}_std"] = df["time"].rolling(window=window_size).std()

    return df


def parse_contents(contents, filename, date):
    content_type, content_string = contents.split(",")

    decoded = base64.b64decode(content_string)
    try:
        if "csv" in filename:
            # Assume that the user uploaded a CSV file
            df = pd.read_csv(io.StringIO(decoded.decode("utf-8")))
        elif "xls" in filename:
            # Assume that the user uploaded an excel file
            df = pd.read_excel(io.BytesIO(decoded))
    except Exception as e:
        print(e)
        return html.Div(["There was an error processing this file."])

    return df

    return html.Div(
        [
            html.H5(filename),
            html.H6(datetime.datetime.fromtimestamp(date)),
            dash_table.DataTable(
                data=df.to_dict("records"),
                columns=[{"name": i, "id": i} for i in df.columns],
            ),
            html.Hr(),  # horizontal line
            # For debugging, display the raw contents provided by the web browser
            html.Div("Raw Content"),
            html.Pre(
                contents[0:200] + "...",
                style={"whiteSpace": "pre-wrap", "wordBreak": "break-all"},
            ),
        ]
    )


def plot_best_times(df, df_mins, window_sizes):
    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=df["num"],
            y=df["time"],
            mode="lines",
            name="Everything",
            line={"color": "white"},
        )
    )

    for window_size in window_sizes:
        fig.add_trace(
            go.Scatter(
                x=df["num"],
                y=df[f"{window_size}_avg"],
                mode="lines",
                name=f"{window_size} avg",
                # line={"color": "white"},
            )
        )

    fig.add_trace(
        go.Scatter(
            x=df_mins["num"],
            y=df_mins["best_time"],
            mode="lines+markers",
            # mode="lines",
            name="Best",
            line={"dash": "dash", "color": "yellow"},
            marker={"size": 8},
        )
    )

    fig.update_layout(
        template=theme,
        xaxis_title="Solves",
        yaxis_title="Time (s)",
        # title=f"Jurgen's solves as at: {today}",
    )

    return fig


@app.callback(
    Output("output-data-upload", "children"),
    [Input("upload-data", "contents")],
    [State("upload-data", "filename"), State("upload-data", "last_modified")],
)
def update_output(content, name, date):
    if content is not None:
        df_raw = parse_contents(content, name, date)
        df_clean = process_data(df_raw, window_sizes)
        df_mins = df_clean[df_clean["is_diff"] == True]
        fig = plot_best_times(df_clean, df_mins, window_sizes)
        return dcc.Graph("main-graph", figure=fig)
        return fig
        # return parse_contents(content, name, date)


if __name__ == "__main__":
    environment = os.getenv("ENVIRONMENT")
    if environment == "local":
        app.run_server(host="127.0.0.1", port=8000, debug=True)
    else:
        app.run_server()
