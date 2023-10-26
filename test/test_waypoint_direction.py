import pytest

from waypoint_direction import get_waypoint_direction, Direction


@pytest.fixture
def waypoints():
    waypoints = []
    with open('waypoints.csv') as fh:
        for i, line in enumerate(fh):
            if i == 0:
                continue
            x, y = line.strip().split(',')
            waypoints.append((float(x), float(y)))
    return waypoints


@pytest.mark.parametrize('index, exp_direction', [
    (1, Direction.RIGHT),
    (50, Direction.LEFT),
    (100, Direction.LEFT),
    (33, Direction.LEFT),
    (423, Direction.RIGHT),
    (200, Direction.LEFT),
    (219, Direction.STRAIGHT),
    (225, Direction.STRAIGHT),
    (226, Direction.LEFT),
    (227, Direction.LEFT),
    (345, Direction.LEFT),
])
def test_waypoint_direction(waypoints, index, exp_direction):
    direction = get_waypoint_direction(waypoints[index], waypoints[index + 1], waypoints[index + 2])
    assert direction == exp_direction
