import os
from .solution_one_day_01_2023 import solve_day_01_2023_one
from .solution_two_day_01_2023 import solve_day_01_2023_two

filename_demo_one = "input_demo_one.txt"
filename_demo_two = "input_demo_two.txt"
filename = "input.txt"
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path_demo_one = os.path.join(current_dir, filename_demo_one)
file_path_demo_two = os.path.join(current_dir, filename_demo_two)
file_path = os.path.join(current_dir, filename)


def test_day_01_2023_one():
    result_demo_one = solve_day_01_2023_one(file_path_demo_one)
    assert result_demo_one == 142
    result_one = solve_day_01_2023_one(file_path)
    assert result_one == 56397


def test_second_part():
    result_demo_two = solve_day_01_2023_two(file_path_demo_two)
    assert result_demo_two == 281
    result_two = solve_day_01_2023_two(file_path)
    assert result_two == 55701

