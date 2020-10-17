import dash_html_components as html
import dash_core_components as dcc

from cubeviz.helpers import load_text


def upload_window():
    return dcc.Upload(
        id="upload-data",
        children=html.Div(["Drag and Drop or ", html.A("Select Files")]),
        style={
            # "width": "100%",
            "height": "60px",
            "lineHeight": "60px",
            "borderWidth": "1px",
            "borderStyle": "dashed",
            "borderRadius": "5px",
            "textAlign": "center",
            "margin": "10px",
            "color": "rgb(90, 90, 90)",
        },
        multiple=False,
    )


def info_markdown():
    return dcc.Markdown(load_text("cubeviz/markdown/info.md"))


def info_tab_layout():
    return [upload_window(), info_markdown()]


def build_app(app):
    app.layout = html.Div(
        [
            dcc.Tabs(
                [
                    dcc.Tab(label="Info", children=info_tab_layout()),
                    dcc.Tab(label="Solve times", children=[]),
                    dcc.Tab(label="Solve frequency", children=[]),
                    dcc.Tab(label="Progress", children=[]),
                ]
            )
        ]
    )

    return app


# def build_app(app):
#    app.layout = html.Div(
#        [
#            dcc.Upload(
#                id="upload-data",
#                children=html.Div(["Drag and Drop or ", html.A("Select Files")]),
#                style={
#                    "width": "100%",
#                    "height": "60px",
#                    "lineHeight": "60px",
#                    "borderWidth": "1px",
#                    "borderStyle": "dashed",
#                    "borderRadius": "5px",
#                    "textAlign": "center",
#                    "margin": "10px",
#                },
#                multiple=False,
#            ),
#            html.Div(id="div-solve-time-series"),
#        ],
#    )
#    return app

# app.layout = html.Div(
#    [
#        dcc.Tabs(
#            [
#                dcc.Tab(label="Tab one", children=[]),
#                dcc.Tab(label="Tab two", children=[dcc.Graph]),
#                dcc.Tab(label="Tab three", children=[dcc.Graph]),
#            ]
#        )
#    ]
# )
