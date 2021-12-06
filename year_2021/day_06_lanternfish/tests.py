import unittest
from solution_one_two import lantern_fish


class MyTestCase(unittest.TestCase):

    def test_solution(self):
        days = 18
        self.assertEqual(lantern_fish("input_demo.txt", days), 26)
        days = 80
        self.assertEqual(lantern_fish("input_demo.txt", days), 5934)
        self.assertEqual(lantern_fish("input.txt", days), 352195)
        days = 256
        self.assertEqual(lantern_fish("input_demo.txt", days), 26984457539)
        self.assertEqual(lantern_fish("input.txt", days), 1600306001288)


if __name__ == '__main__':
    unittest.main()
