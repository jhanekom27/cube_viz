import pandas as pd
import dash_core_components as dcc
import plotly.graph_objects as go

from cubeviz.themeing import plotly_theme
from cubeviz.models import CVGroupedDaily, MONTHS


def plot_frequency_heatmap(df_grouped_daily, year, months):
    df_grouped_daily = df_grouped_daily[df_grouped_daily.year == year]
    months_num = list(range(1, 13))
    days_num = list(range(1, 32))

    idx = pd.MultiIndex.from_product([months_num, days_num], names=["month", "day"])
    df_year = pd.DataFrame(index=idx).reset_index()
    df_year = df_year.merge(df_grouped_daily, on=["month", "day"], how="left")

    z_data = df_year["num_solves"].values.reshape((12, 31))
    z_data_null = df_year["num_solves"].isna().astype("int").values.reshape((12, 31))

    fig = go.Figure()

    fig.add_trace(
        go.Heatmap(
            z=z_data_null,
            x=days_num,
            y=months,
            hoverongaps=False,
            zmin=0,
            colorscale=[[0, "rgb(17, 17, 17)"], [1, "rgb(17, 17, 17)"]],
            showscale=False,
        )
    )

    fig.add_trace(go.Heatmap(z=z_data, x=days_num, y=months, hoverongaps=False, zmin=0))

    fig.layout = go.Layout(
        title=f"Solves per day for: {year}",
        xaxis_title="Day of month",
        yaxis_title="Month",
        xaxis={"showgrid": False},
        yaxis={
            "showgrid": False,
            # "autorange": "reversed",
        },
        template=plotly_theme,
    )

    return fig


def get_all_frequency_heatmaps(df_grouped_daily: CVGroupedDaily):
    graphs = []
    years = sorted(list(df_grouped_daily.year.unique()), reverse=True)
    for year in years:
        fig = plot_frequency_heatmap(df_grouped_daily, year, MONTHS)
        graph = dcc.Graph(f"frequency-heatmap-{year}", figure=fig)
        graphs.append(graph)
    return graphs
