import os
from .solution_one_01_2015 import find_floor
from .solution_two_01_2015 import find_index_position_enter_basement

filename_demo = "input_demo.txt"
filename = "input.txt"

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path_demo = os.path.join(current_dir, filename_demo)
file_path = os.path.join(current_dir, filename)


def test_first_part():
    # TO FIX -> Handler error opening file
    result_demo = find_floor(file_path_demo)
    assert result_demo == -3
    result = find_floor(file_path)
    assert result == 138


def test_second_part():
    result_demo = find_index_position_enter_basement(file_path_demo)
    assert result_demo == 43
    result = find_index_position_enter_basement(file_path)
    assert result == 1771

