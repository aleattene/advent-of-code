from itertools import combinations
from utils.file_utils import get_input_file_path, read_input_file


def even_division_result(row: list[int]) -> int:
    """
    Returns the value of value_2//value_1 of the first divisible pair (value_1,value_2).
    The input list must be sorted in ascending order to ensure that in each row
    the value_1 is less or equal than the value_2 (value_1 <= value_2).
    """
    for value_1, value_2 in combinations(sorted(row), 2):
        if value_2 % value_1 == 0:
            return value_2 // value_1
    raise ValueError("No divisible pair found in the row.")


def solve_day_02_2017(filename: str) -> tuple[int, int] | str:
    try:
        # Create the absolute path of the input file
        input_file_path = get_input_file_path(__file__, filename)
        # Read the input file
        data = read_input_file(input_file_path)
    except Exception as error:
        return f"Error: {error}"

    # Preliminary data processing to transform the input list of strings into a list of lists of integers
    data_int = [list(map(int, line.split())) for line in data]

    # Calculate the checksum for part 1 by summing the differences between the maximum and minimum values in each row
    checksum_1 = sum(max(values) - min(values) for values in data_int)

    # Calculate the total for part 2 by summing the results of the even division of each row
    checksum_2 = sum(even_division_result(values) for values in data_int)

    return checksum_1, checksum_2


if __name__ == "__main__":

    # Import function to print results
    from utils.file_utils import print_day_results

    # Calculate results for demo and real input files
    demo_1, demo_2 = solve_day_02_2017("input_demo.txt")
    solution_1, solution_2 = solve_day_02_2017("input.txt")

    # Print results in a formatted table (using rich)
    print_day_results(
        "2017", "02",
        str(demo_1), str(demo_2),
        str(solution_1), str(solution_2)
    )
