from utils.file_utils import get_input_file_path, read_input_file


def solve_day_05_2017(filename: str) -> tuple[int, int]:
    """
    Solve the Advent of Code 2017 Day 05 - A Maze of Twisty Trampolines, All Alike.
    :param filename: The name of the input file containing the room data.
    :return: A tuple containing the number of steps taken to exit the maze for part 1 and part 2.
    """
    try:
        # Create the absolute path of the input file
        input_file_path = get_input_file_path(__file__, filename)
        # Read the input file
        data = read_input_file(input_file_path)
    except Exception as error:
        raise RuntimeError(f"Error: {error}")

    # Parse the input data to create a list of integers (list of offsets)
    offsets_1 = list(map(int, data))

    # Define the upper limit for the offsets
    limit = len(offsets_1)

    # Initialize position, and steps for part 1
    position_1 = 0
    steps_1 = 0

    # Create a copy of the offsets list for the part 2
    offsets_2 = offsets_1[:]

    # Define the position and steps for part 2
    position_2 = 0
    steps_2 = 0

    # Process the offsets until the position is out of bounds
    while 0 <= position_1 < limit:
        jump_1 = offsets_1[position_1]
        offsets_1[position_1] += 1
        position_1 += jump_1
        steps_1 += 1

    while 0 <= position_2 < limit:
        jump_2 = offsets_2[position_2]
        offsets_2[position_2] += -1 if jump_2 >= 3 else 1
        position_2 += jump_2
        steps_2 += 1

    return steps_1, steps_2


if __name__ == "__main__":

    # Import function to print results
    import time
    from utils.file_utils import print_day_results

    # Calculate results for demo and real input files
    demo_1, demo_2 = solve_day_05_2017("input_demo.txt")
    start_time = time.time()
    solution_1, solution_2 = solve_day_05_2017("input.txt")
    end_time = time.time()

    # Calculate execution time in milliseconds
    execution_time = int((end_time - start_time) * 1000)

    # Print results in a formatted table (using rich)
    print_day_results(
        "2017", "05",
        str(demo_1), str(demo_2),
        str(solution_1), str(solution_2),
        execution_time
    )
