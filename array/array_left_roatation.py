def array_left_rotation(a, k):
    a = list(a)
    return a[k:] + a[:k]


print(array_left_rotation([1, 2, 3, 4, 5], 4))
