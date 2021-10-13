import blobs as blob
import plot

#Sorts array using bubblesort
def sort(arr):
	bubblesorted = False
	index_last_sorted = arr.size - 1
	while(not bubblesorted):
		bubblesorted = True
		for i in range(index_last_sorted):
			if arr[i] > arr[i+1]:
				blob.swap(arr, i, i+1)
				bubblesorted = False
				plot.redraw_plt(arr, i, i+1, 'green')
			else:
				plot.redraw_plt(arr, i, i+1, 'gray')
		index_last_sorted -= 1