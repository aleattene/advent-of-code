from utils.file_utils import get_input_file_path


def solve_day_02_2021(filename: str) -> tuple[int, int]:
    """
    Solution of the Advent of Code 2021 Day 02 - Dive.
    :param filename: The name file containing the input data.
    :return: A tuple containing the product of horizontal and depth positions for both parts.
    """
    try:
        # Create the absolute path of the input file
        input_file_path = get_input_file_path(__file__, filename)
        with open(input_file_path, 'r', encoding='utf-8') as f:
            # Read the input file
            data = f.read().split("\n")
    except Exception as error:
        raise RuntimeError(f"Error: {error}")

    # Parse the input data
    data = [line.strip() for line in data]

    # Initialize variables for horizontal and depth positions for both parts
    horizontal_1 = depth_1 = 0
    horizontal_2 = depth_2 = aim = 0

    # Iterate through each command in the input data
    for command in data:

        # Split the command into direction and number using the walrus operator and unpacking
        direction, number = (command_parts := command.split())[0], int(command_parts[1])

        # Update horizontal and depth positions based on the command (part 1 and part 2)
        match direction:
            case "forward":
                horizontal_1 += number
                horizontal_2 += number
                depth_2 += (aim * number)
            case "up":
                depth_1 -= number
                aim -= number
            case "down":
                depth_1 += number
                aim += number

    # Return the product of horizontal and depth positions for both parts
    return horizontal_1 * depth_1, horizontal_2 * depth_2


if __name__ == "__main__":
    # Import function to print results
    import time
    from utils.file_utils import print_day_results

    # Calculate results for demo and real input files
    demo_1, demo_2 = solve_day_02_2021("input_demo.txt")
    start_time = time.time()
    solution_1, solution_2 = solve_day_02_2021("input.txt")
    end_time = time.time()

    # Calculate execution time in milliseconds
    execution_time: int = int((end_time - start_time) * 1000)

    # Print results in a formatted table (using rich)
    print_day_results(
        "2021", "02",
        str(demo_1), str(demo_2),
        str(solution_1), str(solution_2),
        execution_time
    )
