def find_sum(lst, n):
    """
    Function to find two number that add up to n (O(n))
    :param lst: A list of integers
    :param n: The integer number n
    """

    found_values = set()

    for ele in lst:
        if n - ele in found_values:
            return [n - ele, ele]
        found_values.add(ele)

    return False


# Driver to test above code
if __name__ == '__main__':
    print(find_sum([1, 3, 2, 4], 6))


5, 7, 9, 13, 11, 6, 6, 3, 3