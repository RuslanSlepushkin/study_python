import unittest
from task_1 import in_range


class TestInRange(unittest.TestCase):
    def test_in_range_default_arguments(self) -> None:
        result = list(in_range(10))
        self.assertEqual(result, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])


    def test_in_range_with_end(self) -> None:
        result = list(in_range(1, 10))
        self.assertEqual(result, [1, 2, 3, 4, 5, 6, 7, 8, 9])


    def test_in_range_with_end_and_step(self) -> None:
        result = list(in_range(1, 10, 2))
        self.assertEqual(result, [1, 3, 5, 7, 9])


    def test_in_range_with_reverse_step(self) -> None:
        result = list(in_range(10, 1, -1))
        self.assertEqual(result, [10, 9, 8, 7, 6, 5, 4, 3, 2])


    def test_in_range_with_zero_step(self) -> None:
        result = list(in_range(1, 10, 0))
        self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main()