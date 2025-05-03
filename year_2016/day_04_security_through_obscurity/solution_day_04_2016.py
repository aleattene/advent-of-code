from collections import Counter
from utils.file_utils import get_input_file_path, read_input_file, encrypt_caesar_cipher_with_exceptions


def solve_day_04_2016(filename: str) -> tuple[int, int | None]:
    """
    Solve the Advent of Code 2016 Day 04 - Security Through Obscurity.
    :param filename: The name of the input file containing the room data.
    :return: Sum of sector IDs of valid rooms (part 1) and the sector ID of the "northpole" object storage (part 2).
    """
    try:
        # Create the absolute path of the input file
        input_file_path = get_input_file_path(__file__, filename)
        # Read the input file
        data = read_input_file(input_file_path)
    except Exception as error:
        raise RuntimeError(f"Error: {error}")

    total_sector_id: int = 0
    northpole_sector_id: int | None = None

    for room in data:
        # Split the room data into its components (name, sector ID, and checksum)
        name_and_sector_id, checksum = room.rstrip("]\n").split("[", 1)
        checksum_length = len(checksum)

        # Extract the name and sector ID
        *name_segments, sector_id = name_and_sector_id.split("-")
        sector_id = int(sector_id)

        # Count the frequency of each character in the name
        name = "".join(name_segments)
        frequencies: Counter[str] = Counter(name)

        # Order the tuple (char, frequency) first by frequency (descending) and then by character (ascending)
        sorted_frequencies = sorted(frequencies.items(), key=lambda item: (-item[1], item[0]))

        # Calculate the expected checksum by taking the first 'checksum_length' characters from the sorted frequencies
        expected_checksum = "".join(char for char, _ in sorted_frequencies)[:checksum_length]

        # Check if the expected checksum matches the actual checksum or not (part 1)
        if expected_checksum != checksum:
            continue
        total_sector_id += sector_id

        # Decrypt (only once) the Real Room using the Caesar cipher with exceptions (part 2)
        if northpole_sector_id is None:
            decrypted_name = encrypt_caesar_cipher_with_exceptions(
                text_to_encrypt="-".join(name_segments),
                shift=sector_id,
                exceptions={"-": " "}
            )
            # Check if the decrypted name contains "northpole object storage"
            if "northpole object storage" in decrypted_name:
                northpole_sector_id = sector_id

    return total_sector_id, northpole_sector_id


if __name__ == "__main__":

    # Import function to print results
    from utils.file_utils import print_day_results

    # Calculate results for demo and real input files
    demo_1, demo_2 = solve_day_04_2016("input_demo.txt")
    solution_1, solution_2 = solve_day_04_2016("input.txt")

    # Print results in a formatted table (using rich)
    print_day_results(
        "2016", "04",
        str(demo_1), str(demo_2),
        str(solution_1), str(solution_2)
    )
