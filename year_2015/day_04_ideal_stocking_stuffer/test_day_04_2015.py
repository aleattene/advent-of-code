import os
from dotenv import load_dotenv
from .solution_day_04_2015 import solve_day_04_2015

load_dotenv()
environment = os.getenv("ENVIRONMENT")

filename_demo = "input_demo.txt"
filename = "input.txt"
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path_demo = os.path.join(current_dir, filename_demo)
file_path = os.path.join(current_dir, filename)


def test_day_04_2015():
    results_demo = solve_day_04_2015(file_path_demo)
    assert results_demo == (609043, 6742839)
    if environment == "DEVELOPMENT":
        expected_results = int(os.getenv("SOLUTION_01_DAY_04_2015"),
                               int(os.getenv("SOLUTION_02_DAY_04_2015")))
        results = solve_day_04_2015(file_path)
        assert expected_results == results
