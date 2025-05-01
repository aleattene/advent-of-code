import itertools
from utils.file_utils import get_input_file_path, read_input_file


def solve_day_01_2018(filename: str) -> tuple[int, int] | str:
    """
    Solve the Advent of Code 2018 Day 01 - Chronal Calibration.
    :param filename: The name of the input file containing the frequency changes.
    :return: Sum of all frequency changes (part 1) and the first frequency reached twice (part 2).
    """
    try:
        # Create the absolute path of the input file
        input_file_path = get_input_file_path(__file__, filename)
        # Read the input file
        data = read_input_file(input_file_path)
    except Exception as error:
        return f"Error: {error}"

    # Convert the input data (list of strings) to a list of integers
    sequence_changes = [int(x) for x in data]

    # Calculate the total frequency change (part 1)
    frequency = sum(sequence_changes)

    # Initialize variables for part 2 (set to track frequencies and current frequency for each iteration)
    seen_frequencies = {0}
    current_frequency = 0
    first_repeated_frequency = None

    # Find the first repeated frequency (part 2) using a cycle to iterate recursively through the changes
    for change in itertools.cycle(sequence_changes):
        current_frequency += change
        if current_frequency in seen_frequencies:
            first_repeated_frequency = current_frequency
            break
        seen_frequencies.add(current_frequency)

    return frequency, first_repeated_frequency


if __name__ == "__main__":

    # Import function to print results
    from utils.file_utils import print_day_results

    # Calculate results for demo and real input files
    demo_1, demo_2 = solve_day_01_2018("input_demo.txt")
    solution_1, solution_2 = solve_day_01_2018("input.txt")

    # Print results in a formatted table (using rich)
    print_day_results(
        "2018", "01",
        str(demo_1), str(demo_2),
        str(solution_1), str(solution_2)
    )
