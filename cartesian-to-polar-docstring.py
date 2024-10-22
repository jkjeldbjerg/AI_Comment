import math
from typing import Tuple


def cartesian_to_polar(x: float, y: float) -> Tuple[float, float]:
    """
    Convert Cartesian coordinates to polar coordinates.

    Given a point in Cartesian coordinates (x, y), this function calculates
    and returns its polar coordinates (r, θ).

    Args:
        x (float): The x-coordinate.
        y (float): The y-coordinate.

    Returns:
        Tuple[float, float]: A tuple containing the radius r and the angle θ in radians.

    Raises:
        None

    Examples:
        >>> cartesian_to_polar(3.0, 4.0)
        (5.0, 0.9272952180016122)

    Notes:
        - The angle θ is measured in radians from the positive x-axis.
        - This function uses `math.hypot` for calculating the radius, which is more numerically stable.
    """
    return math.hypot(x, y), math.atan2(y, x)