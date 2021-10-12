import sort_alg_helper as sah
import bubble_sort as bs
import plot



# Main 

#Testing
states = sah.create_rand_array(10)
print(states)
bs.sort(states)
print(states)