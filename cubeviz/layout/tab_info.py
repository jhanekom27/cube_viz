import dash_core_components as dcc
import dash_html_components as html
from cubeviz.helpers import load_text


def upload_window():
    return dcc.Upload(
        id="upload-data",
        children=html.Div(["Drag and Drop or ", html.A("Select Files")]),
        multiple=False,
    )


def info_markdown():
    return dcc.Markdown(load_text("cubeviz/markdown/info.md"))


def info_tab_layout():
    return [upload_window(), info_markdown()]
