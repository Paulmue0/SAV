import blobs as blob
import bubble_sort as bs
import selection_sort as ss
import insertion_sort as ins
import plot


# Main 

#Testing

states = blob.create_rand_array(20)
plot.draw_plt("Insertionsort", states)
print(states)
ins.sort(states)
print(states)
plot.show()

#Testing plotting



