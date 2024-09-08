import time
import sys
import random

from quick_sort import quick_sort
from heap_sort import heap_sort

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
    print(function.__name__, name, f"Time: {time_in_ms:.2f} ms")
    return end_time - start_time

def test_both_algorithms(name, array):
    quick_time = test_sort_speed(name, array, quick_sort)
    heap_time = test_sort_speed(name, array, heap_sort)

    diff_in_ms = (quick_time - heap_time) * 1000
    if diff_in_ms > 0:
        print("Heap sort is faster by ", diff_in_ms, " milliseconds")
    else:
        print("Quick sort is faster by ", -diff_in_ms, " milliseconds")
    print()

# Increase the recursion limit, otherwise the code will throw RecursionError for large arrays
sys.setrecursionlimit(20000)

# Random array
test_both_algorithms("Random array", random_array)
test_both_algorithms("Already sorted array", already_sorted)
test_both_algorithms("Reverse sorted array", reverse_sorted)
test_both_algorithms("Repeated elements array", repeated_elements)
test_both_algorithms("All elements equal array", all_elements_equal)