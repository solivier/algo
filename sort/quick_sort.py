# Below partition is using Hoare's algorithm.
def partition(arr, low, high):
    pivot_value = arr[low]
    i = low
    j = high

    while i < j:
        while i <= high and arr[i] <= pivot_value:
            i += 1
        while arr[j] > pivot_value:
            j -= 1
        if i < j:
            # swap arr[i], arr[j]
            arr[i], arr[j] = arr[j], arr[i]

    arr[low] = arr[j]
    arr[j] = pivot_value

    # return the pivot index
    return j


def quick_sort_rec(a, low, high):
    if high > low:
        pivot_index = partition(a, low, high)
        quick_sort_rec(a, low, pivot_index - 1)
        quick_sort_rec(a, pivot_index + 1, high)


def quick_sort(a):
    quick_sort_rec(a, 0, len(a) - 1)


a = [55, 23, 26, 2, 18, 78, 23, 8, 2, 3]

print("Before Sorting")
print(a)

quick_sort(a)

print("After Sorting")
print(a)
