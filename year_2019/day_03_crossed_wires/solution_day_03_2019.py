from collections import defaultdict
from utils.file_utils import get_input_file_path, read_input_file


def trace_wire_path(wire_path: list[str]) -> dict[tuple[int, int], int]:
    """
    Trace the path of a wire based on its movement instructions (e.g., "R8", "U5", "L5", "D3").
    :param wire_path: A list of strings representing the wire's movement instructions.
    :return: A dictionary mapping each position to the number of steps taken to reach it (the first time).
    """
    # Define the movement directions for the wire
    directions = {
        "R": (0, 1), "U": (-1, 0), "L": (0, -1), "D": (1, 0)
    }
    # Initialize a dictionary to store positions with steps taken to reach them
    wire_position_to_steps = defaultdict(int)
    # Initialize the starting position of the wire and the number of steps
    x_position = y_position = 0
    steps = 0

    # Iterate through each movement instruction in the wire path
    for movement in wire_path:
        # Extract the direction and distance from the wire path instruction
        direction = movement[0]
        distance = int(movement[1:])

        # Identify the movement direction of the axis x and y
        shift_x, shift_y = directions[direction]

        for _ in range(distance):
            steps += 1
            # Update the coordinate x and y of the wire position and add it to the set of visited positions
            x_position += shift_x
            y_position += shift_y

            # Store the number of steps taken to reach this position (if the position is not already visited)
            wire_position_to_steps.setdefault((x_position, y_position), steps)

    return wire_position_to_steps


def get_min_distance_min_steps(
        wire_1_position_to_steps: dict[tuple[int, int], int],
        wire_2_path: list[str]
) -> tuple[int, int]:
    """
    Calculate the minimum Manhattan distance and steps to reach an intersection point between two wires.
    :param wire_1_position_to_steps: A dictionary mapping positions of the first wire
                                        to the number of steps taken to reach them.
    :param wire_2_path: A list of strings representing the second wire's movement instructions.
    :return: A tuple containing the minimum Manhattan distance and the minimum steps to reach an intersection point
            between the two wires.
    """
    from math import inf

    # Define the movement directions for the wire
    directions = {
        "R": (0, 1), "U": (-1, 0), "L": (0, -1), "D": (1, 0)
    }
    # Initialize the starting position of the wire and the number of steps
    x_position = y_position = 0
    steps = 0
    # Initialize the best distance and steps to infinity (worst case)
    best_distance = inf
    best_steps = inf

    # Iterate through each movement instruction in the wire path
    for movement in wire_2_path:
        # Extract the direction and distance from the wire path instruction
        direction = movement[0]
        distance = int(movement[1:])

        # Identify the movement direction of the axis x and y
        shift_x, shift_y = directions[direction]

        for _ in range(distance):
            steps += 1
            # Update the coordinate x and y of the wire position and add it to the set of visited positions
            x_position += shift_x
            y_position += shift_y
            new_position = (x_position, y_position)

            if new_position in wire_1_position_to_steps:
                # Calculate the Manhattan distance from the origin (0, 0) to the intersection point (part 1)
                best_distance = min(best_distance,  abs(x_position) + abs(y_position))
                # Calculate the minimum steps to reach the intersection point (part 2)
                best_steps = min(best_steps, wire_1_position_to_steps[new_position] + steps)

    return best_distance, best_steps


def solve_day_03_2019(filename: str) -> tuple[int, int]:
    """
    Solution of the Advent of Code 2019 Day 03 - Crossed Wires.
    :param filename: The name file containing the input data.
    :return: A tuple containing the minimum Manhattan distance (part 1) and
            the fewest combined steps (wire 1 + wire 2) to reach an intersection point (part 2).
    """
    try:
        # Create the absolute path of the input file
        input_file_path = get_input_file_path(__file__, filename)
        # Read the input file
        data = read_input_file(input_file_path)
    except Exception as error:
        raise RuntimeError(f"Error: {error}")

    # Split the input data into two wires instructions
    wire_1 = data[0].split(",")
    wire_2 = data[1].split(",")

    # Trace the path of the first wire and store the positions with steps taken to reach them
    wire_1_position_to_steps = trace_wire_path(wire_1)

    # Calculate the minimum Manhattan distance and steps to reach an intersection point between the two wires
    min_manhattan_distance, min_steps = get_min_distance_min_steps(wire_1_position_to_steps, wire_2)

    return min_manhattan_distance, min_steps


if __name__ == "__main__":

    # Import function to print results
    import time
    from utils.file_utils import print_day_results

    # Calculate results for demo and real input files
    demo_1, demo_2 = solve_day_03_2019("input_demo.txt")
    start_time = time.time()
    solution_1, solution_2 = solve_day_03_2019("input.txt")
    end_time = time.time()

    # Calculate execution time in milliseconds
    execution_time = int((end_time - start_time) * 1000)

    # Print results in a formatted table (using rich)
    print_day_results(
        "2019", "03",
        str(demo_1), str(demo_2),
        str(solution_1), str(solution_2),
        execution_time
    )
