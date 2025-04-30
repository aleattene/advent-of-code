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


def print_day_results(year: str, day: str, demo_1: str, demo_2: str, solution_1: str, solution_2: str, ) -> None:
    """
    Print a rich table with the results of Advent of Code for a given day.
    :param year: year of the challenge
    :param day: number of the day
    :param demo_1: result demo part 1
    :param demo_2: result demo part 2
    :param solution_1: result real part 1
    :param solution_2: result real part 2
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
    )

    # Add columns headers to the table
    table.add_column("", header_style="italic dim", no_wrap=True)
    table.add_column("Part 1", justify="right", header_style="bold magenta", style="bold magenta")
    table.add_column("Part 2", justify="right", header_style="bold green", style=" bold green")

    # Add rows with demo and solution results to the table
    table.add_row("Demo", str(demo_1), str(demo_2), style="white")
    table.add_row("Solution", str(solution_1), str(solution_2), style="")

    # Print the table to the console
    console.print(table)
    console.print()
