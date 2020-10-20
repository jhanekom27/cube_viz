import plotly.io as pio


class CVColors:
    BACKGROUND = "#111111"
    PRIMARY_BLUE = "#002df7"
    ACCENT_1_BLUE = "#00f2ff"


class CVThemes:
    HEATMAP_COLORSCALE = [
        [0, CVColors.BACKGROUND],
        [0.5, CVColors.PRIMARY_BLUE],
        [1, CVColors.ACCENT_1_BLUE],
    ]


def load_theme():
    # Can only edit properties that are part of plotly layout already
    base_layout = pio.templates["plotly_dark"].layout

    cubeviz_theme = {"layout": base_layout}

    return cubeviz_theme


cubeviz_theme = load_theme()
