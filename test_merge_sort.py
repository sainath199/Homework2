# test_merge_sort.py

import pytest
from hw2_debugging import merge_sort

def test_merge_sort_empty():
    """Test merge sort on an empty array."""
    assert merge_sort([]) == []

def test_merge_sort_single():
    """Test merge sort on a single-element array."""
    assert merge_sort([1]) == [1]

def test_merge_sort_multiple():
    """Test merge sort on a multiple-element array."""
    assert merge_sort([3, 1, 2, 5, 4]) == [1, 2, 3, 4, 5]

def test_merge_sort_duplicates():
    """Test merge sort on an array with duplicate values."""
    assert merge_sort([4, 2, 4, 2, 1]) == [1, 2, 2, 4, 4]

