import unittest
import solution_one
import solution_two


class MyTestCase(unittest.TestCase):

    def test_solution_one(self):
        self.assertEqual(solution_one.find_overlapping_lines("input_demo.txt"), 5)
        self.assertEqual(solution_one.find_overlapping_lines("input.txt"), 6564)

    def test_solution_two(self):
        self.assertEqual(solution_two.find_overlapping_lines("input_demo.txt"), 12)
        self.assertEqual(solution_two.find_overlapping_lines("input.txt"), 19172)


if __name__ == '__main__':
    unittest.main()
