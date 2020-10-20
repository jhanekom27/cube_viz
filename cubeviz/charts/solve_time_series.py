from typing import List
import plotly.graph_objects as go
import dash_core_components as dcc

from cubeviz.themeing import plotly_theme
from cubeviz.models import CVEnhanced


def get_ao_windows(cols: List[str]) -> List[str]:
    return [ao for ao in cols if "ao" in ao.lower()]


def plot_solve_time_series(df: CVEnhanced, window_sizes):
    windows = get_ao_windows(df.columns)
    df_mins = df[df.best_time_is_diff == True]

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=df.solve_num,
            y=df.time_sec,
            mode="lines",
            name="Everything",
            line={"color": "white"},
        )
    )

    for window in windows:
        fig.add_trace(
            go.Scatter(
                x=df.solve_num,
                y=df[window],
                mode="lines",
                name=window,
            )
        )

    fig.add_trace(
        go.Scatter(
            x=df_mins.solve_num,
            y=df_mins.best_time,
            mode="lines+markers",
            name="Best",
            line={"dash": "dash", "color": "yellow"},
            marker={"size": 8},
        )
    )

    fig.update_layout(
        template=plotly_theme,
        xaxis_title="Solves",
        yaxis_title="Time (s)",
    )

    return fig


def get_solve_times_graph(df_cv_enhanced, window_sizes):
    fig_solve_times = plot_solve_time_series(df_cv_enhanced, window_sizes)

    return dcc.Graph("main-graph", figure=fig_solve_times, className="big-plot")
