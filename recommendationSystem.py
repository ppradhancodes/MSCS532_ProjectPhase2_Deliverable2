from graph import Graph
from hashTable import HashTable
from priorityQueue import PriorityQueue

class RecommendationSystem:
    def __init__(self):
        self.user_preferences = HashTable()
        self.product_graph = Graph()
        self.recommendations = PriorityQueue()

    def add_user_preference(self, user_id, product_id, rating):
        if self.user_preferences.get(user_id) is None:
            self.user_preferences.insert(user_id, {})
        user_prefs = self.user_preferences.get(user_id)
        user_prefs[product_id] = rating
        self.user_preferences.insert(user_id, user_prefs)

    def add_product_relation(self, product1, product2, strength):
        self.product_graph.add_edge(product1, product2, strength)

    def generate_recommendations(self, user_id):
        user_prefs = self.user_preferences.get(user_id)
        if user_prefs is None:
            return []

        for product_id, rating in user_prefs.items():
            related_products = self.product_graph.get_neighbors(product_id)
            for related_product, relation_strength in related_products.items():
                if related_product not in user_prefs:
                    recommendation_score = rating * relation_strength
                    self.recommendations.push(related_product, -recommendation_score)

        top_recommendations = []
        while not self.recommendations.is_empty() and len(top_recommendations) < 5:
            top_recommendations.append(self.recommendations.pop())

        return top_recommendations