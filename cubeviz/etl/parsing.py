import base64
import io
import pandas as pd
import dash_html_components as html

from cubeviz.config import cubeviz_config
from cubeviz.models import CVEnhanced
from cubeviz.etl.process_data_sources import (
    get_data_source_format,
    parse_timiks_to_base,
    UploadFormats,
)
from cubeviz.etl.enhance import enhance_base_data


def parse_upload_content(contents: str, filename: str, date) -> CVEnhanced:
    content_type, content_string = contents.split(",")
    window_sizes = cubeviz_config.window_sizes

    decoded = base64.b64decode(content_string)
    try:
        if "csv" in filename:
            # Assume that the user uploaded a CSV file
            df = pd.read_csv(io.StringIO(decoded.decode("utf-8")))
        elif "xls" in filename:
            # Assume that the user uploaded an excel file
            df = pd.read_excel(io.BytesIO(decoded))

        data_format = get_data_source_format(df)

        if data_format == UploadFormats.TIMIKS:
            df = parse_timiks_to_base(df)
        else:
            raise Exception("Uh oh!")

        df = enhance_base_data(df, window_sizes)

    except Exception as e:
        print(e)
        return html.Div(["There was an error processing this file."])

    return df
