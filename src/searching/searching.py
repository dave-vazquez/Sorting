import os
os.system("clear")
# STRETCH: implement Linear Search


def linear_search(arr, target):

    for i in range(0, len(arr)):
        if target == arr[i]:
            return i

    return -1   # not found


# STRETCH: write an iterative implementation of Binary Search
def binary_search(arr, target):

    if len(arr) == 0:
        return -1  # array empty

    low = 0
    high = len(arr)-1

    while low <= high:
        middle = (low + high) // 2
        if target < arr[middle]:
            high = middle - 1  # eliminate RHS
        elif target > arr[middle]:
            low = middle + 1  # eliminate LHS
        else:
            return middle
    return -1  # not found


# STRETCH: write a recursive implementation of Binary Search
def binary_search_recursive(arr, target, low, high):
    # find the middle
    middle = (low+high) // 2
    # base case: array is no length
    if len(arr) == 0:
        return -1
    # recursive case: target is less than the middle element
    if target < arr[middle]:
        # adjust high so it's one index behind the middle
        high = middle - 1
        # recursive binary search: return statement required to
        # pass result down the call stack
        return binary_search_recursive(arr, target, low, high)
    elif target > arr[middle]:
        # adjust low so it's one index ahead of the middle
        low = middle + 1
        # recursive binary search: return statement required to
        # pass result down the call stack
        return binary_search_recursive(arr, target, low, high)
    # returns middle index if target is neither lower or
    # higher than the middle element...
    # in otherwords, they're equal
    return middle
