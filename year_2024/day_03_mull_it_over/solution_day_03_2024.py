import re
from itertools import zip_longest
from utils.file_utils import get_input_file_path, read_input_file


def solve_day_03_2024(filename: str) -> tuple[int, int]:
    """
    Solution of the Advent of Code 2024 Day 03 - Mull It Over.
    :param filename: The name file containing the input data.
    :return: A tuple containing the total sum of all mul(num1,num2) matches (part 1) and
                the total sum of mul(num1,num2) matches that are preceded by do() (part 2).
    """
    try:
        # Create the absolute path of the input file
        input_file_path = get_input_file_path(__file__, filename)
        # Read the input file
        data = read_input_file(input_file_path)
    except Exception as error:
        raise RuntimeError(f"Error: {error}")

    # Initialize the total sum that considers all matches of mul(num1,num2) function
    total_mul_sum: int = 0
    # Initialize the total sum that considers all matches of do() and mul(num1,num2) functions
    total_do_mul_sum: int = 0

    # Join the data into a single string
    input_string: str = "".join(data)

    # Split the input string into segments based on the do() and don't() delimiters
    segments: list[str] = re.split(r"do\(\)|don't\(\)", input_string)
    delimiters: list[str] = re.findall(r"do\(\)|don't\(\)", input_string)
    # # Add do() at the beginning to treat the first segment as active
    delimiters.insert(0, "do()")

    # Define the pattern to match the mul(num1,num2) function
    mul_pattern: str = r"mul\((\d{1,3}),(\d{1,3})\)"

    # Iterate through each segment and delimiter
    for segment, delimiter in zip_longest(segments, delimiters, fillvalue="don't()"):
        # Find all matches of mul(num1, num2) in the segment
        matches: list[str] = re.findall(mul_pattern, segment)
        # Iterate through each match
        for match in matches:
            num1, num2 = map(int, match)
            # Calculate the product of the two numbers in the match (part one)
            total_mul_sum += num1 * num2
            # Check if the delimiter is do() and calculate the product of the two numbers in the match (part two)
            if delimiter == "do()":
                total_do_mul_sum += num1 * num2

    return total_mul_sum, total_do_mul_sum


if __name__ == "__main__":
    # Import function to print results
    import time
    from utils.file_utils import print_day_results

    # Calculate results for demo and real input files
    demo_1, demo_2 = solve_day_03_2024("input_demo.txt")
    start_time = time.time()
    solution_1, solution_2 = solve_day_03_2024("input.txt")
    end_time = time.time()

    # Calculate execution time in milliseconds
    execution_time: int = int((end_time - start_time) * 1000)

    # Print results in a formatted table (using rich)
    print_day_results(
        "2024", "03",
        str(demo_1), str(demo_2),
        str(solution_1), str(solution_2),
        execution_time
    )
