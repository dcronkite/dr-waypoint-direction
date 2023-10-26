import math
from enum import Enum


class DotOnSide(Enum):
    LEFT = 0
    RIGHT = 1
    ON_LINE = 2


class Direction(Enum):
    LEFT = 1
    RIGHT = 0
    STRAIGHT = 2


def get_waypoint_side(w0, w1, w2, threshold=0.0000005) -> DotOnSide:
    """On which side is w1 of a line from w0 to w2"""
    x0, y0 = w0
    x1, y1 = w1
    x2, y2 = w2
    m = (y2 - y0) / (x2 - x0)
    b = y2 - (m * x2)
    # get predicted y1 if w1 were on the line
    y1_pred = (x1 * m) + b
    distance = ((m * x1) + (-1 * y1) + b) / math.sqrt((m ** 2) + 1)
    if abs(distance) < threshold:  # threshold to consider the point on the line
        return DotOnSide.ON_LINE
    if x2 > x0:
        if y1_pred < y1:
            return DotOnSide.LEFT
        else:
            return DotOnSide.RIGHT
    else:
        if y1_pred < y1:
            return DotOnSide.RIGHT
        else:
            return DotOnSide.LEFT


def get_waypoint_direction(w0, w1, w2, threshold=0.0000005) -> Direction:
    side = get_waypoint_side(w0, w1, w2, threshold=threshold)
    print(f'Dot on side: {side}')
    if side == DotOnSide.RIGHT:
        # road is turning left
        return Direction.LEFT
    elif side == DotOnSide.LEFT:
        # road is turning left
        return Direction.RIGHT
    elif side == DotOnSide.ON_LINE:
        return Direction.STRAIGHT
    else:
        raise ValueError(f'Unrecognized side: {side}')
