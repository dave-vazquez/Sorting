import os
os.system('clear')


def selection_sort(arr):
    # for each element in the list (execpt for last)
    for i in range(0, len(arr) - 1):
        # initialize the smallest index to i
        smallest = i
        # for each element in the list beginning at i
        for j in range(i, len(arr)):
            # if an element is smaller than the smallest
            if(arr[j] <= arr[smallest]):
                # store the new smallest index
                smallest = j
        # swap the current index with the smallest
        arr[i], arr[smallest] = arr[smallest], arr[i]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # initializes sorted to False so loop can start
    sorted = False
    while not sorted:
        # sorting is true until a swap occurs
        sorted = True
        # loop through the list up until the last index
        # if you keep it you wind up comparing the last
        # index to an index out of bounds
        for i in range(0, len(arr) - 1):
            # if the element is larger than the one to its right
            if arr[i] > arr[i+1]:
                # swap
                arr[i], arr[i+1] = arr[i+1], arr[i]
                sorted = False
        # only when a full pass through the list occurs
        # without any swaps can the list be considered sorted
        if sorted:
            return arr

# STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):
    count_array = [0] * len(arr)

    for i, el in enumerate(arr):
        count_array[el] = arr[i]

    return count_array


array = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]

result = count_sort(array)

print(result)
