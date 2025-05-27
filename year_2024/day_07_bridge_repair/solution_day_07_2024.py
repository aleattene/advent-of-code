from itertools import product
from utils.file_utils import get_input_file_path, read_input_file


def evaluate_left_to_right_expression(numbers: list[int], operators: list[str]) -> int:
    """
    Evaluate an expression respecting left-to-right precedence.
    """
    result: int = numbers[0]
    for i, operator in enumerate(operators):
        match operator:
            case '+':
                result += numbers[i + 1]
            case '*':
                result *= numbers[i + 1]
            case '||':
                result = int(str(result) + str(numbers[i + 1]))
    return result


def evaluate_value_combination(numbers: list[int], value: int, operators: list[str]) -> int:
    """
    Evaluate all combinations of numbers with the specified operators,
    respecting left-to-right precedence, and check if any equals the target value.
    """
    # Check if the list of numbers contains only one element and if it equals the target value
    if len(numbers) < 2:
        return numbers[0] == value

    # Generate all combinations of the specified operators
    operator_combinations = product(operators, repeat=len(numbers) - 1)

    # Check each combination
    for operator in operator_combinations:
        result: int = evaluate_left_to_right_expression(numbers, operator)
        if result == value:
            return value

    # If no combination is found, return 0
    return 0


def solve_day_07_2024(filename: str) -> tuple[int, int]:
    """
    Solution of the Advent of Code 2024 Day 07 - Bridge Repair.
    Note: The solution can be improved, actually the time of execution is approximately 10 seconds.
    :param filename: The name file containing the input data.
    :return: A tuple containing the number of occurrences of the Xmas patterns (part 1) and
                the number of occurrences of the cross patterns (part 2).
    """
    try:
        # Create the absolute path of the input file
        input_file_path = get_input_file_path(__file__, filename)
        # Read the input file
        data = read_input_file(input_file_path)
    except Exception as error:
        raise RuntimeError(f"Error: {error}")

    # Initialize the calibration results and the operators for the two parts
    calibration_result: int = 0
    operators_part_one: list[str] = ['+', '*']
    calibration_result_with_concat: int = 0
    operators_part_two: list[str] = operators_part_one + ['||']

    for line in data:
        # Split the line into the value and the list of numbers
        value, numbers = line.split(":")
        value: int = int(value)
        numbers: list[int] = list(map(int, numbers.split()))

        # Calculate if exists a combination of numbers that equals the target value
        result: int = evaluate_value_combination(numbers, value, operators_part_one)
        if result != 0:
            calibration_result += result
        else:
            # If no combination is found, try also with the concatenation operator
            calibration_result_with_concat += evaluate_value_combination(numbers, value, operators_part_two)

    # Add the results of the initial calibration to the calibration result with concatenation
    calibration_result_with_concat += calibration_result

    return calibration_result, calibration_result_with_concat


if __name__ == "__main__":
    # Import function to print results
    import time
    from utils.file_utils import print_day_results

    # Calculate results for demo and real input files
    demo_1, demo_2 = solve_day_07_2024("input_demo.txt")
    start_time = time.time()
    solution_1, solution_2 = solve_day_07_2024("input.txt")
    end_time = time.time()

    # Calculate execution time in milliseconds
    execution_time: int = int((end_time - start_time) * 1000)

    # Print results in a formatted table (using rich)
    print_day_results(
        "2024", "07",
        str(demo_1), str(demo_2),
        str(solution_1), str(solution_2),
        execution_time
    )