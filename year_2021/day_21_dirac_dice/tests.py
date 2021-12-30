
import unittest
from solution_one import function_one
from solution_two import function_two


class MyTestCase(unittest.TestCase):
    def test_solution_one(self):
        self.assertEqual(function_one(4, 8), 739785)
        self.assertEqual(function_one(7, 3), 551901)

    def test_solution_two(self):
        self.assertEqual(function_two(4, 8), 444356092776315)
        self.assertEqual(function_two(7, 3), 272847859601291)


if __name__ == '__main__':
    unittest.main()
