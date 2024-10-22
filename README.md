# AI for Commenting Code

One sometimes neglected thing is to properly document code. In the case of Python the docstring feature is eminent 
for that. This short project shows how code can be documented with the aid of AI. We will be using `ChatGPT o1-mini` 
from OpenAI.

## The Code

We have a Python file with a few functions and a class that implements a two-dimensional point.

The file [point-no-comment.py](point-no-comment.py) contains the base code used.

It implements a few utility functions and a `Point` class.

## Naïve Attempt

Enter the following into the ChatGPT prompt:

> Write Python docstring for this function:
> ```python
> def polar_to_cartesian(radius: float, theta: float) -> Tuple[float, float]:
>    if radius < 0:
>        raise ValueError("Radius cannot be negative")
>    return radius * math.cos(theta), radius * math.sin(theta)
> ```

The resulting code can be found in [polar-to-cartesian-docstring.py](polar-to-cartesian-docstring.py)

Apart from the comments ChatGPT also inserts a lot of non-code explanation:
> 
> Explanation of the Docstring Components:
> 
> 1. Short Description:
>   *Provides a concise summary of what the function does.
> 2. Detailed Description:
>   * Offers more context about the function’s purpose and its usage.
> 3. Args:
>   *	radius (float):
>     * Description: The radial distance from the origin.
>   *	Constraint: Must be non-negative.
>   *	theta (float):
>     * Description: The angle in radians from the positive x-axis.
> 4. Returns:
>   * Tuple[float, float]:
>   *	Description: A tuple containing the x and y cartesian coordinates corresponding to the given polar coordinates.
> 5. Raises:
>   * ValueError:
>   *	Condition: If the provided radius is negative.
>   * Message: “Radius cannot be negative”
> 6. Example:
>   * Demonstrates how to use the function with sample input and the expected output.
> 
> Additional Recommendations:
> 
> * Type Annotations:
> * Ensure that you have the necessary imports (math and Tuple from typing) to support type annotations and mathematical operations.
> * Validation:
> * The function currently checks for a negative radius. Depending on your application’s requirements, you might want to add more validations, such as ensuring theta is within a specific range, although mathematically any real number for theta is valid.
> * Floating-Point Precision:
> * Be aware of floating-point precision issues when dealing with trigonometric functions. For most applications, the precision provided by Python’s float type is sufficient, but if higher precision is needed, consider using the decimal module.

## Focused Response

We add some more context to the prompt to get a concise result:

> answer in UK English. Answer without explanation. Answer without changing code. Add docstrings for this python function:
>```python
> def cartesian_to_polar(x: float, y: float) -> Tuple[float, float]:
>     return math.hypot(x, y), math.atan2(y, x)
> ```

This provides a short answer without the explanations:

> ```python
> import math
> from typing import Tuple
> 
> def cartesian_to_polar(x: float, y: float) -> Tuple[float, float]:
>     """
>     Convert Cartesian coordinates to polar coordinates.
> 
>     Given a point in Cartesian coordinates (x, y), this function calculates
>     and returns its polar coordinates (r, θ).
> 
>     Args:
>         x (float): The x-coordinate.
>         y (float): The y-coordinate.
> 
>     Returns:
>         Tuple[float, float]: A tuple containing the radius r and the angle θ in radians.
> 
>     Raises:
>         None
> 
>     Examples:
>         >>> cartesian_to_polar(3.0, 4.0)
>         (5.0, 0.9272952180016122)
> 
>     Notes:
>         - The angle θ is measured in radians from the positive x-axis.
>         - This function uses `math.hypot` for calculating the radius, which is more numerically stable.
>     """
>     return math.hypot(x, y), math.atan2(y, x)
> ```

The result can also be found in [cartesian-to-polar-docstring.py](cartesian-to-polar-docstring.py)

## Class Example

The `Point` class can be documented in the same fashion. Check the file 
[class-with-docstring.py](class-with-docstring.py) for an example.

The class is not completely accurate. The `__init__` docstring does not precisely describe that you either
provide (x, y) style coordinates or polar coordinates (radius, theta).
