import math

# To heapify subtree rooted at index i. n is size of heap
def heapify(array, n, i):
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # In our tree, left = 2*i + 1
    right = 2 * i + 2  # And right = 2*i + 2

    # See if left child of root exists and is greater than root
    if left < n and array[i] < array[left]:
        largest = left
 
    # See if right child of root exists and is greater than root
    if right < n and array[largest] < array[right]:
        largest = right
 
    # Change root, if needed
    if largest != i:
        (array[i], array[largest]) = (array[largest], array[i])  # swap
        # Heapify the root.
        heapify(array, n, largest)
 
# The main function to sort an array of given size
def heap_sort(array):
    n = len(array)
 
    # Step 1: Heap construction
    # Since last parent will be at floor(n/2) we can start at that location. -1 is to move to the index of the last element.
    for i in range(math.floor(n / 2), -1, -1):
        heapify(array, n, i)
 
    # Step 2: Extract elements one by one
    for i in range(n - 1, 0, -1):
        (array[i], array[0]) = (array[0], array[i])  # swap to move the largest element to the end
        heapify(array, i, 0)