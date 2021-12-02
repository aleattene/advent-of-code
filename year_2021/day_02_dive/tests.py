import unittest
import solution_one
import solution_two


class MyTestCase(unittest.TestCase):

    def test_solution_one(self):
        self.assertEqual(solution_one.calculate_horizontal_depth_position("input_demo.txt"), 150)
        self.assertEqual(solution_one.calculate_horizontal_depth_position("input.txt"), 1746616)

    def test_solution_two(self):
        self.assertEqual(solution_two.calculate_horizontal_depth_position("input_demo.txt"), 900)
        self.assertEqual(solution_two.calculate_horizontal_depth_position("input.txt"), 1741971043)


if __name__ == '__main__':
    unittest.main()
