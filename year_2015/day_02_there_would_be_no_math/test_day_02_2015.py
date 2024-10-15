import os
from .solution_one_day_02_2015 import solve_day_02_2015_one

filename = "input.txt"
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, filename)


def test_day_02_2015_one():
    result = solve_day_02_2015_one(file_path)
    # TO FIX -> Handler error opening file
    assert result == 1598415


# def test_second_part():
#     result = solve_day01_two(file_path)
#     assert result == "55701"
