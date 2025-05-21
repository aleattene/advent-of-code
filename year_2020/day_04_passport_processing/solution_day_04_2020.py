from typing import Callable
from utils.file_utils import get_input_file_path

def is_valid_field_byr(value: str) -> bool:
    """
    Check if the birth year is valid (between 1920 and 2002).
    :param value: The value of the field.
    :return: True if valid, False otherwise.
    """
    try:
        return 1920 <= int(value) <= 2002
    except ValueError:
        return False

def is_valid_field_iyr(value: str) -> bool:
    """
    Check if the issue year is valid (between 2010 and 2020).
    :param value: The value of the field.
    :return: True if valid, False otherwise.
    """
    try:
        return 2010 <= int(value) <= 2020
    except ValueError:
        return False

def is_valid_field_eyr(value: str) -> bool:
    """
    Check if the expiration year is valid (between 2020 and 2030).
    :param value: The value of the field.
    :return: True if valid, False otherwise.
    """
    try:
        return 2020 <= int(value) <= 2030
    except ValueError:
        return False

def is_valid_field_hgt(value: str) -> bool:
    """
    Check if the height is valid (in cm or in).
    :param value: The value of the field.
    :return: True if valid, False otherwise.
    """
    try:
        if value.endswith("cm"):
            return 150 <= int(value[:-2]) <= 193
        elif value.endswith("in"):
            return 59 <= int(value[:-2]) <= 76
        else:
            return False
    except ValueError:
        return False

def is_valid_field_hcl(value: str) -> bool:
    """
    Check if the hair color is valid (matches the regex pattern).
    :param value: The value of the field.
    :return: True if valid, False otherwise.
    """
    import re
    return bool(re.match(r"^#[0-9a-f]{6}$", value))

def is_valid_field_ecl(value: str) -> bool:
    """
    Check if the eye color is one of the allowed values.
    :param value: The value of the field.
    :return: True if valid, False otherwise.
    """
    return value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

def is_valid_field_pid(value: str) -> bool:
    """
    Check if the passport ID has a valid format (9 digits including leading zeros).
    :param value: The value of the field.
    :return: True if valid, False otherwise.
    """
    import re
    return bool(re.match(r"^\d{9}$", value))


def solve_day_04_2020(filename: str) -> tuple[int, int]:
    """
    Solution of the Advent of Code 2020 Day 04 - Passport Processing.
    :param filename: The name file containing the input data.
    :return: A tuple containing the number of valid passports containing all required fields (part 1) and
            the number of valid passports with all required fields and valid values (part 2).
    """
    try:
        # Create the absolute path of the input file
        input_file_path = get_input_file_path(__file__, filename)
        with open(input_file_path, 'r', encoding='utf-8') as f:
            # Read the input file
            data = f.read().split("\n\n")
    except Exception as error:
        raise RuntimeError(f"Error: {error}")

    # Define the required fields for a valid passport (part 1)
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

    # Define a dictionary of field validators (part 2)
    validator = Callable[[str], bool]
    field_validators: dict[str, validator] = {
        'byr': is_valid_field_byr,
        'iyr': is_valid_field_iyr,
        'eyr': is_valid_field_eyr,
        'hgt': is_valid_field_hgt,
        'hcl': is_valid_field_hcl,
        'ecl': is_valid_field_ecl,
        'pid': is_valid_field_pid,
        'cid': lambda x: True
    }

    # Initialize the number of valid passports for both parts
    valid_passports_1 = 0
    valid_passports_2 = 0

    # Iterate through each passport in the input data
    for passport in data:
        fields = passport.replace("\n", " ").split(" ")

        # Check if all required fields are present (part 1)
        if all(field in passport for field in required_fields):
            valid_passports_1 += 1

            # If all required fields are present, check also if they are valid (part 2)
            if all(field_validators[field[:3]](field[4:]) for field in fields):
                valid_passports_2 += 1

    # Return the number of valid passports for both parts
    return valid_passports_1, valid_passports_2



if __name__ == "__main__":
    # Import function to print results
    import time
    from utils.file_utils import print_day_results

    # Calculate results for demo and real input files
    demo_1, demo_2 = solve_day_04_2020("input_demo.txt")
    start_time = time.time()
    solution_1, solution_2 = solve_day_04_2020("input.txt")
    end_time = time.time()

    # Calculate execution time in milliseconds
    execution_time = int((end_time - start_time) * 1000)

    # Print results in a formatted table (using rich)
    print_day_results(
        "2020", "04",
        str(demo_1), str(demo_2),
        str(solution_1), str(solution_2),
        execution_time
    )
