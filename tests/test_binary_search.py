import pytest
from algorithms.functions.binary_search.binary_search import binary_search

def test_binary_search_finds_sorted():
	items = [1, 3, 5, 7, 9]
	wanted = 7

	index = binary_search(items, wanted)
	assert index == 3

def test_binary_search_not_found_unsorted():
	items = [9, 3, 7, 5, 1]
	wanted = 3

	index = binary_search(items, wanted)
	assert index == None
