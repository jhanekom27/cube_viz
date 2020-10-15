import plotly.graph_objects as go
from cubeviz.themeing import plotly_theme


def plot_solve_time_series(df, df_mins, window_sizes):
    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=df["num"],
            y=df["time"],
            mode="lines",
            name="Everything",
            line={"color": "white"},
        )
    )

    for window_size in window_sizes:
        fig.add_trace(
            go.Scatter(
                x=df["num"],
                y=df[f"{window_size}_avg"],
                mode="lines",
                name=f"{window_size} avg",
            )
        )

    fig.add_trace(
        go.Scatter(
            x=df_mins["num"],
            y=df_mins["best_time"],
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
        # title=f"Jurgen's solves as at: {today}",
    )

    return fig
