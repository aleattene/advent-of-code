from utils.file_utils import get_input_file_path


def solve_day_01_2021(filename: str) -> tuple[int, int]:
    """
    Solution of the Advent of Code 2021 Day 01 - Sonar Sweep.
    :param filename: The name file containing the input data.
    :return: A tuple containing the number of increases in depth for single values (part 1) and
                the number of increases in depth for sliding windows of 3 values (part 2).
    """
    try:
        # Create the absolute path of the input file
        input_file_path = get_input_file_path(__file__, filename)
        with open(input_file_path, 'r', encoding='utf-8') as f:
            # Read the input file
            data = f.read().split("\n")
    except Exception as error:
        raise RuntimeError(f"Error: {error}")

    # Parse the input data (convert string values to integers) and calculate the number of values
    values = [int(value) for value in data]
    num_values = len(values)

    # Calculate the number of increases in depth for single values (part 1)
    increases_value = sum(1 for i in range(num_values - 1) if values[i + 1] > values[i])

    # Calculate the number of increases in depth for sliding windows of 3 values (part 2)
    increases_window = sum(1 for i in range(num_values - 3) if values[i + 3] > values[i])

    return increases_value, increases_window


if __name__ == "__main__":
    # Import function to print results
    import time
    from utils.file_utils import print_day_results

    # Calculate results for demo and real input files
    demo_1, demo_2 = solve_day_01_2021("input_demo.txt")
    start_time = time.time()
    solution_1, solution_2 = solve_day_01_2021("input.txt")
    end_time = time.time()

    # Calculate execution time in milliseconds
    execution_time: int = int((end_time - start_time) * 1000)

    # Print results in a formatted table (using rich)
    print_day_results(
        "2021", "01",
        str(demo_1), str(demo_2),
        str(solution_1), str(solution_2),
        execution_time
    )
