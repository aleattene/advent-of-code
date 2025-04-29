from utils.file_utils import get_input_file_path, read_input_file


def parse_row(line: str) -> list[int]:
    """ Parse a row of integers from a string. For example, '5 10 25' becomes [5, 10, 25]."""
    return list(map(int, line.split()))


def is_valid_triangle(sides: list[int]) -> bool:
    """Check if the given sides can form a valid triangle."""
    side_1, side_2, side_3 = sorted(sides)
    return side_1 + side_2 > side_3


def solve_day_03_2016(filename: str) -> tuple[int, int] | str:
    """Solution for Advent of Code 2016, Day 3: Squares with Three Sides."""
    try:
        # Create the absolute path of the input file
        input_file_path = get_input_file_path(__file__, filename)
        # Read the input file
        data = read_input_file(input_file_path)
    except Exception as error:
        return f"Error: {error}"

    # Parse the input data to extract the triangle sides
    matrix = [parse_row(line) for line in data]

    # Count the number of valid triangles in the original matrix
    valid_triangles = sum(1 for sides in matrix if is_valid_triangle(sides))

    # Count the number of valid triangles in the transposed matrix (3 rows at a time)
    valid_triangles_transposed_matrix = 0
    for i in range(0, len(matrix), 3):
        triangles = [parse_row(row) for row in data[i:i + 3]]
        # Transpose the sides of the triangles using the zip function
        for transposed_sides in zip(*triangles):
            if is_valid_triangle(transposed_sides):
                valid_triangles_transposed_matrix += 1

    # Return the results as a tuple
    return valid_triangles, valid_triangles_transposed_matrix
