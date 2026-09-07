import matplotlib.pyplot as plt
import numpy as np


WIDTH = 3508
HEIGHT = 2480
DPI = 100


def create_contour_map(
    grid_x,
    grid_y,
    grid_z,
    wells,
    value_column,
    title,
    output_path=None,
    contour_interval=None
):

    figsize = (
        WIDTH / DPI,
        HEIGHT / DPI
    )

    fig, ax = plt.subplots(
        figsize=figsize,
        dpi=DPI
    )

    valid_values = grid_z[
        ~np.isnan(grid_z)
    ]

    if len(valid_values) == 0:
        raise ValueError(
            "Tidak ada area yang dapat diinterpolasi."
        )

    minimum = np.nanmin(grid_z)
    maximum = np.nanmax(grid_z)

    if contour_interval is None:

        value_range = maximum - minimum

        if value_range <= 100:
            contour_interval = 10
        elif value_range <= 500:
            contour_interval = 25
        else:
            contour_interval = 50

    start = (
        np.floor(minimum / contour_interval)
        * contour_interval
    )

    end = (
        np.ceil(maximum / contour_interval)
        * contour_interval
    )

    levels = np.arange(
        start,
        end + contour_interval,
        contour_interval
    )

    # Filled contour
    filled = ax.contourf(
        grid_x,
        grid_y,
        grid_z,
        levels=100,
        cmap="viridis"
    )

    # Contour line
    contours = ax.contour(
        grid_x,
        grid_y,
        grid_z,
        levels=levels,
        colors="black",
        linewidths=0.8
    )

    ax.clabel(
        contours,
        inline=True,
        fontsize=10,
        fmt="%1.0f"
    )

    # Titik sumur
    ax.scatter(
        wells["X"],
        wells["Y"],
        s=80,
        facecolors="white",
        edgecolors="black",
        linewidths=1.5,
        zorder=5
    )

    # Label sumur
    for _, well in wells.iterrows():

        ax.annotate(
            str(well["No Sumur"]),
            (
                well["X"],
                well["Y"]
            ),
            xytext=(8, 8),
            textcoords="offset points",
            fontsize=10,
            fontweight="bold"
        )

    # Colorbar
    colorbar = fig.colorbar(
        filled,
        ax=ax,
        pad=0.02
    )

    colorbar.set_label(
        value_column,
        fontsize=14
    )

    ax.set_title(
        title,
        fontsize=20,
        fontweight="bold",
        pad=15
    )

    ax.set_xlabel(
        "Coordinate X",
        fontsize=14
    )

    ax.set_ylabel(
        "Coordinate Y",
        fontsize=14
    )

    ax.set_aspect(
        "equal",
        adjustable="box"
    )

    ax.grid(
        True,
        linestyle="--",
        alpha=0.3
    )

    plt.tight_layout()

    if output_path:
        fig.savefig(
            output_path,
            dpi=DPI,
            bbox_inches="tight"
        )

    return fig