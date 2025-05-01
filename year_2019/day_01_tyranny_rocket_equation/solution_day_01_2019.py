import itertools
import math

from utils.file_utils import get_input_file_path, read_input_file


def get_fuel_from_mass(mass: int) -> int:
    """
    Calculate the fuel required for a given mass.
    :param mass: The mass of the module.
    :return: The fuel required for the module.
    """
    return math.floor(mass / 3) - 2


def get_strong_fuel_from_mass(mass: int) -> int:
    """
    Calculate the total fuel required for a given mass, including the fuel for the fuel itself.
    :param mass: The mass of the module.
    :return: The total fuel required for the module.
    """
    # Calculate the initial fuel requirement
    total_fuel = 0
    fuel = get_fuel_from_mass(mass)
    # Iterate until the fuel is zero or negative and add the fuel required for the fuel itself
    while fuel > 0:
        total_fuel += fuel
        fuel = get_fuel_from_mass(fuel)
    # Return the total fuel required
    return total_fuel


def solve_day_01_2019(filename: str) -> tuple[int, int] | str:
    """
    Solve the Advent of Code 2019 Day 01 - The Tyranny of the Rocket Equation.
    :param filename: The name of the input file containing the frequency changes.
    :return: Total fuel required for all modules (part 1) and the total fuel required for all modules
            including the fuel for the fuel itself (part 2).
    """
    try:
        # Create the absolute path of the input file
        input_file_path = get_input_file_path(__file__, filename)
        # Read the input file
        data = read_input_file(input_file_path)
    except Exception as error:
        return f"Error: {error}"

    # Convert the input data (list of strings) to a list of integers and calculate the total fuel for each mass (part 1)
    total_fuel = sum(get_fuel_from_mass(int(mass)) for mass in data)
    # Calculate the total fuel required for each mass, including the fuel for the fuel itself (part 2)
    total_strong_fuel = sum(get_strong_fuel_from_mass(int(mass)) for mass in data)

    return total_fuel, total_strong_fuel


if __name__ == "__main__":

    # Import function to print results
    from utils.file_utils import print_day_results

    # Calculate results for demo and real input files
    demo_1, demo_2 = solve_day_01_2019("input_demo.txt")
    solution_1, solution_2 = solve_day_01_2019("input.txt")

    # Print results in a formatted table (using rich)
    print_day_results(
        "2019", "01",
        str(demo_1), str(demo_2),
        str(solution_1), str(solution_2)
    )
