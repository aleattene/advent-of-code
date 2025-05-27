from itertools import combinations
from utils.file_utils import get_input_file_path, read_input_file


def elements_to_coordinates(grid: list[str]) -> dict[str, list[tuple[int, int]]]:
    """Converts a grid of elements to a dictionary of coordinates."""
    grid_coordinates = {}
    for i_row, row in enumerate(grid):
        for i_col, char in enumerate(row):
            if char != '.':
                # If the key does not exist, create it with an empty list otherwise append the coordinates
                grid_coordinates.setdefault(char, []).append((i_row, i_col))
    return grid_coordinates


def generate_antinodes(initial_coord: tuple[int, int], direction: int, diff: tuple[int, int], rows: int, cols: int
                       ) -> tuple[int, int] | None:
    """Generate a single antinode based on the difference and direction."""
    new_row = initial_coord[0] + direction * diff[0]
    new_col = initial_coord[1] + direction * diff[1]
    # Check if the new coordinates are within the grid otherwise return None
    if 0 <= new_row < rows and 0 <= new_col < cols:
        return new_row, new_col
    return None


def generate_iterative_antinodes(initial_coord: tuple[int, int], direction: int, diff: tuple[int, int], rows: int,
                                 cols: int) -> list[tuple[int, int]]:
    """Generate iterative antinodes starting from an initial coordinate."""
    current_row, current_col = initial_coord
    generated_antinodes = []
    while True:
        current_row += direction * diff[0]
        current_col += direction * diff[1]
        # Check if the new coordinates are within the grid otherwise break the loop
        if not (0 <= current_row < rows and 0 <= current_col < cols):
            break
        generated_antinodes.append((current_row, current_col))
    return generated_antinodes


def solve_day_08_2024(filename: str) -> tuple[int, int] | str:
    """Solutions for Day 08 of AoC 2024."""
    try:
        # Create the absolute path of the input file
        input_file_path = get_input_file_path(__file__, filename)
        # Read the input file
        data = read_input_file(input_file_path)
    except Exception as error:
        raise RuntimeError(f"Error: {error}")

    # Grid dimensions and antennas coordinates
    rows, cols = len(data), len(data[0])
    antennas_coordinates = elements_to_coordinates(data)

    # Initialize dictionaries to store antinodes coordinates (part one and part two)
    antinodes_coordinates = {}
    antinodes_iteratively_coordinates = {}

    for key, coordinates in antennas_coordinates.items():
        new_key = key.swapcase()
        antinodes_coordinates[new_key] = []

        # Iterate through all possible pairs of coordinates
        for coord1, coord2 in combinations(coordinates, 2):
            diff = (coord2[0] - coord1[0], coord2[1] - coord1[1])

            # Iterate through both directions (positive and negative) to generate antinodes
            for initial_coord, direction in [(coord1, -1), (coord2, 1)]:
                # Generate a single pair of antinodes (part one)
                new_antinodes = generate_antinodes(initial_coord, direction, diff, rows, cols)
                if new_antinodes is not None:
                    antinodes_coordinates.setdefault(new_key, []).append(new_antinodes)
                # Generate iterative antinodes (part two)
                new_iterative_antinodes = generate_iterative_antinodes(initial_coord, direction, diff, rows, cols)
                antinodes_iteratively_coordinates.setdefault(new_key, []).extend(new_iterative_antinodes)

    # Set of unique antinodes coordinates (part one)
    unique_antinodes_coordinates = {
        coord for coords in antinodes_coordinates.values() for coord in coords
    }
    # Set of unique iterative antinodes coordinates (part two)
    unique_antinodes_iteratively_coordinates = {
        coord for coords in antinodes_iteratively_coordinates.values() for coord in coords
    }
    unique_antinodes_iteratively_coordinates.update(
        {coord for coords in antennas_coordinates.values() for coord in coords}
    )

    return len(unique_antinodes_coordinates), len(unique_antinodes_iteratively_coordinates)
