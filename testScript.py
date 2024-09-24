from hashTable import HashTable
from graph import Graph
from priorityQueue import PriorityQueue
from recommendationSystem import RecommendationSystem

def test_hash_table():
    print("Testing Hash Table:")
    ht = HashTable()
    
    # Test insertion and retrieval
    ht.insert("user1", {"product1": 5, "product2": 4})
    ht.insert("user2", {"product2": 3, "product3": 5})
    
    print("User1 preferences:", ht.get("user1"))
    print("User2 preferences:", ht.get("user2"))
    
    # Test updating existing key
    ht.insert("user1", {"product1": 5, "product2": 4, "product3": 3})
    print("Updated User1 preferences:", ht.get("user1"))
    
    # Test non-existent key
    try:
        print(ht.get("user3"))
    except KeyError:
        print("KeyError raised for non-existent user")
    
    # Test deletion
    ht.delete("user2")
    try:
        print(ht.get("user2"))
    except KeyError:
        print("User2 successfully deleted")

def test_graph():
    print("\nTesting Graph:")
    g = Graph()
    
    # Test adding edges
    g.add_edge("product1", "product2", 0.8)
    g.add_edge("product1", "product3", 0.6)
    g.add_edge("product2", "product4", 0.7)
    
    # Test getting neighbors
    print("Neighbors of product1:", g.get_neighbors("product1"))
    print("Neighbors of product2:", g.get_neighbors("product2"))
    
    # Test non-existent node
    print("Neighbors of non-existent product:", g.get_neighbors("product5"))
    
    # Test removing edge
    g.remove_edge("product1", "product2")
    print("Neighbors of product1 after removing edge:", g.get_neighbors("product1"))
    
    # Test getting all nodes
    print("All nodes in the graph:", g.get_all_nodes())

def test_priority_queue():
    print("\nTesting Priority Queue:")
    pq = PriorityQueue()
    
    # Test pushing items
    pq.push("product1", 5)
    pq.push("product2", 3)
    pq.push("product3", 4)
    
    # Test popping items
    print("Popped item:", pq.pop())
    print("Popped item:", pq.pop())
    
    # Test peeking
    pq.push("product4", 2)
    print("Peeked item:", pq.peek())
    
    # Test is_empty and size
    print("Is queue empty?", pq.is_empty())
    print("Queue size:", pq.size())
    
    # Pop remaining items
    while not pq.is_empty():
        print("Popped item:", pq.pop())
    
    print("Is queue empty now?", pq.is_empty())

def test_recommendation_system():
    print("\nTesting Recommendation System:")
    rs = RecommendationSystem()
    
    # Add user preferences
    rs.add_user_preference("user1", "product1", 5)
    rs.add_user_preference("user1", "product2", 4)
    rs.add_user_preference("user2", "product2", 3)
    rs.add_user_preference("user2", "product3", 5)
    
    # Add product relations
    rs.add_product_relation("product1", "product3", 0.8)
    rs.add_product_relation("product1", "product4", 0.6)
    rs.add_product_relation("product2", "product4", 0.7)
    rs.add_product_relation("product2", "product5", 0.5)
    
    # Generate recommendations
    recommendations_user1 = rs.generate_recommendations("user1")
    print("Recommendations for user1:", recommendations_user1)
    
    recommendations_user2 = rs.generate_recommendations("user2")
    print("Recommendations for user2:", recommendations_user2)
    
    # Test non-existent user
    recommendations_user3 = rs.generate_recommendations("user3")
    print("Recommendations for non-existent user:", recommendations_user3)

if __name__ == "__main__":
    test_hash_table()
    test_graph()
    test_priority_queue()
    test_recommendation_system()