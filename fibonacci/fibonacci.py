import unittest


class Fibonacci:
    def compute_n_term(self, n):
        if n <= 1:
            return n
        else:
            return self.compute_n_term(n - 1) + self.compute_n_term(n - 2)

    def generate(self, number_of_terms):
        return [self.compute_n_term(i) for i in range(0, number_of_terms)]


class TestFibonacci(unittest.TestCase):
    def test_fibonacci_third_term(self):
        fibonacci = Fibonacci()
        self.assertEqual(fibonacci.compute_n_term(3), 2)

    def test_fibonacci_suit(self):
        fibonacci = Fibonacci()
        self.assertEqual(fibonacci.generate(4), [0, 1, 1, 2])


if __name__ == '__main__':
    unittest.main()
