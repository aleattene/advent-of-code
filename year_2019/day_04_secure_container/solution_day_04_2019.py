from itertools import combinations_with_replacement, groupby
from utils.file_utils import get_input_file_path, read_input_file


def check_double_adjacency(password: str) -> tuple[bool, bool]:
    """
    Check if the password has double adjacency and exact double adjacency.
    :param password: The password to check.
    :return: A tuple with two boolean values indicating the presence of double adjacency and exact double adjacency.
    """
    # Initialize flags for double adjacency and exact double adjacency
    has_doubles = False
    has_exact_double = False

    # Iterate through the digits of the password using group by function (expecting: digit [ digit, digit, ...])
    for digit, group in groupby(password):
        digit_occurrences = list(group)
        # Check if are present double adjacency (part 1)
        if not has_doubles and len(digit_occurrences) > 1:
            has_doubles = True
        # Check if are present exact double adjacency (part 2)
        if not has_exact_double and len(digit_occurrences) == 2:
            has_exact_double = True
        # If both conditions are met, break the loop
        if has_doubles and has_exact_double:
            break

    return has_doubles, has_exact_double


def solve_day_04_2019(filename: str) -> tuple[int, int]:
    """
    Solution of the Advent of Code 2019 Day 04 - Secure Container.
    :param filename: The name file containing the input data.
    :return: A tuple with two integers representing the number of valid passwords for part 1 and part 2.
    """
    try:
        # Create the absolute path of the input file
        input_file_path = get_input_file_path(__file__, filename)
        # Read the input file
        data = read_input_file(input_file_path)[0]
    except Exception as error:
        raise RuntimeError(f"Error: {error}")

    # Parse the input data to get the start and end range of the password
    start_range, end_range = map(int, data.split("-"))

    # Define the password length and number of digits (according to the rules)
    password_length = 6
    password_digits = 10

    # Initialize counters for valid passwords (part 1 and part 2)
    valid_passwords_1 = 0
    valid_passwords_2 = 0

    # Generate all possible combinations with replacement (increasing order by default convention)
    increasing_passwords = combinations_with_replacement(range(password_digits), password_length)
    for password_tuple in increasing_passwords:
        # Convert the tuple of digits to a string and then to an integer
        password_string = "".join(map(str, password_tuple))
        password_number = int(password_string)
        # Check if the password number is within the specified range otherwise skip or break
        if password_number < start_range:
            continue
        elif password_number > end_range:
            break

        # Check if the password number is valid (according to the rules part 1 and part 2)
        has_doubles, has_exact_double = check_double_adjacency(password_string)

        # If the password number is valid, increment the counters (part 1 and part 2)
        if has_doubles:
            valid_passwords_1 += 1
        if has_exact_double:
            valid_passwords_2 += 1

    return valid_passwords_1, valid_passwords_2


if __name__ == "__main__":
    # Import function to print results
    import time
    from utils.file_utils import print_day_results

    # Calculate results for demo and real input files
    demo_1, demo_2 = solve_day_04_2019("input_demo.txt")
    start_time = time.time()
    solution_1, solution_2 = solve_day_04_2019("input.txt")
    end_time = time.time()

    # Calculate execution time in milliseconds
    execution_time = int((end_time - start_time) * 1000)

    # Print results in a formatted table (using rich)
    print_day_results(
        "2019", "04",
        str(demo_1), str(demo_2),
        str(solution_1), str(solution_2),
        execution_time
    )
