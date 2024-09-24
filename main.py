from MSCS532_ProjectPhase2_Deliverable2 import recommendationSystem

# Create a recommendation system
rec_system = recommendationSystem()

# Add user preferences
rec_system.add_user_preference("user1", "product1", 5)
rec_system.add_user_preference("user1", "product2", 4)
rec_system.add_user_preference("user1", "product3", 3)

# Add product relations
rec_system.add_product_relation("product1", "product4", 0.8)
rec_system.add_product_relation("product1", "product5", 0.6)
rec_system.add_product_relation("product2", "product6", 0.7)

# Generate recommendations for user1
recommendations = rec_system.generate_recommendations("user1")
print("Recommendations for user1:", recommendations)