def solve_day_01_2023_one(filename: str) -> int | str:
    calibration_sum = 0
    try:
        # Open the file and read the data using the utf-8 encoding
        with open(filename, 'r', encoding='utf-8') as f:
            # Iterate over each line in the data and extract the numbers
            for line in f:
                first_digit = None
                last_digit = None

                # We call the enumerate function only once for each line, not for each character
                enumerated_line = enumerate(line)
                for i, char in enumerated_line:

                    # Found first digit
                    if first_digit is None and char.isdigit():
                        first_digit = char

                    # Found last digit
                    if last_digit is None and line[-(i + 1)].isdigit():
                        last_digit = line[-(i + 1)]

                    # If we found the first and last digit, we can break the loop
                    if first_digit and last_digit:
                        calibration_sum += int(first_digit + last_digit)
                        break

        return calibration_sum
    except Exception as error:
        return "Error: {}".format(str(error).replace('\n', ''))
