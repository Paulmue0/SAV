import numpy as np

# This module provides functions which will be used by most sorting-algorithms


def create_rand_array(size):
	return np.random.randint(-100, 100,size = size)

# Checks whether the array is sorted
def isSorted(arr):
	s = True
	for i in range (arr.size -1):
		if arr[i] > arr[i+1]:
			s = False
			break
	return s




#Swaps two position in an array
def swap(arr, x, y):
	tmp = arr[x]
	arr[x] = arr[y]
	arr[y] = tmp