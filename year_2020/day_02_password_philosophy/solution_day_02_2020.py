from utils.file_utils import get_input_file_path, read_input_file


def solve_day_02_2020(filename: str) -> tuple[int, int]:
    """
    Solution of the Advent of Code 2020 Day 02 - Password Philosophy.
    :param filename: The name file containing the input data.
    :return: A tuple containing the number of valid passwords (according to the policy) for part 1 and part 2.
    """
    try:
        # Create the absolute path of the input file
        input_file_path = get_input_file_path(__file__, filename)
        # Read the input file
        data = read_input_file(input_file_path)
    except Exception as error:
        raise RuntimeError(f"Error: {error}")

    # Initialize the number of valid passwords for both parts
    valid_passwords_1: int = 0
    valid_passwords_2: int = 0

    # Iterate through each line of the input data ("password-policy character: password")
    for line in data:
        # Identify the values of the password policy and the password
        values_range, token, password = line.split(" ")
        char_required: str = token[0]
        min_reference , max_reference = map(int, values_range.split("-", 1))

        # Check if the password is valid verifying the number of occurrences of the required character
        if min_reference <= password.count(char_required) <= max_reference:
            valid_passwords_1 += 1

        # Check if the password is valid using XOR operator: True if exactly one of the operands is True (part 2)
        if (password[min_reference - 1] == char_required) ^ (password[max_reference - 1] == char_required):
            valid_passwords_2 += 1

    return valid_passwords_1, valid_passwords_2



if __name__ == "__main__":
    # Import function to print results
    import time
    from utils.file_utils import print_day_results

    # Calculate results for demo and real input files
    demo_1, demo_2 = solve_day_02_2020("input_demo.txt")
    start_time = time.time()
    solution_1, solution_2 = solve_day_02_2020("input.txt")
    end_time = time.time()

    # Calculate execution time in milliseconds
    execution_time = int((end_time - start_time) * 1000)

    # Print results in a formatted table (using rich)
    print_day_results(
        "2020", "02",
        str(demo_1), str(demo_2),
        str(solution_1), str(solution_2),
        execution_time
    )
