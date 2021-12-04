import unittest
import solution_one
import solution_two


class MyTestCase(unittest.TestCase):

    def test_solution_one(self):
        self.assertEqual(solution_one.velocity("input_demo.txt"), 198)
        self.assertEqual(solution_one.velocity("input.txt"), 845186)

    def test_solution_two(self):
        self.assertEqual(solution_two.support("input_demo.txt"), 230)
        self.assertEqual(solution_two.support("input.txt"), 4636702)


if __name__ == '__main__':
    unittest.main()
