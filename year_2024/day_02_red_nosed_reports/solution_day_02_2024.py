from utils.file_utils import get_input_file_path, read_input_file


def is_safe_levels(current_level: int, next_level: int) -> bool:
    """Check if the difference between levels is within safe range (1 to 3)."""
    return 1 <= abs(next_level - current_level) <= 3


def is_report_increasing(current_level: int, next_level: int) -> bool:
    """Check if the next level is greater than the current level."""
    return next_level > current_level


def is_report_safe(levels: list[int]) -> bool:
    """Check if the sequence of levels is safe (all differences are within range and all directions are consistent)."""
    directions: list[bool] = []
    safety: list[bool] = []
    for i in range(len(levels) - 1):
        is_level_increasing: bool = is_report_increasing(levels[i], levels[i + 1])
        directions.append(is_level_increasing)
        is_level_safe: bool = is_safe_levels(levels[i], levels[i + 1])
        safety.append(is_level_safe)

    # Check if the entire sequence (report) is either consistently increasing or decreasing
    if all(directions) or all(not direction for direction in directions):
        return all(safety)
    return False


def solve_day_02_2024(filename: str) -> tuple[int, int]:
    """
    Solution of the Advent of Code 2024 Day 02 - Red-Nosed Reports.
    :param filename: The name file containing the input data.
    :return: A tuple with two integers:
                - The number of safe reports (solution 1).
                - The number of safe reports with one modification allowed (solution 2).
    """
    try:
        # Create the absolute path of the input file
        input_file_path = get_input_file_path(__file__, filename)
        # Read the input file
        data = read_input_file(input_file_path)
    except Exception as error:
        raise RuntimeError(f"Error: {error}")

    # Initialize the counters (solution 1 and 2)
    safe_reports: int = 0
    safe_reports_with_tolerance: int = 0

    # Iterate through each line in the input data
    for line in data:
        # Parse the levels from the line and convert chars to integers
        levels: list[int] = list(map(int, line.split()))

        # Check if the sequence (report) is already safe (no need to modify to check tolerance for eventual safety)
        if is_report_safe(levels):
            safe_reports += 1
        else:
            # Try to modify one element to see if the report becomes safe
            safe_report_with_tolerance = False
            for i in range(len(levels)):
                # Create a copy of the levels list without the current element
                modified_levels: list[int] = levels[:i] + levels[i + 1:]

                # Check if the modified sequence (report) is safe
                if is_report_safe(modified_levels):
                    safe_report_with_tolerance = True
                    break

            # Increment the counters based on the result of the tolerance check (solution two)
            if safe_report_with_tolerance:
                safe_reports_with_tolerance += 1

    return safe_reports, safe_reports + safe_reports_with_tolerance


if __name__ == "__main__":
    # Import function to print results
    import time
    from utils.file_utils import print_day_results

    # Calculate results for demo and real input files
    demo_1, demo_2 = solve_day_02_2024("input_demo.txt")
    start_time = time.time()
    solution_1, solution_2 = solve_day_02_2024("input.txt")
    end_time = time.time()

    # Calculate execution time in milliseconds
    execution_time: int = int((end_time - start_time) * 1000)

    # Print results in a formatted table (using rich)
    print_day_results(
        "2024", "02",
        str(demo_1), str(demo_2),
        str(solution_1), str(solution_2),
        execution_time
    )