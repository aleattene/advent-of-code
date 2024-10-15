import os
from .solution_one_01_2015 import find_floor
from .solution_two_01_2015 import find_index_position_enter_basement

filename = "input.txt"
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, filename)


def test_first_part():
    result = find_floor(file_path)
    # TO FIX -> Handler error opening file
    assert result == 138


def test_second_part():
    result = find_index_position_enter_basement(file_path)
    assert result == 1771

