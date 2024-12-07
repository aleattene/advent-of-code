import os
from .solution_day_07_2024 import solve_day_07_2024

filename_demo = "input_demo.txt"
filename = "input.txt"
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path_demo = os.path.join(current_dir, filename_demo)
file_path = os.path.join(current_dir, filename)


def test_day_07_2024():
    result_demo = solve_day_07_2024(file_path_demo)
    assert result_demo == (3749, 11387)
    result_one = solve_day_07_2024(file_path)
    assert result_one == (7579994664753, 438027111276610)

