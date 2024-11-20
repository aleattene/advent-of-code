def read_input_file(filename: str) -> list[str]:
    """Read the input file and return the content."""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return f.read().splitlines()
    except Exception as error:
        raise RuntimeError(f"Error reading the file: {error}")


def contains_substring(word: str) -> bool:
    """Check if a word contains any of the substrings."""
    substrings = ("ab", "cd", "pq", "xy")
    return any(substring in word for substring in substrings)


def contains_twice_letters(word: str) -> bool:
    """Check if a word contains at least one letter that appears twice."""
    return any(word[i] == word[i + 1] for i in range(len(word) - 1))


def contains_three_vowels(word: str) -> bool:
    """Check if a word contains at least three vowels."""
    vowels = "aeiou"
    return sum(1 for letter in word if letter in vowels) >= 3


def contains_double_pair(word: str) -> bool:
    """Check if a word contains at least one pair of letters that appears twice without overlapping."""
    seen_pairs = {}
    for i in range(len(word) - 1):
        pair = word[i:i + 2]
        if pair in seen_pairs and seen_pairs[pair] < i - 1:
            return True
        seen_pairs[pair] = i
    return False


def contains_letter_between_repeat(word: str) -> bool:
    """Check if a word contains a letter that repeats with exactly one letter between them."""
    return any(word[i] == word[i + 2] for i in range(len(word) - 2))


def solve_part_one(words: list[str]) -> int:
    """Solve the first part of the puzzle."""
    return sum(
        1 for word in words if word
        and not contains_substring(word)
        and contains_twice_letters(word)
        and contains_three_vowels(word)
    )


def solve_part_two(words: list[str]) -> int:
    """Solve the second part of the puzzle."""
    return sum(
        1 for word in words if word
        and contains_double_pair(word)
        and contains_letter_between_repeat(word)
    )


def solve_day_05_2015(filename_one: str, filename_two: str = "") -> tuple[int, int] | str:
    """ Find the number of nice words in the input data."""
    try:
        # Read input data once and use it for both parts
        words_one = read_input_file(filename_one)
        # If filename_two is different, read it separately
        words_two = read_input_file(filename_two) if filename_two else words_one

        # Calculate the solutions for both parts
        nice_words_one = solve_part_one(words_one)
        nice_words_two = solve_part_two(words_two)

        return nice_words_one, nice_words_two
    except Exception as error:
        return f"Error: {error}"
