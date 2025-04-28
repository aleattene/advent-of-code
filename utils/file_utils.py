import os


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
