from collections import Counter
from utils.file_utils import get_input_file_path, read_input_file


def solve_day_02_2018(filename: str) -> tuple[int, str | None]:
    """
    Solve the Advent of Code 2018 Day 02 - Inventory Management System.
    :param filename: The name of the input file containing the room data.
    :return: A tuple containing the checksum (part 1) and the common letters between the correct boxes (part 2).
    """
    try:
        # Create the absolute path of the input file
        input_file_path = get_input_file_path(__file__, filename)
        # Read the input file
        data = read_input_file(input_file_path)
    except Exception as error:
        raise RuntimeError(f"Error: {error}")

    # Count the number of IDs with exactly two and three of any letter (counted separately)
    id_with_twice_letters = sum(1 for box in data if 2 in Counter(box).values())
    id_with_thrice_letters = sum(1 for box in data if 3 in Counter(box).values())

    # Calculate the checksum (part 1)
    checksum = id_with_twice_letters * id_with_thrice_letters

    # Length of the boxes (number of letters in each box)
    box_length = len(data[0])

    # Remove one letter at a time from each box and check for duplicates
    for i_to_remove in range(box_length):
        # Create a set to store the seen substrings of boxes created by removing one letter in position i_to_remove
        seen_substrings = set()

        for box in data:
            # Create substring of the box by removing the letter at index i_to_remove
            box_substring = box[:i_to_remove] + box[i_to_remove + 1:]

            if box_substring in seen_substrings:
                # If the substring is already in the set, we have found two boxes that differ by one letter
                correct_box_common_letters = box_substring
                # Return the checksum (part 1) and the common letters between the correct boxes (part 2)
                return checksum, correct_box_common_letters

            # If the substring is not in the set, add it and continue searching
            seen_substrings.add(box_substring)

    # If no common letters are found, return None
    return checksum, None


if __name__ == "__main__":

    # Import function to print results
    import time
    from utils.file_utils import print_day_results

    # Calculate results for demo and real input files
    demo_1, demo_2 = solve_day_02_2018("input_demo.txt")
    start_time = time.time()
    solution_1, solution_2 = solve_day_02_2018("input.txt")
    end_time = time.time()

    # Calculate execution time in milliseconds
    execution_time = int((end_time - start_time) * 1000)

    # Print results in a formatted table (using rich)
    print_day_results(
        "2018", "02",
        str(demo_1), str(demo_2),
        str(solution_1), str(solution_2),
        execution_time
    )
