import blobs as blob
import plot

#Sorts array using selection-sort
def sort(arr):
	for i in range(arr.size):
		print(arr.size)
		min = i
		for j in range((i+1),(arr.size)):
			if arr[j] < arr[min]:
				min = j
			plot.redraw_plt(arr, "Selectionsort", x = i, y = j, z = min, col = 'green', col2 = 'blue')
		if i is not min:
			blob.swap(arr, i, min)

		





