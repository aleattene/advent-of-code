

import unittest
from solution_one_two import function


class TestTrickShot(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(function()[0], 7503)
        self.assertEqual(function(124, 174, -86, -123)[0], 7503)

    def test_part_two(self):
        self.assertEqual(function()[1], 3229)
        self.assertEqual(function(124, 174, -86, -123)[1], 3229)


if __name__ == '__main__':
    unittest.main()
