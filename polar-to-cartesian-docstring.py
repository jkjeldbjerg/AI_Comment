import math
from typing import Tuple


def polar_to_cartesian(radius: float, theta: float) -> Tuple[float, float]:
    """
    Convert polar coordinates to cartesian coordinates.

    This function takes a radial distance and an angle in radians, and converts
    them into corresponding cartesian (x, y) coordinates.

    Args:
        radius (float): The radial distance from the origin. Must be non-negative.
        theta (float): The angle in radians measured from the positive x-axis.

    Returns:
        Tuple[float, float]: A tuple containing the x and y cartesian coordinates.

    Raises:
        ValueError: If the provided radius is negative.

    Example:
        >>> polar_to_cartesian(5, math.pi / 4)
        (3.5355339059327378, 3.5355339059327373)
    """
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return radius * math.cos(theta), radius * math.sin(theta)
