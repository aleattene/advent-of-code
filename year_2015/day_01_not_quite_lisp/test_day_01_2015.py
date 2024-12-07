import os
from dotenv import load_dotenv
from .solution_one_01_2015 import find_floor
from .solution_two_01_2015 import find_index_position_enter_basement

load_dotenv()
environment = os.getenv("ENVIRONMENT")

filename_demo = "input_demo.txt"
filename = "input.txt"
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path_demo = os.path.join(current_dir, filename_demo)
file_path = os.path.join(current_dir, filename)


def test_day_01_2015():
    result_demo = find_floor(file_path_demo)
    assert result_demo == -3
    result_demo = find_index_position_enter_basement(file_path_demo)
    assert result_demo == 43
    if environment == "development":
        expected_result_one = int(os.getenv("SOLUTION_01_DAY_01_2015"))
        result_one = find_floor(file_path)
        assert expected_result_one == result_one
        expected_result_two = int(os.getenv("SOLUTION_02_DAY_01_2015"))
        result_two = find_index_position_enter_basement(file_path)
        assert expected_result_two == result_two
