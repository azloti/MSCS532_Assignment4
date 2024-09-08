import time
import sys
import random

from quick_sort import quick_sort
from heap_sort import heap_sort
from merge_sort import merge_sort

array_length = 10000

# 1. A random array of 100000 elements
random_array = random.sample(range(1, array_length + 1), array_length)

# 2. A sorted array
already_sorted = quick_sort(random_array)

# 3. A reverse sorted array
reverse_sorted = already_sorted[::-1]

# 4. An array with repeated elements: 100 elements randomly selected from the first 25 elements of the random array
repeated_elements = [random.choice(random_array[:50]) for _ in range(array_length)]

# 5. An array with all elements equal
all_elements_equal = [1 for _ in range(array_length)]


# Ok, all of our arrays are ready. Let's compare the running time of quick_sort with random and deterministic pivot selection for each of the arrays.
def test_sort_speed(name, array, function):
    start_time = time.time()
    sorted_array = function(array)
    end_time = time.time()

    time_in_ms = 1000 * (end_time - start_time)
    return time_in_ms

def test_all_algorithms(name, array):
    quick_time = test_sort_speed(name, array, quick_sort)
    heap_time = test_sort_speed(name, array, heap_sort)
    merge_time = test_sort_speed(name, array, merge_sort)

    print(f'{name} of {array_length} elements')
    # Sort by the fastest algorithm
    if quick_time < heap_time and quick_time < merge_time:
        print("Quick sort is the fastest")
    elif heap_time < quick_time and heap_time < merge_time:
        print("Heap sort is the fastest")
    else:
        print("Merge sort is the fastest")
    
    print(f'Quick sort time: {quick_time:.2f} ms')
    print(f'Heap sort time: {heap_time:.2f} ms')
    print(f'Merge sort time: {merge_time:.2f} ms')
    print()
    print()

# Increase the recursion limit, otherwise the code will throw RecursionError for large arrays
sys.setrecursionlimit(20000)

# Random array
test_all_algorithms("Random array", random_array)
test_all_algorithms("Already sorted array", already_sorted)
test_all_algorithms("Reverse sorted array", reverse_sorted)
test_all_algorithms("Repeated elements array", repeated_elements)
test_all_algorithms("All elements equal array", all_elements_equal)