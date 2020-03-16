import os
os.system('clear')
# TO-DO: Complete the selection_sort() function below


def selection_sort(arr):
    # for each element in the array (execpt for last)
    for i in range(0, len(arr) - 1):
        # initialize the smallest index to i
        smallest = i
        # for each element in the array beginning at i
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
    sorted = False
    while not sorted:
        sorted = True
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                sorted = False

        if sorted:
            return arr

# STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):

    return arr
