# Heap Sort

#### Analysis

As seen in the implementation (heap_sort.py) the time complexity of Heap Sort is dependant on the complexity of the heapify function.

There are 2 steps to heap sort that have to be considered when calculating it's complexity: the heap construction, and the extraction of elements.

In all cases, heap construction takes O(n) time. This is because although heapifying each node can take up to O(logn), the nodes closer to the bottom require less work than those at the top, since they have fewer children. This leads to an overall cost of O(n) after summing the work at each level of the tree.

As for the extraction phase, in it we repeatedly remove the largest element and place it at the end of the array. After each removal, the algorithm has to re-heapify the heap, which takes O(logn) time since it requires traversing the height of the tree. Since there are n elements, this leads to a total time of O(n logn)

#### Space Complexity

Heapsort is an in-place algorithm, so it does not require allocating additional information (except for a few variables), since the array itself is rearranged to represent the heap.

However, the present implementation of heapsort uses recursivity to heapify the tree, which requires O(logn) extra space in order to hold the recursive stack. This means that in the worst case, heapsort has a space complexity of O(logn) for this version, and O(1) in the best case.

#### Additional Overhead

There are additional overheads to consider when discussing quicksort: for one, it is not a stable sorting algorithm by default; the relative order of equal elements is not preserved. Implementing stability requires additional work and could lead to extra overhead, increasing memory and time complexity.

Heapsort is also known for exhibiting poor cache performance: it requires constant non-sequential access when heapifying the tree, since it has to jump to different positions of the array

#### Comparison

This is the benchmark code, which you can test by running "python main.py"

```
Random array of 10000 elements
Quick sort is the fastest
Quick sort time: 15.88 ms
Heap sort time: 33.99 ms
Merge sort time: 18.32 msAlready sorted array of 10000 elements
Quick sort is the fastest
Quick sort time: 16.45 ms
Heap sort time: 35.64 ms
Merge sort time: 18.28 msReverse sorted array of 10000 elements
Quick sort is the fastest
Quick sort time: 17.36 ms
Heap sort time: 31.60 ms
Merge sort time: 18.36 msRepeated elements array of 10000 elements
Merge sort is the fastest
Quick sort time: 110.41 ms
Heap sort time: 32.70 ms
Merge sort time: 19.66 msAll elements equal array of 10000 elements
Heap sort is the fastest
Quick sort time: 4928.03 ms
Heap sort time: 3.61 ms
Merge sort time: 19.26 ms
```

These results were unexpected: heap sort is consistently twice as slow as the other search algorithms, averaging at 30ms. It only won, by a large margin, on the "all elements equal" array, since it never needs to actually swap elements, which is one of its costliest operations. This is known for being one of the worst cases for both quick sort and merge sort.

I assume that the slower performance of heap sort in this case is due to its poor cache locality, and higher constant factors: The quick sort and merge sort implementations perform better in those cases.
