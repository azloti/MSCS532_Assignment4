import random

def partition(source, low, high):
    pivot_index = random.randint(low, high) # Choose a random pivot_index

    pivot = source[pivot_index] # Get the pivot value
    source[pivot_index], source[high] = source[high], source[pivot_index] # Swap the pivot value with the last element
    i = low - 1 

    for j in range(low, high): # For each element in the source
        if source[j] <= pivot: # If the element is less than the pivot
            i += 1 # Move the index of the smaller element
            source[i], source[j] = source[j], source[i] # Swap the smaller element with the element at the index

    source[i + 1], source[high] = source[high], source[i + 1] # Swap the pivot value with the element at the index
    return i + 1

def quicksort(source, low, high):
    if low < high: # If the source has more than one element
        pivot_index = partition(source, low, high) # Partition the source
        quicksort(source, low, pivot_index - 1) # Sort the left side of the source
        quicksort(source, pivot_index + 1, high) # Sort the right side of the source

def quick_sort(source): 
    copy = source.copy() # Create a copy of the source
    quicksort(copy, 0, len(source) - 1) # Sort the copy
    return copy