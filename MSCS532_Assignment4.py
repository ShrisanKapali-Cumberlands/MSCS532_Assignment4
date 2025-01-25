# MSCS 532 - Algorithms and Data Structures
# Shrisan kapali
# Student Id : 005032249
# Assignment 4 - Heap Data Structures: Implementation, Analysis, and Applications

import random
import time


# Implementation of Heap sort using max heap
# The process to main the max heap or min heap for the parent element in the tree is called heapify
def heapify(array, n, i):
    # Initializing current root index i as the largest element
    largest = i
    # We compare the left and right child index
    left = 2 * i + 1
    right = 2 * i + 2

    # Pick the higher value from left and right and replace with root if the child element > root
    if left < n and array[left] > array[largest]:
        largest = left

    if right < n and array[right] > array[largest]:
        largest = right

    # If the element at the child root is not greater, swap with the larger child index
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        # Heapify the parent and order the elements accordingly
        heapify(array, n, largest)


def heapSort(array):
    # Size of the array
    n = len(array)

    # Building the max heap
    for i in range(n // 2, -1, -1):
        heapify(array, n, i)

    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)


# Test cases
emptyArray = []
sortedArray = list(range(0, 500000))
reverseSortedArray = list(range(500000, 0, -1))
randomSortedArray = [random.randint(1, 5000) for _ in range(500000)]


# Running heap sort and calculating execution time
startTime = time.time()
heapSort(emptyArray)
endTime = time.time()
print("Running heapsort using max heapify on an empty array")
print(f"Execution time: {endTime - startTime:.6f} seconds")
# print(emptyArray)

# Already sorted array
startTime = time.time()
heapSort(sortedArray)
endTime = time.time()
print("")
print("Running heapsort using max heapify on an sorted array")
print(f"Execution time: {endTime - startTime:.6f} seconds")
# print(sortedArray)

# Reverse sorted array
startTime = time.time()
heapSort(reverseSortedArray)
endTime = time.time()
print("")
print("Running heapsort using max heapify on an reverse sorted array")
print(f"Execution time: {endTime - startTime:.6f} seconds")
# print(reverseSortedArray)

# Randomly sorted array
startTime = time.time()
heapSort(randomSortedArray)
endTime = time.time()
print("")
print("Running heapsort using max heapify on an reverse sorted array")
print(f"Execution time: {endTime - startTime:.6f} seconds")
# print(randomSortedArray)
