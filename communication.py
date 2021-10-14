import bubble_sort as bs
import selection_sort as ss
import insertion_sort as ins

def select_algorithm(str, states):
	str1 = "bubblesort"
	if (str.casefold()).__eq__("bubblesort".casefold()):
		bs.sort(states)
	elif (str.casefold()).__eq__("selectionsort".casefold()):
		ss.sort(states)
	elif (str.casefold()).__eq__("insertionsort".casefold()):
		ins.sort(states)
	else:
		print("invalid input:")
		print(str)