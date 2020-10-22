import base64
import io
import pandas as pd

from cubeviz.models import CVBase
from cubeviz.etl.process_data_sources import (
    get_data_source_format,
    parse_timiks_to_base,
    UploadFormats,
)


def parse_upload_content(contents: str, filename: str, date) -> CVBase:
    content_type, content_string = contents.split(",")

    decoded = base64.b64decode(content_string)

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

    return df
