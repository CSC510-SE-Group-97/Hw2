"""
This module implements the merge sort algorithm using a recursive approach
and helper functions. It includes a `merge_sort` function for sorting arrays
and a `recombine` function to merge two sorted arrays.
"""

import rand


def merge_sort(arr):
    """
    Recursively sorts an array using the merge sort algorithm.

    Args:
        arr (list): The array to be sorted.

    Returns:
        list: The sorted array.
    """
    if len(arr) == 1:
        return arr

    half = len(arr)//2

    return recombine(merge_sort(arr[:half]), merge_sort(arr[half:]))


def recombine(left_arr, right_arr):
    """
    Merges two sorted arrays into one sorted array.

    Args:
        left_arr (list): The left half of the array, already sorted.
        right_arr (list): The right half of the array, already sorted.

    Returns:
        list: A new array with all elements from both input arrays, sorted.
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


a = rand.random_array([None] * 20)
arr_out = merge_sort(a)

print(arr_out)
