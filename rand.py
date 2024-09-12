"""
This module provides a utility function to generate a randomized array
using the Unix 'shuf' command. It uses subprocess to run external commands 
to shuffle and select random numbers for an array.
"""

import subprocess


def random_array(arr):
    """
    Generates a randomized array by populating the given array with random integers.

    Args:
        arr (list): An empty list to populate with random numbers.

    Returns:
        list: The list populated with random integers.
    """
    shuffled_num = None
    for i, _ in enumerate(arr):
        shuffled_num = subprocess.run(
            ["shuf", "-i1-20", "-n1"], capture_output=True, check=True)
        arr[i] = int(shuffled_num.stdout)
    return arr
