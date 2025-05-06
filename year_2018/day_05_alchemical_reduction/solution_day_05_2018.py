from utils.file_utils import get_input_file_path, read_input_file


def do_polymer_reactions(polymer: str) -> str:
    """
    Function to perform polymer reactions by removing adjacent pairs of characters
    that are the same but with different cases (uppercase and lowercase).
    :param polymer: string representing the polymer.
    :return: string representing the polymer after all possible reactions.
    """
    # Initialize the stack of characters to keep track of the polymer during the possible reactions
    chars_stack: list[str] = list()

    # Iterate through each character in the polymer
    for char in polymer:
        # If the last character in the stack is the same as the current character (but with different case), pop it
        if chars_stack and chars_stack[-1] == char.swapcase():
            chars_stack.pop()
        # Otherwise, add the current character to the stack
        else:
            chars_stack.append(char)

    return "".join(chars_stack)


def solve_day_05_2018(filename: str) -> tuple[int, int]:
    """
    Solution of the Advent of Code 2018 Day 05 - Alchemical Reduction.
    :param filename: The name of the input file containing the room data.
    :return: A tuple containing the length of the polymer after all possible reactions (part 1) and
            the length of the polymer after removing the best possible character (part 2).
    """
    try:
        # Create the absolute path of the input file
        input_file_path = get_input_file_path(__file__, filename)
        # Read the input file
        data = read_input_file(input_file_path)[0]
    except Exception as error:
        raise RuntimeError(f"Error: {error}")

    # The length of the stack is the length of the polymer after all possible reactions (part 1)
    polymer_length_1 = len(do_polymer_reactions(data))

    # Initialize a set to keep track of the unique characters in the polymer
    chars_polymer = set(data.lower())

    # Initialize the best polymer length to the length of the polymer after all possible reactions (default)
    best_polymer_length = polymer_length_1

    # Iterate through each unique character in the polymer
    for char in chars_polymer:
        # Create a new polymer by removing all occurrences of the current character (both lowercase and uppercase)
        polymer = data.replace(char, "").replace(char.swapcase(), "")

        # Calculate the length of the polymer after all possible reactions
        polymer_length = len(do_polymer_reactions(polymer))

        # Update the best polymer length if the current one is shorter
        best_polymer_length = min(best_polymer_length, polymer_length)

    return polymer_length_1, best_polymer_length


if __name__ == "__main__":

    # Import function to print results
    import time
    from utils.file_utils import print_day_results

    # Calculate results for demo and real input files
    demo_1, demo_2 = solve_day_05_2018("input_demo.txt")
    start_time = time.time()
    solution_1, solution_2 = solve_day_05_2018("input.txt")
    end_time = time.time()

    # Calculate execution time in milliseconds
    execution_time = int((end_time - start_time) * 1000)

    # Print results in a formatted table (using rich)
    print_day_results(
        "2018", "05",
        str(demo_1), str(demo_2),
        str(solution_1), str(solution_2),
        execution_time
    )
