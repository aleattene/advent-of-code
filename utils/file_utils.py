import os
from rich.console import Console
from rich.table import Table


def get_input_file_path(current_file: str, filename: str) -> str:
    """Get the absolute path of the input file based on the current file location."""
    current_dir = os.path.dirname(current_file)
    return os.path.join(current_dir, filename)


def read_input_file(filename: str) -> list[str]:
    """Read the input file and return a list of lines."""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return f.read().splitlines()
    except Exception as error:
        raise RuntimeError(f"Error reading the file: {error}")


def get_manhattan_distance(x2: int, y2: int, x1: int = 0, y1: int = 0) -> int:
    """Calculate the Manhattan distance between two points."""
    return abs(x2 - x1) + abs(y2 - y1)


def print_day_results(
        year: str, day: str,
        demo_1: str, demo_2: str,
        solution_1: str, solution_2: str,
        execution_time: int = 0
) -> None:
    """
    Print a rich table with the results of Advent of Code for a given day.
    :param year: year of the challenge
    :param day: number of the day
    :param demo_1: result demo part 1
    :param demo_2: result demo part 2
    :param solution_1: result real part 1
    :param solution_2: result real part 2
    :param execution_time: execution time in milliseconds
    """
    # Create a console object for printing
    console = Console()
    console.print()

    # Create a table to display the results
    title = f"Advent of Code {year} – Day {day}"
    table = Table(
        title=title,
        style="bold white",
        title_style="bold yellow",
        caption_style="dim bright_cyan",
    )

    # Add columns headers to the table
    table.add_column("", header_style="italic dim", no_wrap=True)
    table.add_column("Part 1", justify="right", header_style="bold magenta", style="bold magenta")
    table.add_column("Part 2", justify="right", header_style="bold green", style=" bold green")

    # Add rows with demo and solution results to the table
    table.add_row("Demo", str(demo_1), str(demo_2), style="white")
    table.add_row("Solution", str(solution_1), str(solution_2), style="", end_section=True)
    # Add a caption with the execution time
    table.caption = f"Execution Time: {execution_time} ms"

    # Print the table to the console
    console.print(table)
    console.print()


def encrypt_caesar_cipher_with_exceptions(
        text_to_encrypt: str,
        shift: int,
        alphabet_length: int = 26,
        exceptions: dict[str, str] | None = None
) -> str:
    """
    Encrypt a Caesar cipher with a given shift.
    :param text_to_encrypt: The text to encrypt.
    :param shift: The shift value for the Caesar cipher.
    :param alphabet_length: The length of the alphabet (26 for English).
    :param exceptions: A dictionary of exceptions for specific characters.
    :return: The encrypted text.
    """
    # Check if exceptions is None and initialize it as an empty dictionary
    exceptions = exceptions or {}
    # Normalize the shift value to be within the range of the alphabet length
    shift %= alphabet_length

    encrypted_text = []

    for char in text_to_encrypt:
        # If the character is in exceptions, replace it with the corresponding value in the exceptions dictionary
        if exceptions and char in exceptions:
            encrypted_text.append(exceptions[char])
        # If the character is a digit, apply the shift to it
        elif char.isalpha():
            # Determine the base ASCII value for uppercase or lowercase letters
            base_char = ord('A') if char.isupper() else ord('a')
            # Calculate the new position by applying the shift with wrapping
            code_char = (ord(char) - base_char + shift) % alphabet_length
            # Append the encrypted character to the result
            encrypted_text.append(chr(base_char + code_char))
        # If the character is not a letter, keep it unchanged
        else:
            encrypted_text.append(char)
    return "".join(encrypted_text)


def decrypt_caesar_cipher_with_exceptions(
    text_to_decrypt: str,
    shift: int,
    alphabet_length: int = 26,
    exceptions: dict[str, str] | None = None
) -> str:
    """
    Decrypt a Caesar cipher with a given shift.
    :param text_to_decrypt: The text to decrypt.
    :param shift: The shift value for the Caesar cipher.
    :param alphabet_length: The length of the alphabet (26 for English).
    :param exceptions: A dictionary of exceptions for specific characters.
    :return: The decrypted text.
    """
    # Call the encrypt function with a negative shift to decrypt
    return encrypt_caesar_cipher_with_exceptions(text_to_decrypt, -shift, alphabet_length, exceptions)


