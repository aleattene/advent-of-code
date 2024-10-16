import os
from .solution_one_day_01_2023 import solve_day_01_2023_one
from .solution_two_day_01_2023 import solve_day_01_2023_two

filename = "input.txt"
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, filename)


def test_first_part():
    result = solve_day_01_2023_one(file_path)
    assert result == 56397


def test_second_part():
    result = solve_day_01_2023_two(file_path)
    assert result == 55701

