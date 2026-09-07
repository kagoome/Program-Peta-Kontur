import numpy as np
from scipy.interpolate import griddata


def create_interpolation(
    x,
    y,
    z,
    resolution=300,
    method="linear"
):
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    z = np.asarray(z, dtype=float)

    min_x = x.min()
    max_x = x.max()

    min_y = y.min()
    max_y = y.max()

    grid_x = np.linspace(
        min_x,
        max_x,
        resolution
    )

    grid_y = np.linspace(
        min_y,
        max_y,
        resolution
    )

    grid_x, grid_y = np.meshgrid(
        grid_x,
        grid_y
    )

    grid_z = griddata(
        (x, y),
        z,
        (grid_x, grid_y),
        method=method
    )

    return grid_x, grid_y, grid_z