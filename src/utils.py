
from typing import Tuple

def distance(point_A: Tuple[int, int], point_B: Tuple[int, int]) -> float:
    """Returns the euclidean disatance between point A and point B.

    Args:
        point_A (Tuple[int, int]): The first point
        point_B (Tuple[int, int]): The second point

    Returns:
        float: The euclidean disatance between point A and point B
    """
    # This function would be called too often, so keeping it short.
    return ((point_A[0] - point_B[0]) ** 2 + (point_A[1] - point_B[1]) ** 2) ** (0.5)
