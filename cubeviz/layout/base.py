import dash_html_components as html
import dash_core_components as dcc

from cubeviz.layout.tab_info import info_tab_layout
from cubeviz.layout.tab_solve_times import solve_times_tab_layout


def build_app(app):
    app.layout = html.Div(
        [
            dcc.Tabs(
                [
                    dcc.Tab(label="Info", children=info_tab_layout()),
                    dcc.Tab(label="Solve times", children=solve_times_tab_layout()),
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
