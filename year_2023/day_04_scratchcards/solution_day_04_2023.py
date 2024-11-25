from utils.file_utils import get_input_file_path, read_input_file


def parse_row(row: str, idx_row: int) -> tuple[int, list[str], list[str]]:
    """Parse a row to extract card number, winners, and my numbers."""
    all_values = row.split("|")
    num_card = idx_row + 1
    winners = all_values[0].split(":")[1].strip().split()
    my_numbers = all_values[1].strip().split()
    return num_card, winners, my_numbers


def update_scratchcards(scratchcards: dict[int, int], num_card: int, count: int):
    """Update the scratchcards based on the number of matches found."""
    repeat = scratchcards.get(num_card, 0)
    if count:
        repeat += 1

    for _ in range(repeat):
        for win_card in range(1, count + 1):
            new_card = num_card + win_card
            scratchcards[new_card] = scratchcards.get(new_card, 0) + 1

    scratchcards[num_card] = scratchcards.get(num_card, 0) + 1


def calculate_points(count: int) -> int:
    """Calculate points based on the number of matches."""
    if count - 1 >= 0:
        return 2 ** (count - 1)
    return 0


def solve_day_04_2023(filename: str) -> tuple[int, int] | str:
    try:
        # Create the absolute path of the input file
        input_file_path = get_input_file_path(__file__, filename)
        # Read the input file
        data = read_input_file(input_file_path)

        total_points = 0
        scratchcards = {}

        # Process each row
        for idx_row, row in enumerate(data):
            num_card, winners, my_numbers = parse_row(row, idx_row)

            # Count how many of my numbers are in the winners list
            count = sum(1 for number in my_numbers if number in winners)

            # Update scratchcards based on the matches found
            update_scratchcards(scratchcards, num_card, count)

            # Calculate the points and add to the total
            total_points += calculate_points(count)

        # Calculate the sum of all scratchcards
        sum_scratchcards = sum(scratchcards.values())

        return total_points, sum_scratchcards

    except Exception as error:
        return f"Error: {error}"
