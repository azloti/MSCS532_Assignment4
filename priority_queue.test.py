from priority_queue import PriorityQueue, Task

pq = PriorityQueue()
pq.insert(Task(1, 10))
pq.insert(Task(4, 20))
pq.insert(Task(2, 5))
pq.insert(Task(6, 30))
pq.insert(Task(3, 15))
pq.insert(Task(5, 25))

pq.adjust_priority(2, 35)

assert pq.extract_max().id == 2
assert pq.extract_max().id == 6
assert pq.extract_max().id == 5

print("All tests passed!")
