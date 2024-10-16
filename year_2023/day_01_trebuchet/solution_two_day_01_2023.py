import re


def solve_day_01_2023_two(filename: str) -> int | str:
    verbose_to_numbers = {
        'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9,
    }
    try:
        calibration_sum = 0
        # Open the file and read the data using the utf-8 encoding
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                matches = []

                # Found all the matches for the digits and add to the matches list
                for match in re.finditer(r'\d', line):
                    matches.append((match.start(), match.group()))

                # Found all the matches for the verbose numbers and add to the matches list
                for key, value in verbose_to_numbers.items():
                    for match in re.finditer(key, line):
                        matches.append((match.start(), str(value)))
                print(matches)
                # Sort the matches list by the first element of each tuple (using a lambda/anonymous function)
                matches.sort(key=lambda elem: elem[0])
                # First digit is the first element of the first tuple
                first_digit = matches[0][1]
                # Last digit is the second element of the last tuple
                last_digit = matches[-1][1]

                calibration_sum += int(first_digit + last_digit)

        return calibration_sum
    except Exception as error:
        return "Error: {}".format(str(error).replace('\n', ''))
