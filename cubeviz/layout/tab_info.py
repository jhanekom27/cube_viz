import dash_core_components as dcc
import dash_html_components as html
from cubeviz.helpers import load_text
from cubeviz.themeing import CVColors


def upload_window():
    return dcc.Upload(
        id="upload-data",
        children=html.Div(["Drag and Drop or ", html.A("Select Files")]),
        multiple=False,
    )


def info_markdown():
    return dcc.Markdown(load_text("cubeviz/markdown/info.md"))


def uploaded_file_name():
    return html.H3(
        id="h2-uploaded-file-name",
    )


def get_title_value(file_name):
    return [
        "Uploaded file: ",
        html.Span(
            id="span-file-name",
            children=file_name,
            style={"color": CVColors.PRIMARY_BLUE},
        ),
    ]


def info_tab_layout():
    return [upload_window(), uploaded_file_name(), info_markdown()]
