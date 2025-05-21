from utils.file_utils import get_input_file_path

def get_row_from_boarding_card(boarding_card: str) -> int:
    """
    Get the row number from the boarding card.
    :param boarding_card: The boarding card string.
    :return: The row number.
    """
    binary_row: str = boarding_card[:7].replace('F', '0').replace('B', '1')
    return int(binary_row, 2)

def get_column_from_boarding_card(boarding_card: str) -> int:
    """
    Get the column number from the boarding card.
    :param boarding_card: The boarding card string.
    :return: The column number.
    """
    binary_column: str = boarding_card[7:].replace('L', '0').replace('R', '1')
    return int(binary_column, 2)


def solve_day_05_2020(filename: str) -> tuple[int, int | None]:
    """
    Solution of the Advent of Code 2020 Day 05 - Binary Boarding.
    :param filename: The name file containing the input data.
    :return: A tuple containing the maximum seat ID (part 1) and the missing seat ID (part 2).
    """
    try:
        # Create the absolute path of the input file
        input_file_path = get_input_file_path(__file__, filename)
        with open(input_file_path, 'r', encoding='utf-8') as f:
            # Read the input file
            data = f.read().split("\n")
    except Exception as error:
        raise RuntimeError(f"Error: {error}")

    # Initialize a list to store seat IDs
    seat_ids: list[int] = []

    # Iterate through each boarding card in the input data
    for boarding_card in data:
        row: int = get_row_from_boarding_card(boarding_card)
        column: int = get_column_from_boarding_card(boarding_card)

        # Calculate the seat ID and append it to the list of seat IDs
        seat_id: int = column + (row * 8)
        seat_ids.append(seat_id)

    # Sort the seat IDs to find the missing seat ID
    seat_ids.sort()
    missing_seat_id: None = None
    for seat in range(1, len(seat_ids)):
        prev: int = seat_ids[seat - 1]
        current: int = seat_ids[seat]
        # If the difference between consecutive seat IDs is 2 then the missing seat ID is the previous one
        if current - prev == 2:
            missing_seat_id: int = current - 1
            break

    # Return the maximum seat ID and the missing seat ID
    return max(seat_ids), missing_seat_id


if __name__ == "__main__":
    # Import function to print results
    import time
    from utils.file_utils import print_day_results

    # Calculate results for demo and real input files
    demo_1, demo_2 = solve_day_05_2020("input_demo.txt")
    start_time = time.time()
    solution_1, solution_2 = solve_day_05_2020("input.txt")
    end_time = time.time()

    # Calculate execution time in milliseconds
    execution_time: int = int((end_time - start_time) * 1000)

    # Print results in a formatted table (using rich)
    print_day_results(
        "2020", "05",
        str(demo_1), str(demo_2),
        str(solution_1), str(solution_2),
        execution_time
    )
