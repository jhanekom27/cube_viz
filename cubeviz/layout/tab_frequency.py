import dash_html_components as html


def frequency_tab_layout():
    return html.Div(
        id="tab-frequency", children=[html.Div(id="div-frequency-heatmaps")]
    )
