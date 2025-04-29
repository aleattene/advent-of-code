from utils.file_utils import get_input_file_path, read_input_file


def walk_keypad(
        keypad: list[list[str]],
        start_position: tuple[int, int],
        sequence_buttons: list[str],
        blocker: str = "_") -> str:

    # Define the movement directions (up, down, left, right)
    directions_map = {
        "U": (-1, 0),
        "D": (1, 0),
        "L": (0, -1),
        "R": (0, 1),
    }

    last_row_index = len(keypad) - 1
    last_col_index = len(keypad[0]) - 1

    row, col = start_position
    code = ""

    for buttons in sequence_buttons:
        for move in buttons:

            # Identify the direction to move (row and column)
            direction_y, direction_x = directions_map[move]
            new_row, new_col = row + direction_y, col + direction_x

            # Check if the new position is within bounds and not a blocker
            if (
                    0 <= new_row <= last_row_index
                    and 0 <= new_col <= last_col_index
                    and keypad[new_row][new_col] != blocker
            ):
                row, col = new_row, new_col

        # Append the button at the current position to the code
        code += keypad[row][col]

    return code


def solve_day_02_2016(filename: str) -> tuple[str, str] | str:
    try:
        # Create the absolute path of the input file
        input_file_path = get_input_file_path(__file__, filename)
        # Read the input file
        data = read_input_file(input_file_path)
    except Exception as error:
        return f"Error: {error}"

    # Keypad for part 1 (3x3 grid without blockers)
    keypad_1 = [
        ["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"]
    ]
    # Keypad for part 2 (5x5 grid with blockers)
    keypad_2 = [
        ["_", "_", "1", "_", "_"],
        ["_", "2", "3", "4", "_"],
        ["5", "6", "7", "8", "9"],
        ["_", "A", "B", "C", "_"],
        ["_", "_", "D", "_", "_"]
    ]

    # Define the initial positions for both keypads
    start_position_1 = (1, 1)
    start_position_2 = (2, 0)

    # For each keypad, walk through the sequence of buttons and identify the code
    code_1 = walk_keypad(keypad_1, start_position_1, data)
    code_2 = walk_keypad(keypad_2, start_position_2, data)

    # Return the codes for both keypads
    return code_1, code_2
