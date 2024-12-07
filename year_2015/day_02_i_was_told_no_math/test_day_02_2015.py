import os
from dotenv import load_dotenv
from .solution_one_day_02_2015 import solve_day_02_2015_one
from .solution_two_day_02_2015 import solve_day_02_2015_two

load_dotenv()
environment = os.getenv("ENVIRONMENT")

filename_demo = "input_demo.txt"
filename = "input.txt"
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path_demo = os.path.join(current_dir, filename_demo)
file_path = os.path.join(current_dir, filename)


def test_day_02_2015():
    result_demo = solve_day_02_2015_one(file_path_demo)
    assert result_demo == 101
    result_demo = solve_day_02_2015_two(file_path_demo)
    assert result_demo == 48
    if environment == "development":
        expected_result_one = int(os.getenv("SOLUTION_01_DAY_02_2015"))
        result_one = solve_day_02_2015_one(file_path)
        assert expected_result_one == result_one
        expected_result_two = int(os.getenv("SOLUTION_02_DAY_02_2015"))
        result_two = solve_day_02_2015_two(file_path)
        assert expected_result_two == result_two
