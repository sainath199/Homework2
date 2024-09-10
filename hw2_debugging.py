"""
This module contains an implementation of the Merge Sort algorithm in Python, which is a
divide-and-conquer sorting algorithm.

"""

import rand

def merge_sort(input_arr):   # renamed 'arr' to 'input_arr'
    """
    Recursively splits the input array into halves and sorts them using merge sort.

    Args:
        input_arr (list): The array to be sorted.

    Returns:
        list: A sorted version of the input array.
    """
    if len(input_arr) == 1:
        return input_arr

    half = len(input_arr) // 2

    return recombine(merge_sort(input_arr[:half]), merge_sort(input_arr[half:]))


def recombine(left_arr, right_arr):
    """
    Merges two sorted arrays into one sorted array.

    Args:
        left_arr (list): The first sorted array.
        right_arr (list): The second sorted array.

    Returns:
        list: A merged and sorted array combining left_arr and right_arr.
    """
    left_index = 0
    right_index = 0
    merge_arr = [None] * (len(left_arr) + len(right_arr))
    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            right_index += 1
            merge_arr[left_index + right_index] = left_arr[left_index]
        else:
            left_index += 1
            merge_arr[left_index + right_index] = right_arr[right_index]

    for i in range(right_index, len(right_arr)):
        merge_arr[left_index + right_index] = right_arr[i]

    for i in range(left_index, len(left_arr)):
        merge_arr[left_index + right_index] = left_arr[i]

    return merge_arr


arr = rand.random_array([None] * 20)
arr_out = merge_sort(arr)

print(arr_out)
