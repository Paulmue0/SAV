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
				plot.redraw_plt(arr, "Bubblesort", x =i, y = i+1, col = 'green')
			else:
				plot.redraw_plt(arr, "Bubblesort", x =i, y = i+1, col = 'blue')
		index_last_sorted -= 1