import blobs as blob
import bubble_sort as bs
import plot


# Main 

#Testing

states = blob.create_rand_array(50)
plot.draw_plt('Bubblesort', states)
print(states)
bs.sort(states)
print(states)

#Testing plotting



