import blobs as blob
import bubble_sort as bs
import selection_sort as ss
import insertion_sort as ins
import plot
import communication as com

import sys

n = len(sys.argv)
print("Total arguments passed:", n)


# Main 




#Testing

states = blob.create_rand_array(20)
plot.draw_plt("Insertionsort", states)
print(states)
com.select_algorithm(sys.argv[1], states)
print(states)
plot.show()

#Testing plotting



