import os
from .solution_one_01_2020 import find_entries_2020 as find_entries_2020_one
from .solution_two_01_2020 import find_entries_2020 as find_entries_2020_two

filename_demo = "input_demo.txt"
filename = "input.txt"
current_dir = os.path.dirname(os.path.abspath(__file__))
file_demo = os.path.join(current_dir, filename_demo)
file_path = os.path.join(current_dir, filename)


def test_first_part():
    result_demo = find_entries_2020_one(file_demo)
    assert result_demo == 514579
    result = find_entries_2020_one(file_path)
    assert result == 485739


def test_second_part():
    result_demo = find_entries_2020_two(file_demo)
    assert result_demo == 241861950
    result = find_entries_2020_two(file_path)
    assert result == 161109702

