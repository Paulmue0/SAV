import sort_alg_helper as sah


#Sorts array using bubblesort
def sort(arr):
	bubblesorted = False
	while(not bubblesorted):
		bubblesorted = True
		for i in range (arr.size -1):
			if arr[i] > arr[i+1]:
				sah.swap(arr, i, i+1)
				bubblesorted = False


def sort_step(arr):
	if(not sah.isSorted(arr)):
		pass