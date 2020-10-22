from dash.dependencies import Input, Output, State

from cubeviz.server import app
from cubeviz.charts import get_solve_times_graph, get_all_frequency_heatmaps
from cubeviz.etl import (
    enhance_base_data,
    parse_upload_content,
    group_enhanced_by_day,
    get_base_from_sample,
)
from cubeviz.layout import get_title_value, display_error_message
from cubeviz.config import cubeviz_config


@app.callback(
    [
        Output("div-error-display", "children"),
        Output("h2-uploaded-file-name", "children"),
        Output("div-solve-time-series", "children"),
        Output("div-frequency-heatmaps", "children"),
    ],
    [Input("upload-data", "contents")],
    [State("upload-data", "filename"), State("upload-data", "last_modified")],
)
def update_output(content, name, date):
    error_display = None
    window_sizes = cubeviz_config.window_sizes
    error_message = None

    if content is not None:
        try:
            df_base = parse_upload_content(content, name, date)
        except Exception as e:
            error_message = e
            name, df_base = get_base_from_sample()
    else:
        name, df_base = get_base_from_sample()

    df_cv_enhanced = enhance_base_data(df_base, window_sizes)
    df_grouped_daily = group_enhanced_by_day(df_cv_enhanced)

    file_name_display = get_title_value(name)
    solve_times_graph = get_solve_times_graph(df_cv_enhanced, window_sizes)
    div_frequency_heatmaps = get_all_frequency_heatmaps(df_grouped_daily)

    if error_message:
        error_display = display_error_message(error_message)

    return (error_display, file_name_display, solve_times_graph, div_frequency_heatmaps)
