from utils.file_utils import get_input_file_path


def get_most_and_least_common_bits(data: str) -> tuple[str, str]:
    """
    Get the most and least common bits in a binary string.
    :param data: A binary string.
    :return: A tuple containing the most common and least common bits.
    """
    # Count the occurrences of '1's and '0's in the data string
    ones = data.count('1')
    zeros = len(data) - ones
    return ('1', '0') if ones >= zeros else ('0', '1')


def find_rating(data: list[str], num_col: int = 0, is_most_common_bit: bool = True) -> int:
    """
    Find the rating (oxygen generator or CO2 scrubber) based on the most or least common bits.
    :param data: A list of binary strings.
    :param num_col: The current column index to evaluate (default is 0).
    :param is_most_common_bit: If True, find the most common bit; otherwise, find the least common bit.
    :return: The rating as an integer.
    """

    # Check if the data list has only one element (base case for recursion)
    if len(data) == 1:
        return int(data[0], 2)

    # Identify the most and least common bits in the current column (num_col)
    column = ''.join(row[num_col] for row in data)
    most_common, least_common = get_most_and_least_common_bits(column)

    # Identify the bit criteria: most common or least common
    bit_criteria = most_common if is_most_common_bit else least_common

    # Filter the data based on the bit criteria
    filtered = [row for row in data if row[num_col] == bit_criteria]

    # Recursively call find_rating with the next column
    return find_rating(filtered, num_col + 1, is_most_common_bit)


def solve_day_03_2021(filename: str) -> tuple[int, int]:
    """
    Solution of the Advent of Code 2021 Day 03 - Binary Diagnostic.
    :param filename: The name file containing the input data.
    :return: A tuple containing the power consumption (part 1) and life support rating (part 2).
    """
    try:
        # Create the absolute path of the input file
        input_file_path = get_input_file_path(__file__, filename)
        with open(input_file_path, 'r', encoding='utf-8') as f:
            # Read the input file
            data = f.read().split("\n")
    except Exception as error:
        raise RuntimeError(f"Error: {error}")

    # Parse the input data to create a transposed list of bits
    columns = [''.join(col) for col in zip(*data)]

    # Initialize variables for gamma and epsilon rates
    gamma_rate: list[str] = []
    epsilon_rate: list[str] = []

    # Iterate through each column of bits
    for column in columns:
        # Find the most common and least common bits [('value', 'frequency']), ... , ('value', 'frequency')
        most_common, least_common = get_most_and_least_common_bits(column)
        gamma_rate.append(most_common)
        epsilon_rate.append(least_common)

    # Calculate the power consumption (part 1)
    power_consumption = int("".join(gamma_rate), 2) * int("".join(epsilon_rate), 2)

    # Find the oxygen generator and CO2 scrubber ratings using recursion and calculate the life support rating (part 2)
    oxygen_generator_rating = find_rating(data, 0, True)
    co2_scrubber_rating = find_rating(data, 0, False)
    life_support_rating = oxygen_generator_rating * co2_scrubber_rating

    # Return the power consumption and life support rating
    return power_consumption, life_support_rating


if __name__ == "__main__":
    # Import function to print results
    import time
    from utils.file_utils import print_day_results

    # Calculate results for demo and real input files
    demo_1, demo_2 = solve_day_03_2021("input_demo.txt")
    start_time = time.time()
    solution_1, solution_2 = solve_day_03_2021("input.txt")
    end_time = time.time()

    # Calculate execution time in milliseconds
    execution_time: int = int((end_time - start_time) * 1000)

    # Print results in a formatted table (using rich)
    print_day_results(
        "2021", "03",
        str(demo_1), str(demo_2),
        str(solution_1), str(solution_2),
        execution_time
    )
