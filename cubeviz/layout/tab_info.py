import dash_core_components as dcc
import dash_html_components as html
from cubeviz.helpers import load_text
from cubeviz.themeing import CVColors


def display_error_message(message):
    return html.Div(
        [
            html.H1("There was an error processing this file!", style={"color": "red"}),
            html.H2(str(message), style={"color": "red"}),
        ]
    )


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


def error_display():
    return html.Div(id="div-error-display")


def info_tab_layout():
    return [upload_window(), error_display(), uploaded_file_name(), info_markdown()]
