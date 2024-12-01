from collections import Counter
from utils.file_utils import get_input_file_path, read_input_file


def solve_day_01_2024(filename: str) -> tuple[int, int] | str:

    try:
        # Create the absolute path of the input file
        input_file_path = get_input_file_path(__file__, filename)
        # Read the input file
        data = read_input_file(input_file_path)
    except Exception as error:
        return f"Error: {error}"

    # Parse the data into left and right lists
    left_list = []
    right_list = []
    for line in data:
        left, right = map(int, line.split())
        left_list.append(left)
        right_list.append(right)

    # Sort the left and right lists
    left_list.sort()
    right_list.sort()

    # Part One - Calculate the sum of the absolute differences between the left and right lists
    sum_differences = sum(abs(left - right) for left, right in zip(left_list, right_list))

    # Create a Counter object for the right list
    right_counter = Counter(right_list)

    # Part Two - Calculate the similarity score between the left and right lists
    similarity_score = sum(value * right_counter[value] for value in left_list)

    return sum_differences, similarity_score
