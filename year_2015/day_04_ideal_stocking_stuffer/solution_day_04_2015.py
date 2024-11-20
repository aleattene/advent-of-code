import hashlib


def read_input_file(filename: str) -> str:
    """Read the input file and return the content."""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as error:
        raise RuntimeError(f"Error reading the file: {error}")


def generate_md5_hash(data: str) -> str:
    """Generate the MD5 hash of the data."""
    hash_md5 = hashlib.md5(data.encode('utf-8'))
    return hash_md5.hexdigest()


def find_solutions(data: str, one: int, two: int) -> tuple[int, int]:
    """Find the puzzle solutions."""
    start = 1
    solution_one = None
    solution_two = None

    while True:
        # Generate the hash of the data
        hash_hex = generate_md5_hash(f"{data}{start}")

        # Check if the hash starts with the required number of zeros
        if solution_one is None and hash_hex.startswith("0" * one):
            solution_one = start
        if solution_one is not None and hash_hex.startswith("0" * two):
            solution_two = start

        # Break the loop if both solutions are found
        if solution_one is not None and solution_two is not None:
            break

        # Increment the start value
        start += 1

    return solution_one, solution_two


def solve_day_04_2015(filename: str) -> tuple[int, int] | str:
    try:
        # Read the input file
        data = read_input_file(filename)
        # Find the solutions
        return find_solutions(data, 5, 6)
    except RuntimeError as error:
        return str(error)


