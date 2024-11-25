import os
from .solution_day_03_2023 import solve_day_03_2023

filename_demo = "input_demo.txt"
filename = "input.txt"
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path_demo = os.path.join(current_dir, filename_demo)
file_path = os.path.join(current_dir, filename)


def test_day_03_2023():
    result_demo = solve_day_03_2023(file_path_demo)
    assert result_demo == (4361, 467835)
    result = solve_day_03_2023(file_path)
    assert result == (519444, 74528807)



