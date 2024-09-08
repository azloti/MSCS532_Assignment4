# The Task class represents a task with an id and a priority.
class Task:
    def __init__(self, id, priority):
        self.id = id
        self.priority = priority

    def __str__(self):
        return f"Task: {self.id}, Priority: {self.priority}"

# The PriorityQueue class represents a priority queue implemented using a binary heap.
class PriorityQueue:
    def __init__(self):
        self.heap = []

    def __str__(self):
        return ", ".join(str(task) for task in self.heap)

    # Insert a task into the priority queue.
    def insert(self, task):
        self.heap.append(task) # Add the task to the end of the heap
        self._heapify_up(len(self.heap) - 1) # Heapify up from the last index

    # Extract the task with the maximum priority from the priority queue.
    def extract_max(self):
        if not self.heap:
            return None

        # Remove the task with the maximum priority
        max_task = self.heap[0]
        last_task = self.heap.pop()

        # If the heap is not empty, replace the root with the last task and heapify down
        if self.heap:
            self.heap[0] = last_task
            self._heapify_down(0)

        # Return the task with the maximum priority
        return max_task
    
    # Adjust the priority of a task in the priority queue.
    def adjust_priority(self, task_id, new_priority):

        # Find the task with the given id
        for index, task in enumerate(self.heap):
            if task.id == task_id:
                # Save the old priority and update the priority
                old_priority = task.priority
                task.priority = new_priority

                # Determine whether to heapify up or down
                if new_priority > old_priority:
                    self._heapify_up(index)
                else:
                    self._heapify_down(index)
                break

    # Check if the priority queue is empty.
    def is_empty(self):
        return len(self.heap) == 0 # Return True if the heap is empty

    # Heapify up the task at the given index. Heapify means to move the task up the heap until the heap property is satisfied.
    def _heapify_up(self, index):
        parent_index = (index - 1) // 2 # Start from the parent of the given index

        # Swap the task with its parent if the priority of the task is greater than the priority of the parent
        if parent_index >= 0 and self.heap[parent_index].priority < self.heap[index].priority:
            self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]

            # Recursively heapify up the parent
            self._heapify_up(parent_index)

    # Heapify down the task at the given index. Heapify means to move the task down the heap until the heap property is satisfied.
    def _heapify_down(self, index):
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        largest = index

        # Find the largest task among the task at the given index, the left child, and the right child
        if left_child_index < len(self.heap) and self.heap[left_child_index].priority > self.heap[largest].priority:
            largest = left_child_index

        # Compare the largest task with the right child
        if right_child_index < len(self.heap) and self.heap[right_child_index].priority > self.heap[largest].priority:
            largest = right_child_index

        # Swap the task with the largest task if the largest task is not the task at the given index
        if largest != index:
            self.heap[largest], self.heap[index] = self.heap[index], self.heap[largest]

            # Recursively heapify down the largest task
            self._heapify_down(largest)