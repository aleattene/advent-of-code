import os
from .solution_one_day_03_2015 import solve_day_03_2015_one
from .solution_two_day_03_2015 import solve_day_03_2015_two

filename_demo = "input_demo.txt"
filename = "input.txt"
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path_demo = os.path.join(current_dir, filename_demo)
file_path = os.path.join(current_dir, filename)


def test_day_03_2015_one():
    # TO FIX -> Handler error opening file
    result_demo = solve_day_03_2015_one(file_path_demo)
    assert result_demo == 5
    result = solve_day_03_2015_one(file_path)
    assert result == 2572


def test_day_03_2015_two():
    # TO FIX -> Handler error opening file
    result_demo = solve_day_03_2015_two(file_path_demo)
    assert result_demo == 13
    result = solve_day_03_2015_two(file_path)
    assert result == 2631
