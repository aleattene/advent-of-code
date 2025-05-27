import re
from utils.file_utils import get_input_file_path, read_input_file


def find_occurrences_pattern(string: str, pattern: str) -> int:
    """Find the number of occurrences of a regex pattern in a string."""
    matches: list[str] = []
    for i in range(len(string)):
        match = re.match(pattern, string[i:])
        if match:
            matches.append((match.group(), i))
    return len(matches)


def is_neighbour_pattern_match(matrix: list[str], row: int, col: int, cross_patterns: list[str]) -> bool:
    """Check if both primary and secondary diagonal match the target patterns."""

    # Primary diagonal pattern: (r-1, c-1), (r, c), (r+1, c+1)
    primary_diagonal = matrix[row-1][col-1] + matrix[row][col] + matrix[row+1][col+1]
    if primary_diagonal not in cross_patterns:
        return False

    # Secondary diagonal pattern: (r-1, c+1), (r, c), (r+1, c-1)
    secondary_diagonal = matrix[row-1][col+1] + matrix[row][col] + matrix[row+1][col-1]
    if secondary_diagonal not in cross_patterns:
        return False

    return True


def find_occurrences_cross_pattern(matrix, cross_patterns):
    """Find the number of occurrences of the cross patterns in the matrix."""
    rows: int = len(matrix)
    cols: int = len(matrix[0])
    count_matching_patterns: int = 0

    # Iterate through each cell in the matrix (except the border cells)
    for row in range(1, rows - 1):
        for col in range(1, cols - 1):
            # Check if the current cell is 'A' and the neighbour cells match the target patterns
            if matrix[row][col] == 'A' and is_neighbour_pattern_match(matrix, row, col, cross_patterns):
                count_matching_patterns += 1
    return count_matching_patterns


def create_diagonals_matrix(matrix: list[str]) -> list[str]:
    """Create a list of all diagonals from the given matrix."""
    rows: int = len(matrix)
    cols: int = len(matrix[0])
    diagonals: list[str] = []

    # Helper function to add diagonals
    def add_diagonal(start_row, start_col, delta_row, delta_col):
        """Add a diagonal to the list of diagonals."""
        diagonal = []
        r, c = start_row, start_col
        while 0 <= r < rows and 0 <= c < cols:
            diagonal.append(matrix[r][c])
            r += delta_row
            c += delta_col
        diagonals.append("".join(diagonal))

    # Diagonals from top-left to bottom-right
    for row in range(rows):
        add_diagonal(row, 0, 1, 1)
    for col in range(1, cols):
        add_diagonal(0, col, 1, 1)

    # Diagonals from top-right to bottom-left
    for col in range(cols):
        add_diagonal(0, col, 1, -1)
    for row in range(1, rows):
        add_diagonal(row, cols - 1, 1, -1)

    return diagonals


def solve_day_04_2024(filename: str) -> tuple[int, int]:
    """
    Solution of the Advent of Code 2024 Day 04 - Ceres Search.
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

    xmas_pattern: str = r"XMAS|SAMX"

    # Find the number of occurrences of the Xmas patterns in the matrix (part one)
    occurrences_pattern: int = sum(find_occurrences_pattern(line, xmas_pattern) for line in data)

    cols = ["".join(col) for col in zip(*data)]
    occurrences_pattern += sum(find_occurrences_pattern(col, xmas_pattern) for col in cols)

    diagonals = create_diagonals_matrix(data)
    occurrences_pattern += sum(find_occurrences_pattern(d, xmas_pattern) for d in diagonals if len(d) >= 3)

    # Find the number of occurrences of the target patterns in the matrix (part two)
    cross_patterns: list[str] = ["MAS", "SAM"]
    occurrences_cross_pattern: int = find_occurrences_cross_pattern(data, cross_patterns)

    return occurrences_pattern, occurrences_cross_pattern


if __name__ == "__main__":
    # Import function to print results
    import time
    from utils.file_utils import print_day_results

    # Calculate results for demo and real input files
    demo_1, demo_2 = solve_day_04_2024("input_demo.txt")
    start_time = time.time()
    solution_1, solution_2 = solve_day_04_2024("input.txt")
    end_time = time.time()

    # Calculate execution time in milliseconds
    execution_time: int = int((end_time - start_time) * 1000)

    # Print results in a formatted table (using rich)
    print_day_results(
        "2024", "04",
        str(demo_1), str(demo_2),
        str(solution_1), str(solution_2),
        execution_time
    )
