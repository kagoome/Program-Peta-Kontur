import plotly.graph_objects as go


def create_3d_surface(
    grid_x_top,
    grid_y_top,
    grid_top,
    grid_x_bottom,
    grid_y_bottom,
    grid_bottom,
    wells
):

    fig = go.Figure()

    # Top surface
    fig.add_trace(
        go.Surface(
            x=grid_x_top,
            y=grid_y_top,
            z=grid_top,
            name="Top Sandstone",
            colorscale="Viridis",
            opacity=0.85,
            showscale=True,
            colorbar=dict(
                title="Top"
            )
        )
    )

    # Bottom surface
    fig.add_trace(
        go.Surface(
            x=grid_x_bottom,
            y=grid_y_bottom,
            z=grid_bottom,
            name="Bottom Sandstone",
            colorscale="Cividis",
            opacity=0.75,
            showscale=True,
            colorbar=dict(
                title="Bottom"
            )
        )
    )

    # Posisi sumur
    fig.add_trace(
        go.Scatter3d(
            x=wells["X"],
            y=wells["Y"],
            z=wells["Top"],
            mode="markers+text",
            marker=dict(
                size=5,
                color="red"
            ),
            text=wells["No Sumur"],
            textposition="top center",
            name="Wells"
        )
    )

    fig.update_layout(
        title="3D Sandstone Surface",
        scene=dict(
            xaxis_title="Coordinate X",
            yaxis_title="Coordinate Y",
            zaxis_title="Depth",
            aspectmode="data"
        ),
        height=750
    )

    return fig