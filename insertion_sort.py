import blobs as blob
import plot

#Sorts array using insertion-sort
def sort(arr):
	for i in range(arr.size-1):
		new_data = i + 1
		index_last_sorted = i
		for j in range(index_last_sorted+1, 0,-1):
			if arr[new_data] < arr[j-1]:
				blob.swap(arr, new_data, j-1)
				new_data -= 1
				plot.redraw_plt(arr, "Insertionsort", x = new_data, y = j-1, col = 'green')
			else:
				break

		


		





