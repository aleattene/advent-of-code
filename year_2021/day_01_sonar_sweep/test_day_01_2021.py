import os
from dotenv import load_dotenv
from .solution_day_01_2021 import solve_day_01_2021

load_dotenv()
environment = os.getenv("ENVIRONMENT")

filename_demo = "input_demo.txt"
filename = "input.txt"
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path_demo = os.path.join(current_dir, filename_demo)
file_path = os.path.join(current_dir, filename)


def test_day_01_2021():
    results_demo = solve_day_01_2021(file_path_demo)
    assert results_demo == (7, 5)
    if environment == "development":
        expected_results = (int(os.getenv("SOLUTION_01_DAY_01_2021")),
                            int(os.getenv("SOLUTION_02_DAY_01_2021")))
        results = solve_day_01_2021(file_path)
        assert expected_results == results
