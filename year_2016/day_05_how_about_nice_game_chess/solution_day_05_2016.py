from utils.file_utils import get_input_file_path, read_input_file


def get_md5_hash(text_to_encode: str | bytes) -> str:
    """
    Generate the MD5 hash of a given text.
    :param text_to_encode: The text to encode (string or bytes).
    :return: The MD5 hash of the input text.
    """
    import hashlib

    # Check if the input is a string and convert it to bytes
    if isinstance(text_to_encode, str):
        text_to_encode = text_to_encode.encode('utf-8')
    # Return the MD5 hash of the input text
    return hashlib.md5(text_to_encode).hexdigest()


def solve_day_05_2016(filename: str) -> tuple[str, str]:
    """
    Solve the Advent of Code 2016 Day 05 - How About Nice Game Chess.
    :param filename: The name of the input file containing the room data.
    :return: The door simple password (part 1) and the door complex password (part 2).
    """
    try:
        # Create the absolute path of the input file
        input_file_path = get_input_file_path(__file__, filename)
        # Read the input file
        data = read_input_file(input_file_path)
    except Exception as error:
        raise RuntimeError(f"Error: {error}")

    id_door: str = data[0]
    # Generate the MD5 hash of the door ID only once (it's not necessary to do it multiple times in the loop)
    id_door_bytes = id_door.encode('utf-8')

    # Initialize the variables
    password_length: int = 8
    password_1_list: list[str] = []
    char_value_password_1 = 5
    password_2_list: list[str | None] = [None] * password_length
    password_2_length: int = 0
    char_position_password_2: int = 5
    char_value_password_2: int = 6
    idx_hash: int = 0

    while True:
        idx_bytes = str(idx_hash).encode('utf-8')
        room_hashed = get_md5_hash(id_door_bytes + idx_bytes)
        idx_hash += 1

        # If the hash doesn't start with "00000", skip to the next iteration
        if not room_hashed.startswith("00000"):
            continue

        # The hash is valid, so we can extract the character (value) we need to build the password part 1
        if len(password_1_list) < password_length:
            password_1_list.append(room_hashed[char_value_password_1])

        # The hash is valid, so we can extract the characters (position and value) we need to build the password part 2
        digit_position: str | int = room_hashed[char_position_password_2]
        if digit_position.isdigit():
            digit_position = int(digit_position)
            if 0 <= digit_position < password_length and password_2_list[digit_position] is None:
                password_2_list[digit_position] = room_hashed[char_value_password_2]
                password_2_length += 1

        # Check if the passwords chars are found
        if len(password_1_list) == password_length and password_2_length == password_length:
            break

    # When the chars of the passwords are found, we need to join them to form the real passwords
    password_1: str = "".join(password_1_list)
    password_2: str = "".join(password_2_list)

    return password_1, password_2


if __name__ == "__main__":

    # Import function to print results
    from utils.file_utils import print_day_results

    # Calculate results for demo and real input files
    demo_1, demo_2 = solve_day_05_2016("input_demo.txt")

    solution_1, solution_2 = solve_day_05_2016("input.txt")

    # Print results in a formatted table (using rich)
    print_day_results(
        "2016", "05",
        str(demo_1), str(demo_2),
        str(solution_1), str(solution_2)
    )
