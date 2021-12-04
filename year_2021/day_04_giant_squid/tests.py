import unittest
import solution_one
import solution_two


class MyTestCase(unittest.TestCase):

    def test_solution_one(self):
        self.assertEqual(solution_one.bingo("input_demo.txt"), 4512)
        self.assertEqual(solution_one.bingo("input.txt"), 41668)

    def test_solution_two(self):
        self.assertEqual(solution_two.bingo("input_demo.txt"), 1924)
        self.assertEqual(solution_two.bingo("input.txt"), 10478)


if __name__ == '__main__':
    unittest.main()
