# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(lhs, rhs):
    merged_list = []

    # while the length of the rhs and the lhs remain
    # above 0 - compare the first of each list and
    # append them in ascending order to the new
    # merged list
    while len(lhs) > 0 and len(rhs) > 0:
        if rhs[0] < lhs[0]:
            merged_list.append(rhs.pop(0))
        elif lhs[0] < rhs[0]:
            merged_list.append(lhs.pop(0))

    # if there are any remainders in the lhs
    # append them
    while len(lhs) > 0:
        merged_list.append(lhs.pop(0))
    # if there are any remainders in the rhs
    # append them as well
    while len(rhs) > 0:
        merged_list.append(rhs.pop(0))
    # return the merged_list
    return merged_list


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # base case
    if len(arr) == 1 or len(arr) == 0:
        return arr

    # recursive case
    else:
        middle = len(arr) // 2
        lhs = arr[:middle]
        rhs = arr[middle:]

        # divide lhs and rhs down further
        lhs = merge_sort(lhs)
        rhs = merge_sort(rhs)

        return merge(lhs, rhs)

# STRETCH: implement an in-place merge sort algorithm


def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
