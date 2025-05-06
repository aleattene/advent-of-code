from utils.file_utils import get_input_file_path, read_input_file


def solve_day_03_2018(filename: str) -> tuple[int, str]:
    """
    Solution of the Advent of Code 2018 Day 03 - No Matter How You Slice It.
    :param filename: The name of the input file containing the room data.
    :return: A tuple containing the number of overlapped coordinates (part 1) and the non overlapped claim ID (part 2).
    """
    try:
        # Create the absolute path of the input file
        input_file_path = get_input_file_path(__file__, filename)
        # Read the input file
        data = read_input_file(input_file_path)
    except Exception as error:
        raise RuntimeError(f"Error: {error}")

    # Initialize a dictionary to store the coordinates and their corresponding occurrences and claim IDs
    coordinate_to_claim_ids: dict[tuple[int, int], list[int | str]] = {}
    # Set to store all claim IDs that do not overlap with any other claim
    no_overlapped_claim_ids: set[str] | int = set()

    for claim in data:
        # Claim Elements expected: [ "#123", "@",  "3,2:", "5x4" ]
        claim_elements: list[str] = claim.split()

        # Extract claim ID from the first element (#123 becomes 123)
        claim_id: str = claim_elements[0][1:]
        no_overlapped_claim_ids.add(claim_id)

        # Extract padding_left, padding_top, width, and height from the claim elements
        padding_left, padding_top = map(int, claim_elements[2][:-1].split(","))
        width,  height = map(int, claim_elements[3].split("x"))

        # Iterate over the coordinates of the claim
        for i_x in range(width):
            for i_y in range(height):
                # Calculate the coordinate of the current position
                coordinate: tuple[int, int] = (padding_left + i_x, padding_top + i_y)

                # Check if the coordinate is already in the dictionary otherwise add it
                if coordinate not in coordinate_to_claim_ids:
                    coordinate_to_claim_ids[coordinate] = [1, claim_id]
                # If the coordinate is already in the dictionary, increment the count
                else:
                    coordinate_to_claim_ids[coordinate][0] += 1
                    # Remove the claim ID (current and previous) from the set of non-overlapped claim IDs
                    no_overlapped_claim_ids.discard(claim_id)
                    no_overlapped_claim_ids.discard(coordinate_to_claim_ids[coordinate][1])

    # Count the number of coordinates with more than one claim
    overlapped_coordinates: int = sum(1 for value in coordinate_to_claim_ids.values() if value[0] > 1)

    # Extract the non-overlapped claim ID from the set if it exists otherwise set it to None
    no_overlapped_claim_id: str = no_overlapped_claim_ids.pop() if no_overlapped_claim_ids else None

    return overlapped_coordinates, no_overlapped_claim_id


if __name__ == "__main__":

    # Import function to print results
    import time
    from utils.file_utils import print_day_results

    # Calculate results for demo and real input files
    demo_1, demo_2 = solve_day_03_2018("input_demo.txt")
    start_time = time.time()
    solution_1, solution_2 = solve_day_03_2018("input.txt")
    end_time = time.time()

    # Calculate execution time in milliseconds
    execution_time = int((end_time - start_time) * 1000)

    # Print results in a formatted table (using rich)
    print_day_results(
        "2018", "03",
        str(demo_1), str(demo_2),
        str(solution_1), str(solution_2),
        execution_time
    )
