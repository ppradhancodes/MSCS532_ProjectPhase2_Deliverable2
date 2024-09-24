# E-commerce Recommendation System

## Overview

This project implements a recommendation system for an e-commerce platform using Python. It utilizes key data structures such as hash tables, graphs, and priority queues to efficiently process and analyze user preferences and product data, providing personalized product recommendations.

## Features

- Hash Table: Stores user preferences and product information
- Graph: Represents relationships between users and products
- Priority Queue: Ranks recommendations based on relevance

## Requirements

- Python 3.x

## Installation

1. Clone the repository: git clone https://github.com/ppradhancodes/MSCS532_ProjectPhase1_Deliverable1.git

2. Navigate to the project directory: cd MSCS532_ProjectPhase1_Deliverable1

## Usage

To run the test script:

1. Ensure you're in the project directory
2. Run the following command:

This will execute a series of tests on the implemented data structures and the recommendation system.

## Implementation Details

### Hash Table
```python
class HashTable:
 def __init__(self):
     self.table = {}
 def insert(self, key, value):
     self.table[key] = value
 def get(self, key):
     return self.table.get(key)

class Graph:
    def __init__(self):
        self.graph = {}
    def add_edge(self, node1, node2, weight):
        if node1 not in self.graph:
            self.graph[node1] = {}
        self.graph[node1][node2] = weight
        if node2 not in self.graph:
            self.graph[node2] = {}
        self.graph[node2][node1] = weight
    def get_neighbors(self, node):
        return self.graph.get(node, {})


 import heapq

class PriorityQueue:
    def __init__(self):
        self.pq = []
    def push(self, item, priority):
        heapq.heappush(self.pq, (priority, item))
    def pop(self):
        return heapq.heappop(self.pq)[1]
    def is_empty(self):        
        return len(self.pq) == 0        
    