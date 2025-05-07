from itertools import product
from utils.file_utils import get_input_file_path, read_input_file


def run_program(program: list[int], noun: int, verb: int) -> int | None:
    """
    Run the program with the given data.
    :param program: The program to run.
    :param noun: The noun value to set at position 1.
    :param verb: The verb value to set at position 2.
    :return: The first value in the modified program or None if an error occurs.
    """
    # Create a copy of the program to avoid modifying the original
    program_to_run = program.copy()

    # Set Nuon and Verb at positions 1 and 2
    program_to_run[1] = noun
    program_to_run[2] = verb

    # Process the program in chunks of 4 integers
    for i in range(0, len(program_to_run), 4):
        # Using try-except to handle IndexError (part 2)
        try:
            # Identify the operation code as the first integer in the chunk
            op_code = program_to_run[i]
            # Opcode 99: End of the program
            if op_code == 99:
                break
            # Opcode 1: Sum values at positions identified at positions 1 and 2 and store the result at position 3
            elif op_code == 1:
                program_to_run[program_to_run[i + 3]] = (
                        program_to_run[program_to_run[i + 1]] + program_to_run[program_to_run[i + 2]]
                )
            # Opcode 2: Multiply values at positions identified at positions 1 and 2 and store the result at position 3
            else:
                program_to_run[program_to_run[i + 3]] = (
                        program_to_run[program_to_run[i + 1]] * program_to_run[program_to_run[i + 2]]
                )
        # Handle IndexError exception (the noun and verb are not good numbers)
        except IndexError:
            return None
    # Return the first value in the modified program
    return program_to_run[0]


def solve_day_02_2019(filename: str) -> tuple[int, str]:
    """
    Solution of the Advent of Code 2019 Day 02 - 1202 Program Alarm.
    :param filename: The name file containing the input data.
    :return: A tuple containing the first element of the modified program (part 1) and
            the noun-verb string that produce a value of 19690720 of the modified program (part 2).
    """
    try:
        # Create the absolute path of the input file
        input_file_path = get_input_file_path(__file__, filename)
        # Read the input file
        data = read_input_file(input_file_path)[0]
    except Exception as error:
        raise RuntimeError(f"Error: {error}")

    # Split the data into a list of integers
    data = list(map(int, data.split(",")))

    # Part 1: Run the program with noun = 12 and verb = 2 (default values by the problem)
    result_1 = run_program(data, 12, 2)

    # Part 2: Find the values of noun and verb that produce the first element of the modified program equal to 19690720
    expected_result = 19690720

    # Iterate through all possible combinations of noun and verb (0-99)
    for noun, verb in product(range(100), repeat=2):
        result = run_program(data, noun, verb)
        # If the first value of the modified program is equal to 19690720, return the noun and verb string
        if result == expected_result:
            return result_1, f"{noun * 100 + verb}"

    # If no solution is found, return the result of part 1 and a string of 4 zeros
    return result_1, "0000"


if __name__ == "__main__":

    # Import function to print results
    import time
    from utils.file_utils import print_day_results

    # Calculate results for demo and real input files
    demo_1, demo_2 = solve_day_02_2019("input_demo.txt")
    start_time = time.time()
    solution_1, solution_2 = solve_day_02_2019("input.txt")
    end_time = time.time()

    # Calculate execution time in milliseconds
    execution_time = int((end_time - start_time) * 1000)

    # Print results in a formatted table (using rich)
    print_day_results(
        "2019", "02",
        str(demo_1), str(demo_2),
        str(solution_1), str(solution_2),
        execution_time
    )
