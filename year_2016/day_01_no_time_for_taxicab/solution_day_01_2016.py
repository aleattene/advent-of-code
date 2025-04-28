from utils.file_utils import get_input_file_path, read_input_file, get_manhattan_distance


def solve_day_01_2016(filename: str) -> tuple[int, int] | str:
    try:
        # Create the absolute path of the input file
        input_file_path = get_input_file_path(__file__, filename)
        # Read the input file
        data = read_input_file(input_file_path)[0]
    except Exception as error:
        return f"Error: {error}"

    # Directions (North, East, South, West)
    directions = ((-1, 0), (0, 1), (1, 0), (0, -1))
    index_current_direction = 0
    position_x = position_y = 0

    # Dictionary to map left and right turns to their respective direction changes
    rotations_direction = {"L": -1, "R": 1}

    # List to keep track of visited positions
    visited_positions = [(0, 0)]
    first_position_visited_distance = None

    for token in data.split(", "):
        # Extract the direction and number of steps from the token
        step_direction = token[0]
        steps = int(token[1:])

        # Update the current direction based on the turn (left or right)
        index_current_direction += rotations_direction[step_direction]
        step_x, step_y = directions[index_current_direction % len(directions)]

        # Move in the current direction for the specified number of steps
        for _ in range(steps):
            position_x += step_x
            position_y += step_y
            position = (position_x, position_y)
            if first_position_visited_distance is None and position in visited_positions:
                # Manhattan distance from the first position visited to the starting point (0,0)
                first_position_visited_distance = get_manhattan_distance(position_x, position_y)
            elif first_position_visited_distance is None:
                visited_positions.append(position)

    # Manhattan distance from the last position to the starting point (0,0)
    final_distance = get_manhattan_distance(position_x, position_y)

    return final_distance, first_position_visited_distance

