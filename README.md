Determine direction of a path given three waypoints.

## Prerequisites

* Python
* `pip install -r requirements.txt`

## Usage

### Graph

1. Run `/src/graph_waypoint_direction.py` which will launch an interactive shell.
2. Pick a waypoint to consider (integer), or 'q' to quit
3. A graph will show the specified index point with the following two, moving from red -> green -> blue (think `rgb`)
4. The road is turning away from the green point.

### Get Direction of Turn

* Use `get_waypoint_direction` and specify three waypoint (moving from w0 -> w2)
* Optionally specify a threshold which will count any variance less than this 'STRAIGHT' (i.e., the road doesn't turn)
* This will return a direction (Direction.LEFT, Direction.RIGHT, Direction.STRAIGHT)

### Run Tests

* `pytest test`