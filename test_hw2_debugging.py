# test_hw2_debugging.py
import pytest
from hw2_debugging import merge_sort

def test_sorted_array():
    """Test sorting an already sorted array."""
    arr = [1, 2, 3, 4, 5]
    assert merge_sort(arr) == [1, 2, 3, 4, 5]

def test_random_array():
    """Test sorting an unsorted array."""
    arr = [5, 2, 9, 1, 5, 6]
    assert merge_sort(arr) == [1, 2, 5, 5, 6, 9]

def test_array_with_duplicates():
    """Test sorting an array with duplicate values."""
    arr = [4, 5, 4, 3, 2, 5]
    assert merge_sort(arr) == [2, 3, 4, 4, 5, 5]
