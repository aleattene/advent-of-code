import os
from dotenv import load_dotenv
from .solution_day_05_2015 import solve_day_05_2015

load_dotenv()
environment = os.getenv("ENVIRONMENT")

filename_demo_one = "input_demo_one.txt"
filename_demo_two = "input_demo_two.txt"
filename = "input.txt"
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path_demo_one = os.path.join(current_dir, filename_demo_one)
file_path_demo_two = os.path.join(current_dir, filename_demo_two)
file_path = os.path.join(current_dir, filename)


def test_day_05_2015():
    results_demo = solve_day_05_2015(file_path_demo_one, file_path_demo_two)
    assert results_demo == (2, 2)
    if environment == "development":
        expected_results = (int(os.getenv("SOLUTION_01_DAY_05_2015")),
                            int(os.getenv("SOLUTION_02_DAY_05_2015")))
        results = solve_day_05_2015(file_path)
        assert expected_results == results
