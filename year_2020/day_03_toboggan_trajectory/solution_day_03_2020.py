import math
from utils.file_utils import get_input_file_path, read_input_file


def count_trees(data: list[str], slope: tuple[int, int]) -> int:
    """
    Count the number of trees (#) encountered on a given slope (right, down).
    :param data: The map of the area.
    :param slope: The slope defined by (right, down).
    :return: The number of trees encountered on the slope in the map.
    """

    # Initialize the number of rows, columns, current row and column, and the number of trees encountered
    rows: int = len(data)
    cols: int = len(data[0])
    row = col = 0
    trees: int = 0
    right, down = slope

    # Iterate through the map using the slope to move down and right until the end of the vertical map (rows)
    while row < rows - 1:
        row, col = row + down, (col + right) % cols
        # Check if the current position is a tree (#) and increment the count
        if data[row][col] == "#":
            trees += 1

    return trees


def solve_day_03_2020(filename: str) -> tuple[int, int]:
    """
    Solution of the Advent of Code 2020 Day 03 - Toboggan Trajectory.
    :param filename: The name file containing the input data.
    :return: A tuple containing the number of trees encountered on the slope (3, 1) (part 1) and
            a product of the number of trees encountered on the slopes (1, 1), (3, 1), (5, 1), (7, 1), (1, 2) (part 2).
    """
    try:
        # Create the absolute path of the input file
        input_file_path = get_input_file_path(__file__, filename)
        # Read the input file
        data = read_input_file(input_file_path)
    except Exception as error:
        raise RuntimeError(f"Error: {error}")

    # Initialize a list of slopes to check (part 2)
    slopes: list[tuple[int, int]] = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

    # Count the number of trees encountered for the part 1 - slope (3, 1)
    trees_2: int = count_trees(data, slopes[1])

    # Count the number of trees encountered for the part 2 - slopes (1, 1), (3, 1), (5, 1), (7, 1), (1, 2)
    trees_product: int = math.prod(count_trees(data, slope) for slope in slopes)

    # Return the number of trees encountered
    return trees_2, trees_product



if __name__ == "__main__":
    # Import function to print results
    import time
    from utils.file_utils import print_day_results

    # Calculate results for demo and real input files
    demo_1, demo_2 = solve_day_03_2020("input_demo.txt")
    start_time = time.time()
    solution_1, solution_2 = solve_day_03_2020("input.txt")
    end_time = time.time()

    # Calculate execution time in milliseconds
    execution_time = int((end_time - start_time) * 1000)

    # Print results in a formatted table (using rich)
    print_day_results(
        "2020", "03",
        str(demo_1), str(demo_2),
        str(solution_1), str(solution_2),
        execution_time
    )
