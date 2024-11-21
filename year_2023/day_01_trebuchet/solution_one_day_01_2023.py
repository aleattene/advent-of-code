def read_input_file(filename: str) -> list[str]:
    """Read the input file and return a list of lines."""
    try:
        # Open the file and read the data using the utf-8 encoding
        with open(filename, 'r', encoding='utf-8') as f:
            return f.read().splitlines()
    except Exception as error:
        raise RuntimeError(f"Error reading the file: {error}")


def find_first_and_last_digit(word: str) -> tuple[str, str]:
    """Find the first and last digit in the word."""
    first_digit = next((char for char in word if char.isdigit()), '0')
    last_digit = next((char for char in reversed(word) if char.isdigit()), '0')
    return first_digit, last_digit


def solve_day_01_2023_one(filename: str) -> int | str:

    try:
        data = read_input_file(filename)
    except Exception as error:
        return f"Error: {error}"

    calibration_sum = 0
    for line in data:
        # Find the first and last digit of the line
        first_digit, last_digit = find_first_and_last_digit(line)
        # Add the sum of the first and last digit to the calibration_sum
        try:
            calibration_sum += int(first_digit + last_digit)
        except ValueError:
            return f"Error: Invalid number format in line: {line}"
    return calibration_sum
