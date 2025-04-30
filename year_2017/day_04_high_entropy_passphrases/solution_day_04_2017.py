from utils.file_utils import get_input_file_path, read_input_file


def is_valid_no_duplicates_passphrase(words: list[str]) -> bool:
    """
    Return True if the passphrase is valid, False otherwise.
    A passphrase is valid if it contains no duplicate words.
    """
    return len(words) == len(set(words))


def is_valid_no_anagrams_duplicates_passphrase(words: list[str]) -> bool:
    """
    Return True if the passphrase is valid, False otherwise.
    A passphrase is valid if it contains no duplicate words and no anagrams.
    """
    normalized = {"".join(sorted(word)) for word in words}
    return len(words) == len(normalized)


def solve_day_04_2017(filename: str) -> tuple[int, int] | str:
    try:
        # Create the absolute path of the input file
        input_file_path = get_input_file_path(__file__, filename)
        # Read the input file
        data = read_input_file(input_file_path)
    except Exception as error:
        return f"Error: {error}"

    # Parse the input data to create from a list of strings (list passphrases) to a list of lists of strings
    passphrases = [line.split() for line in data]

    # Check if the passphrase is valid (no duplicates) and count the number of valid passphrases
    num_valid_passphrases_1 = sum(is_valid_no_duplicates_passphrase(passphrase) for passphrase in passphrases)

    # Check if the passphrase is valid (no duplicates and no anagrams) and count the number of valid passphrases
    num_valid_passphrases_2 = sum(is_valid_no_anagrams_duplicates_passphrase(passphrase) for passphrase in passphrases)

    return num_valid_passphrases_1, num_valid_passphrases_2


if __name__ == "__main__":

    # Import function to print results
    from utils.file_utils import print_day_results

    # Calculate results for demo and real input files
    demo_1, demo_2 = solve_day_04_2017("input_demo.txt")
    solution_1, solution_2 = solve_day_04_2017("input.txt")

    # Print results in a formatted table (using rich)
    print_day_results(
        "2017", "04",
        str(demo_1), str(demo_2),
        str(solution_1), str(solution_2)
    )
