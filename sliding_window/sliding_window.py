import unittest


class AveragesOfSubarrays:
    @staticmethod
    def compute(k, arr):
        result = []
        window_sum, window_start = 0.0, 0
        for windowEnd in range(len(arr)):
            window_sum += arr[windowEnd]
            if windowEnd >= k - 1:
                result.append(window_sum / k)
                window_sum -= arr[window_start]
                window_start += 1

        return result


class TestSlidingWindow(unittest.TestCase):
    def test_find_average_of_all_subarrays_of_size_5(self):
        self.assertEqual(AveragesOfSubarrays.compute(5, [1, 3, 2, 6, -1, 4, 1, 8, 2]), [2.2, 2.8, 2.4, 3.6, 2.8])


if __name__ == '__main__':
    unittest.main()

