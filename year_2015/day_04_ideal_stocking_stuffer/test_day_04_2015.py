import os
from .solution_day_04_2015 import solve_day_04_2015

filename_demo = "input_demo.txt"
filename = "input.txt"
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path_demo = os.path.join(current_dir, filename_demo)
file_path = os.path.join(current_dir, filename)


def test_day_03_201():
    # TO FIX -> Handler error opening file
    result_demo = solve_day_04_2015(file_path_demo)
    assert result_demo == (609043, 6742839)
    result = solve_day_04_2015(file_path)
    assert result == (346386, 9958218)
