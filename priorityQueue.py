import heapq

class PriorityQueue:
    def __init__(self):
        self.elements = []

    def push(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def pop(self):
        return heapq.heappop(self.elements)[1]

    def peek(self):
        return self.elements[0][1] if self.elements else None

    def is_empty(self):
        return len(self.elements) == 0

    def size(self):
        return len(self.elements)