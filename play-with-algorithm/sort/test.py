import my_sort as s
import numpy as np
import time
n = 5000
def test_data(n):
    return list(np.random.randint(n,size=n))
name = 'selection sort'
s.selectionSort(name, test_data(n))
# s.selectionSortQuick(name, test_data)

name = 'insertion sort'
s.insertion_sort(name, test_data(n))

name = 'insertion sort optimal'
s.insertion_sort_optimal(name, test_data(n))

name = 'bubble sort'
s.bubble_sort(name, test_data(n))

name = 'shell sort'
s.shell_sort(name, test_data(n))

name = 'merge sort'
start_time = time.time()
s.merge_sort(test_data(n))
end_time = time.time()
print(name+':'+str(end_time-start_time))