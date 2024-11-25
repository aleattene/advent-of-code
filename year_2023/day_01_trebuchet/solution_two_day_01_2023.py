from utils.file_utils import get_input_file_path, read_input_file


def find_all_matches(line: str, verbose_to_numbers: dict[str, int]) -> list[tuple[int, str]]:
    """Find all numeric and verbose matches in the line and return a sorted list of matches."""
    import re
    matches = []
    # Found all the matches for the digits and add to the matches list
    for match in re.finditer(r'\d', line):
        matches.append((match.start(), match.group()))
    # Found all the matches for the verbose numbers and add to the matches list
    for key, value in verbose_to_numbers.items():
        for match in re.finditer(key, line):
            matches.append((match.start(), str(value)))
    # Sort the matches list by the first element of each tuple (using a lambda/anonymous function)
    matches.sort(key=lambda elem: elem[0])
    return matches


def solve_day_01_2023_two(filename: str) -> int | str:
    """Solve the second part of the puzzle."""
    verbose_to_numbers = {
        'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9,
    }
    try:
        # Create the absolute path of the input file
        input_file_path = get_input_file_path(__file__, filename)
        # Read the input file
        data = read_input_file(input_file_path)
    except Exception as error:
        return f"Error: {error}"

    calibration_sum = 0
    for line in data:
        # First digit is the first element of the first tuple
        first_digit = find_all_matches(line, verbose_to_numbers)[0][1]

        # Last digit is the second element of the last tuple
        last_digit = find_all_matches(line, verbose_to_numbers)[-1][1]

        try:
            calibration_sum += int(first_digit + last_digit)
        except ValueError:
            return f"Error: Invalid number format in line: {line}"
    return calibration_sum
