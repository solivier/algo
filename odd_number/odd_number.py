import unittest


class RemoveEvenNumbersFromList:
    def execute(self, list):
        return [item for item in list if item % 2 == 1]


class TestRemoveEvenNumbersFromList(unittest.TestCase):
    def test_remove(self):
        test = RemoveEvenNumbersFromList()
        self.assertEqual([1, 3, 5, 7], test.execute([1, 2, 3, 4, 5, 6, 7, 8]))


if __name__ == '__main__':
    unittest.main()
