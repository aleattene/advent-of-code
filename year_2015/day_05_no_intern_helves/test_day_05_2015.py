import os
from .solution_day_05_2015 import solve_day_05_2015

filename_demo_one = "input_demo_one.txt"
filename_demo_two = "input_demo_two.txt"
filename = "input.txt"
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path_demo_one = os.path.join(current_dir, filename_demo_one)
file_path_demo_two = os.path.join(current_dir, filename_demo_two)
file_path = os.path.join(current_dir, filename)


def test_day_05_2015():
    # TO FIX -> Handler error opening file
    result_demo = solve_day_05_2015(file_path_demo_one, file_path_demo_two)
    assert result_demo == (2, 2)
    result = solve_day_05_2015(file_path)
    assert result == (258, 53)
