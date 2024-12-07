import os
from dotenv import load_dotenv
from .solution_one_01_2020 import find_entries_2020 as find_entries_2020_one
from .solution_two_01_2020 import find_entries_2020 as find_entries_2020_two

load_dotenv()
environment = os.getenv("ENVIRONMENT")

filename_demo = "input_demo.txt"
filename = "input.txt"
current_dir = os.path.dirname(os.path.abspath(__file__))
file_demo = os.path.join(current_dir, filename_demo)
file_path = os.path.join(current_dir, filename)


def test_day_01_2020():
    result_demo = find_entries_2020_one(file_demo)
    assert result_demo == 514579
    result_demo = find_entries_2020_two(file_demo)
    assert result_demo == 241861950
    if environment == "development":
        expected_result_one = int(os.getenv("SOLUTION_01_DAY_01_2020"))
        result_one = find_entries_2020_one(file_path)
        assert result_one == expected_result_one
        expected_result_two = int(os.getenv("SOLUTION_02_DAY_01_2020"))
        result_two = find_entries_2020_two(file_path)
        assert result_two == expected_result_two


