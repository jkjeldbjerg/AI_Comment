import math
from typing import Tuple, Any


def polar_to_cartesian(radius: float, theta: float) -> Tuple[float, float]:
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return radius * math.cos(theta), radius * math.sin(theta)


def cartesian_to_polar(x: float, y: float) -> Tuple[float, float]:
    return math.hypot(x, y), math.atan2(y, x)


def degrees_to_radian(degrees: float) -> float:
    return degrees / 180.0 * math.pi


def radian_to_degrees(radian: float) -> float:
    return radian / math.pi * 180.0


class Point:
    def __init__(self, *args, **kwargs):
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
        return self._x

    @x.setter
    def x(self, other: float):
        self._x = other

    @property
    def y(self) -> float:
        return self._y

    @y.setter
    def y(self, other: float):
        self._y = other

    @property
    def radius(self) -> float:
        return cartesian_to_polar(self._x, self._y)[0]

    @radius.setter
    def radius(self, other: float):
        r, t = cartesian_to_polar(self._x, self._y)
        self._x, self._y = polar_to_cartesian(r + other, t)

    @property
    def theta(self) -> float:
        return cartesian_to_polar(self._x, self._y)[1]

    @theta.setter
    def theta(self, other: float):
        r, t = cartesian_to_polar(self._x, self._y)
        self._x, self._y = polar_to_cartesian(r, t + other)

    def invert(self) -> "Point":
        self._x, self._y = self._y, self._x
        return self

    def polar(self) -> "Point":
        self._polar = True
        return self

    def cartesian(self) -> "Point":
        self._polar = False
        return self

    def __eq__(self, other: "Point"):
        return self.x == other.x and self.y == other.y

    def __str__(self) -> str:
        if self._polar:
            return f"(radius={self.radius:f}, theta={self.theta:f})"
        return f"({self._x:f}, {self._y:f})"


def main() -> None:
    pass


if __name__ == '__main__':
    main()
