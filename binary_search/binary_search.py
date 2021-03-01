'''

data and target are the input parameters to binary_search_iterative function. data is the array in which we are searching, and target is the value that we are searching for. On lines 2-3, low and high are initialized to 0 and len(data) - 1 respectively. Based on the assumption that data is a sorted list, low and high have been assigned as the indices for the minimum and the maximum values in data.

Next, the while loop on line 5 will run until low is less than or equal to high. On line 6, mid is calculated by dividing the sum of low and high by 2 and getting the floored value because of the // operator. As specified before, target will be compared to the middle element, which is what happens on line 7. If target is equal to data[mid] (the middle element), it implies target exists in data and True is returned from the function as an indication. On the other hand, if target is less than the middle element, it means that target is somewhere in the first half of the array as the array is sorted. Therefore, we set high to mid - 1, i.e., the upper bound of the chunk of the array to be searched will be at a position to the left of mid. In contrast, if target is greater than data[mid], target must be in the second half of the array, so the lower bound (low) is set to mid + 1.

In general, we keep dividing the array into halves in the binary search instead of iterating through all the elements to search for the target element. This implies that it takes O(log n)O(logn) steps to divide into halves until we reach a single element. As a result, the worst-case time complexity of a binary search is O(log n)O(logn).
'''





# Linear Search
def linear_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return True
    return False


# Iterative Binary Search
def binary_search_iterative(data, target):
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False


# Recursive Binary Search 
def binary_search_recursive(data, target, low, high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search_recursive(data, target, low, mid - 1)
        else:
            return binary_search_recursive(data, target, mid + 1, high)


data = [2, 4, 5, 7, 8, 9, 12, 14, 17, 19, 22, 25, 27, 28, 33, 37]
target = 37

print(binary_search_recursive(data, target, 0, len(data) - 1))
print(binary_search_iterative(data, target))
