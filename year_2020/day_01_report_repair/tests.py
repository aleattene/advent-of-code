import unittest
import solution_one
import solution_two


class MyTestCase(unittest.TestCase):

    def test_solution_one(self):
        self.assertEqual(solution_one.find_entries_2020("input_demo.txt"), 514579)
        self.assertEqual(solution_one.find_entries_2020("input.txt"), 485739)

    def test_solution_two(self):
        self.assertEqual(solution_two.find_entries_2020("input_demo.txt"), 241861950)
        self.assertEqual(solution_two.find_entries_2020("input.txt"), 161109702)


if __name__ == '__main__':
    unittest.main()
