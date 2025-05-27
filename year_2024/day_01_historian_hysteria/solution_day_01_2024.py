from collections import Counter
from utils.file_utils import get_input_file_path, read_input_file


def solve_day_01_2024(filename: str) -> tuple[int, int]:
    """
    Solution of the Advent of Code 2024 Day 01 - Historian Hysteria.
    :param filename: The name file containing the input data.
    :return:
    """
    try:
        # Create the absolute path of the input file
        input_file_path = get_input_file_path(__file__, filename)
        # Read the input file
        data = read_input_file(input_file_path)
    except Exception as error:
        raise RuntimeError(f"Error: {error}")

    # Parse the data into two sorted lists of integers
    left_list: list[int] = []
    right_list: list[int] = []
    for line in data:
        left, right = map(int, line.split())
        left_list.append(left)
        right_list.append(right)
    left_list.sort()
    right_list.sort()

    # Calculate the sum of the absolute differences between the lists (part 1)
    sum_differences: int = sum(abs(left - right) for left, right in zip(left_list, right_list))

    # Create a Counter object for the right list
    right_counter: Counter[int] = Counter(right_list)

    # Calculate the similarity score between the lists (part 2)
    similarity_score: int = sum(value * right_counter[value] for value in left_list)

    return sum_differences, similarity_score



if __name__ == "__main__":
    # Import function to print results
    import time
    from utils.file_utils import print_day_results

    # Calculate results for demo and real input files
    demo_1, demo_2 = solve_day_01_2024("input_demo.txt")
    start_time = time.time()
    solution_1, solution_2 = solve_day_01_2024("input.txt")
    end_time = time.time()

    # Calculate execution time in milliseconds
    execution_time: int = int((end_time - start_time) * 1000)

    # Print results in a formatted table (using rich)
    print_day_results(
        "2024", "01",
        str(demo_1), str(demo_2),
        str(solution_1), str(solution_2),
        execution_time
    )

