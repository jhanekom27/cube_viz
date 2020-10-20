import plotly.io as pio


class CVColors:
    PRIMARY_BLUE = "#002df7"


def load_theme():
    base_layout = pio.templates["plotly_dark"].layout

    cubeviz_theme = {"layout": base_layout}

    return cubeviz_theme


cubeviz_theme = load_theme()
