# Priority Queue

#### Chosen data structure (array)

An array is the best data structure for creating a priority queue for many reasons, being both efficient and easy to implement.

First of all, a binary heap can be easily represented in an array: the relationship between a parent and a child can be derived in O(1) using array indices: The parent index of a node will always be `(i - 1) // 2`. While the children of an index will be `2 * i + 1` and ` 2 * i + 2`.

This makes navigating the tree structure simple, fast, and allows for easy manipulation during heapify operations such as swapping nodes.

Using an array also minimizes overhead, since there's no extra space required for pointers, and allows dynamic resizing of the array if needed.

#### Efficiency of Heap Operations

###### Insertions

Adding an element requires adding it to the end of the array, achieved in O(1), and then performing a heapify_up operation which restores the heap property. Restoring requires exponentially fewer nodes as we move further up the tree, leading to a complexity of O(log(n)).

###### Adjusting priority

Adjusting the priority requires scanning the array for the existing tasks, which is an O(n) operation. Once the task is found, an additional heapify_up or heapify_down operation is needed, both of which are O(logn) operations as explained above. This leads to a total complexity of O(logn)

###### Extracting the maximum value

Extracting the maximum element is also an efficient operation. The last element of the array is moved to the root, and then another heapify_down operation restores the heap property in O(logn) time.

#### Implementation details

You can find the full implementation of both the priority queue and the task class in the priority_queue.py file.

The task class is quite simple: it only contains an ID and a priority for the task. The priority is used by the queue to determine the order of the items inside the heap.

The priority task, as detailed above, is based on an array for ease of implementation. Most of the functions depend on the heapify_down and heapify_up functions.

The heapify_up function, mostly used when inserting new elements, calculates the parent index of the current index, which is just (index - 1) // 2. It then checks whether the current task's priority is higher than the parent, which violates the heap property. When that happens, a swap between the 2 elements occurs, and then heapify_up is called recursively to ensure that the heap property is maintained in subsequent levels.

Similarly, the heapify_down is used primarily after extracing the root of the heap, which is the highest priority task. When the root is removed, the last task in the heap is moved to the root, which usually violates the heap property. heapify_down checks both children of the current index, and picks the largest one to swap. This ensures that the largest index always "swims up" to the root position in the array.

After finding the largest one and swapping to it, it calls itself recursively for that index, ensuring that the heap property will again be maintained at all levels.

#### Analysis of the scheduling results

The scheduling results demonstrate that the priority queue works correctly. I inserted six tasks with different priorities, then adjusted the priority of Task 2 from 5 to 35. That triggered a heapify_up operation, moving task 2 up to the root since it now has the highest priority.

Afterwards, I extracted 3 tasks. Task 2 (35) was extracted first, followed by Task 6 (30) and then 5 (25). Every time a task is extracted, heapify_down is called to ensure that the heap proprty is maintained, and the highest priority task is moved to the root.

The assertions confirm the correct behaviour of the queue.
