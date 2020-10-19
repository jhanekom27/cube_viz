import plotly.graph_objects as go
from cubeviz.themeing import plotly_theme
from cubeviz.models import CVEnhanced
from cubeviz.etl.raw.parsing import get_relevant_windows


def plot_solve_time_series(df: CVEnhanced, window_sizes):
    # TODO: clean this up
    window_sizes = get_relevant_windows(df, window_sizes)
    print(df.columns)
    df_mins = df[df["best_time_is_diff"] == True]
    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=df.solve_num,
            y=df.time_sec,
            # x=df["num"],
            # y=df["time"],
            mode="lines",
            name="Everything",
            line={"color": "white"},
        )
    )

    for window_size in window_sizes:
        fig.add_trace(
            go.Scatter(
                x=df.solve_num,
                y=df[f"Ao{window_size}"],
                mode="lines",
                name=f"Ao{window_size}",
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
