import dash_html_components as html
import dash_core_components as dcc

from cubeviz.layout.tab_info import info_tab_layout
from cubeviz.layout.tab_solve_times import solve_times_tab_layout
from cubeviz.layout.tab_frequency import frequency_tab_layout


def build_app(app):
    app.layout = html.Div(
        [
            dcc.Tabs(
                [
                    dcc.Tab(label="Info", children=info_tab_layout()),
                    dcc.Tab(label="Solve times", children=solve_times_tab_layout()),
                    dcc.Tab(label="Solve frequency", children=frequency_tab_layout()),
                    dcc.Tab(label="Progress", children=[]),
                ]
            )
        ]
    )

    return app
