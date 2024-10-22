import math
from typing import Tuple

class Point:
    """
    Represents a point in a 2D coordinate system.

    The Point class supports initialization using either Cartesian coordinates (x, y) or
    polar coordinates (radius, theta). It provides properties to access and modify the
    coordinates and methods to invert and switch between polar and Cartesian representations.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize a Point instance.

        Args:
            *args: Two numeric values representing (x, y) coordinates.
            **kwargs: Keyword arguments which can include:
                - x (float): The x-coordinate.
                - y (float): The y-coordinate.
                - radius (float): The radius in polar coordinates.
                - theta (float): The angle in radians in polar coordinates.
                - degrees (float): The angle in degrees in polar coordinates.

        Raises:
            TypeError: If no arguments are provided or if argument patterns do not match.
            ValueError: If the provided numeric values are not both integers or floats.
        """
        self._x: float = 0.0
        self._y: float = 0.0
        self._polar: bool = False
        # the code below is a workaround to have different class initializers based on arguments
        if not args and not kwargs:
            raise TypeError("No arguments entered for constructor")
        if args and len(args) == 2:
            if sum([1 for i in args if type(i) in (int, float)]) != 2:
                raise ValueError("Not all values given are numeric")
            self._x, self._y = args
        elif kwargs and len(kwargs) == 2:
            if sum([1 for i in kwargs.values() if type(i) in (int, float)]) != 2:
                raise ValueError("Not all values given are numeric")
            if 'x' in kwargs and 'y' in kwargs:
                self._x = float(kwargs['x'])
                self._y = float(kwargs['y'])
            elif 'radius' in kwargs and 'theta' in kwargs:
                self._x, self._y = polar_to_cartesian(kwargs['radius'], kwargs['theta'])
            elif 'radius' in kwargs and 'degrees' in kwargs:
                self._x, self._y = polar_to_cartesian(kwargs['radius'], degrees_to_radian(kwargs['degrees']))
        else:
            raise TypeError("Argument mismatch")

    @property
    def x(self) -> float:
        """
        Get the x-coordinate of the point.

        Returns:
            float: The x-coordinate.
        """
        return self._x

    @x.setter
    def x(self, other: float):
        """
        Set the x-coordinate of the point.

        Args:
            other (float): The new x-coordinate.
        """
        self._x = other

    @property
    def y(self) -> float:
        """
        Get the y-coordinate of the point.

        Returns:
            float: The y-coordinate.
        """
        return self._y

    @y.setter
    def y(self, other: float):
        """
        Set the y-coordinate of the point.

        Args:
            other (float): The new y-coordinate.
        """
        self._y = other

    @property
    def radius(self) -> float:
        """
        Get the radius of the point in polar coordinates.

        Returns:
            float: The radius.
        """
        return cartesian_to_polar(self._x, self._y)[0]

    @radius.setter
    def radius(self, other: float):
        """
        Set the radius of the point in polar coordinates.

        Args:
            other (float): The new radius.
        """
        r, t = cartesian_to_polar(self._x, self._y)
        self._x, self._y = polar_to_cartesian(r + other, t)

    @property
    def theta(self) -> float:
        """
        Get the angle θ of the point in polar coordinates.

        Returns:
            float: The angle in radians.
        """
        return cartesian_to_polar(self._x, self._y)[1]

    @theta.setter
    def theta(self, other: float):
        """
        Set the angle θ of the point in polar coordinates.

        Args:
            other (float): The angle increment in radians.
        """
        r, t = cartesian_to_polar(self._x, self._y)
        self._x, self._y = polar_to_cartesian(r, t + other)

    def invert(self) -> "Point":
        """
        Invert the x and y coordinates of the point.

        Returns:
            Point: The point instance with inverted coordinates.
        """
        self._x, self._y = self._y, self._x
        return self

    def polar(self) -> "Point":
        """
        Switch the representation to polar coordinates.

        Returns:
            Point: The point instance in polar representation.
        """
        self._polar = True
        return self

    def cartesian(self) -> "Point":
        """
        Switch the representation to Cartesian coordinates.

        Returns:
            Point: The point instance in Cartesian representation.
        """
        self._polar = False
        return self

    def __eq__(self, other: "Point"):
        """
        Compare this point with another point for equality.

        Args:
            other (Point): The other point to compare with.

        Returns:
            bool: True if both points have the same coordinates, False otherwise.
        """
        return self.x == other.x and self.y == other.y

    def __str__(self) -> str:
        """
        Get the string representation of the point.

        Returns:
            str: The point in either Cartesian or polar format based on its state.
        """
        if self._polar:
            return f"(radius={self.radius:f}, theta={self.theta:f})"
        return f"({self._x:f}, {self._y:f})"