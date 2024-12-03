import re
from itertools import zip_longest
from utils.file_utils import get_input_file_path, read_input_file


def solve_day_03_2024(filename: str) -> tuple[int, int] | str:
    """Solutions for Day 03 of AoC 2024."""
    try:
        # Create the absolute path of the input file
        input_file_path = get_input_file_path(__file__, filename)
        # Read the input file
        data = read_input_file(input_file_path)
    except Exception as error:
        return f"Error: {error}"

    # Initialize the total sum that considers all matches of mul(num1,num2) function
    total_mul_sum = 0
    # Initialize the total sum that considers all matches of do() and mul(num1,num2) functions
    total_do_mul_sum = 0

    # Join the data into a single string
    input_string = "".join(data)

    # Split the input string into segments based on the do() and don't() delimiters
    segments = re.split(r"do\(\)|don't\(\)", input_string)
    delimiters = re.findall(r"do\(\)|don't\(\)", input_string)
    # # Add do() at the beginning to treat the first segment as active
    delimiters.insert(0, "do()")

    # Define the pattern to match the mul(num1,num2) function
    mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

    # Iterate through each segment and delimiter
    for segment, delimiter in zip_longest(segments, delimiters, fillvalue="don't()"):
        # Find all matches of mul(num1, num2) in the segment
        matches = re.findall(mul_pattern, segment)
        # Iterate through each match
        for match in matches:
            num1, num2 = map(int, match)
            # Calculate the product of the two numbers in the match (part one)
            total_mul_sum += num1 * num2
            # Check if the delimiter is do() and calculate the product of the two numbers in the match (part two)
            if delimiter == "do()":
                total_do_mul_sum += num1 * num2

    return total_mul_sum, total_do_mul_sum
