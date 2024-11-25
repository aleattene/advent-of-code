from utils.file_utils import get_input_file_path, read_input_file


def parse_line(line: str) -> tuple[int, list[tuple[int, str]]]:
    """Parse a line of input and return the game ID and the subsets as tuples of numbers and colors."""
    id_part, subsets_part = line.split(":")
    game_id = int(id_part.replace("Game ", ""))
    subsets = []

    for subset in subsets_part.split(";"):
        values = subset.strip().split(",")
        for value in values:
            parts = value.strip().split(" ")
            num = int(parts[0])
            color = parts[1]
            subsets.append((num, color))

    return game_id, subsets


def is_subset_valid(subsets: list[tuple[int, str]], possibilities: dict[str, int]) -> bool:
    """Check if all subsets are valid according to the color thresholds."""
    for num, color in subsets:
        max_value = possibilities.get(color, None)
        # If the color is not in the possibilities, the subset is surely invalid
        if max_value is None: return False
        # If the number is greater than the maximum value, the subset is surely invalid
        if num > max_value: return False
    return True


def calculate_power(subsets: list[tuple[int, str]]) -> int:
    """Calculate the total power for the line based on the color values."""
    powers = {"red": 0, "green": 0, "blue": 0}

    for num, color in subsets:
        if color in powers and num > powers[color]:
            powers[color] = num

    return powers["red"] * powers["green"] * powers["blue"]


def solve_day_02_2023(filename: str) -> tuple[int, int] | str:
    """
    Solve day 02 puzzle based on game data from the input file.
    """
    possibilities = {"red": 12, "green": 13, "blue": 14}

    try:
        # Create the absolute path of the input file
        input_file_path = get_input_file_path(__file__, filename)
        # Read the input file
        data = read_input_file(input_file_path)

        sum_ids = 0
        total_power = 0
        for line in data:
            # Part One
            game_id, subsets = parse_line(line)
            if is_subset_valid(subsets, possibilities):
                # If the subsets are valid, add the game ID to the sum
                sum_ids += game_id

            # Part Two
            total_power += calculate_power(subsets)

        return sum_ids, total_power
    except Exception as error:
        return f"Error: {error}"
