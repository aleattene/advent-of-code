from utils.file_utils import get_input_file_path, read_input_file


def is_within_bounds(map_data, row, col):
    """Check if the given (row, col) is within the bounds of the map."""
    return 0 <= row < len(map_data) and 0 <= col < len(map_data[0])


def is_valid_neighbour(map_data, row, col):
    """Check if the given (row, col) is a valid neighbour for the current position."""
    return is_within_bounds(map_data, row, col) and isinstance(map_data[row][col], int)


def find_symbol_neighbours(map_data, row, col):
    """Find neighbours of a given position (row, col) in the map."""
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    neighbours_coordinates = [
        (row + dir_row, col + dir_col)
        for dir_row, dir_col in directions
        if is_valid_neighbour(map_data, row + dir_row, col + dir_col)
    ]

    return neighbours_coordinates


def parse_map(data: list[str]) -> list[list[int | str]]:
    """Parse the input data into a map with integers and symbols."""
    map_data = []
    for row in data:
        map_row = [int(value) if value.isdigit() else value for value in row]
        map_data.append(map_row)
    return map_data


def extract_neighbour_values(
        map_data: list[list[int | str]],
        neighbours_coordinates: list[tuple[int, int]]
        ) -> list[int]:
    """Extract and construct numerical values from neighbours."""
    neighbours_values = set()

    for i_row, i_col in neighbours_coordinates:
        number = str(map_data[i_row][i_col])

        # Append digits to the right
        for i in range(i_col + 1, len(map_data[i_row])):
            if not str(map_data[i_row][i]).isdigit():
                break
            number += str(map_data[i_row][i])

        # Prepend digits to the left
        for i in range(i_col - 1, -1, -1):
            if not str(map_data[i_row][i]).isdigit():
                break
            number = str(map_data[i_row][i]) + number

        neighbours_values.add(int(number))

    return list(neighbours_values)


def calculate_energy_and_power(neighbours_values: list[int]) -> tuple[int, int]:
    """Calculate the energy and power based on the neighbours' values."""
    if len(neighbours_values) == 1:
        return neighbours_values[0], 0
    elif len(neighbours_values) == 2:
        return neighbours_values[0] + neighbours_values[1], neighbours_values[0] * neighbours_values[1]
    return 0, 0


def solve_day_03_2023(filename: str) -> tuple[int, int] | str:
    """Solve day 03 puzzle based on the map data from the input file."""
    try:
        # Create the absolute path of the input file
        input_file_path = get_input_file_path(__file__, filename)
        # Read the input file
        data = read_input_file(input_file_path)

        map_data = parse_map(data)

        sum_energy = 0
        sum_power = 0

        # Process the map
        for row_idx in range(len(map_data)):
            for col_idx in range(len(map_data[row_idx])):
                value = map_data[row_idx][col_idx]

                # Check if the value is a symbol
                if not str(value).isdigit() and value != ".":
                    # Find the neighbours of the current symbol
                    symbol_neighbours_coordinates = find_symbol_neighbours(map_data, row_idx, col_idx)

                    # Extract neighbour values
                    neighbours_values = extract_neighbour_values(map_data, symbol_neighbours_coordinates)

                    # Calculate energy and power based on the neighbours' values
                    energy, power = calculate_energy_and_power(neighbours_values)
                    sum_energy += energy
                    sum_power += power

        return sum_energy, sum_power

    except Exception as error:
        return f"Error: {error}"

