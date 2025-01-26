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


# Part 2 Priority Queue Implementation and Applications
# Implementation of priority queue using linked list in python
# Importing heap queue algorithm that is available in python
import heapq


# Constructing a Task class
class Task:
    # Contructor
    def __init__(self, id, priority, arrivalTime, deadline):
        self.id = id
        self.priority = priority
        self.arrivalTime = arrivalTime
        self.deadline = deadline

    # Treat lower priority as higher priority as this is min heap
    def __lt__(self, other):
        return self.priority < other.priority

    def __repr__(self):
        return f"Task(ID={self.id}, Priority={self.priority}, arrivalTime={self.arrivalTime}, deadline={self.deadline})"


# Defining priority queue class with min heap
class PriorityQueue:
    def __init__(self):
        self.heap = []

    # A function to check if the priority queue is empty
    def size(self):
        return len(self.heap)

    def is_empty(self):
        return len(self.heap) == 0

    # Insert a new task into the priority queue
    def insertTask(self, task):
        heapq.heappush(self.heap, task)

    # In min heap the min value has the highest priority
    def extract_min(self):
        # Checking if the priority queue is not empty
        if self.is_empty():
            return None

        return heapq.heappop(self.heap)

    # decrease priority of existing task
    def decrease_key(self, id, newPriority):
        for i, task in enumerate(self.heap):
            if task.id == id:
                if newPriority > task.priority:
                    raise ValueError(
                        "New priority must be less than exising task priority"
                    )
                self.heap[i].priority = newPriority
                while i > 0 and self.heap[i] < self.heap[(i - 1) // 2]:
                    self.heap[i], self.heap[(i - 1) // 2] = (
                        self.heap[(i - 1) // 2],
                        self.heap[i],
                    )
                    i = (i - 1) // 2
                break

    # increase the priority of the existing task
    def increase_key(self, id, newPriority):
        for i, task in enumerate(self.heap):
            if task.id == id:
                if new_priority < task.priority:
                    raise ValueError(
                        "New priority must be greater than exising task priority"
                    )
                self.heap[i].priority = new_priority
                heapq.heapify(self.heap)
                break


# Test cases for priority queue
tasksQueue = PriorityQueue()

print("")
print("")
print(
    "********************************************************************************"
)
print("Priority queue implementation using min heap. Initializing empty priority queue")
print("Priority queue must be empty ", tasksQueue.is_empty())

# Inserting new tasks
startTime = time.time()
tasksQueue.insertTask(Task(1, 4, "09:00 AM", "09:30 AM"))
endTime = time.time()

print("")
print("Inserting a new tasks in the queue")
print(f"Execution time: {endTime - startTime:.6f} seconds")
print("New size of priority queue ", tasksQueue.size())

tasksQueue.insertTask(Task(2, 3, "01:00 AM", "01:30 AM"))
tasksQueue.insertTask(Task(3, 2, "05:00 AM", "07:00 AM"))
tasksQueue.insertTask(Task(4, 5, "10:00 PM", "11:30 PM"))
tasksQueue.insertTask(Task(5, 1, "02:00 PM", "03:30 PM"))

print("")
print("New size of priority queue after 4 more tasks added ", tasksQueue.size())
print("Priority queue is_empty method returns ", tasksQueue.is_empty())

# As this is a priority queue with min heap, the tasks with the lowest priority should pop first
print("")
print("Popping the priority queue")
startTime = time.time()
print(tasksQueue.extract_min())
endTime = time.time()
print(f"Execution time: {endTime - startTime:.6f} seconds")
print("New size of priority queue ", tasksQueue.size())

print("")
print("Popping all the elements of priority queue")
while not tasksQueue.is_empty():
    print(tasksQueue.extract_min())

print("")
print("New size of priority queue ", tasksQueue.size())
print("Priority queue must be empty ", tasksQueue.is_empty())

# Adding tasks again
tasksQueue.insertTask(Task(1, 5, "01:00 AM", "01:30 AM"))
tasksQueue.insertTask(Task(2, 4, "05:00 AM", "07:00 AM"))
tasksQueue.insertTask(Task(3, 9, "10:00 PM", "11:30 PM"))
tasksQueue.insertTask(Task(4, 1, "02:00 PM", "03:30 PM"))
tasksQueue.insertTask(Task(5, 2, "01:00 AM", "01:30 AM"))
tasksQueue.insertTask(Task(6, 3, "05:00 AM", "07:00 AM"))
tasksQueue.insertTask(Task(7, 6, "10:00 PM", "11:30 PM"))
tasksQueue.insertTask(Task(8, 7, "02:00 PM", "03:30 PM"))

print("")
print("Adding 8 tasks")
print("New size of priority queue ", tasksQueue.size())

# Decreasing the priory of task id 8 from 7 to 0
startTime = time.time()
tasksQueue.decrease_key(8, 0)
endTime = time.time()
print("")
print("Changing the priority of task 8 from 7 to 0, making its priority 0")
print(f"Execution time for decreasing the priority: {endTime - startTime:.6f} seconds")
print("Popping the priority queue. This should extract task with id 8")
print(tasksQueue.extract_min())
