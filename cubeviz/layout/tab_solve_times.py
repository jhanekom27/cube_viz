import dash_html_components as html


def solve_times_tab_layout():
    return html.Div(
        id="tab-solve-times",
        children=[
            html.Div(id="div-solve-time-series"),
        ],
    )
