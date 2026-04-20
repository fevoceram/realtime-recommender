import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

class Recommender:
    def __init__(self):
        np.random.seed(42)
        self.user_item_matrix = np.random.rand(100, 50)

    def recommend(self, user_id, top_k=5):
        similarity = cosine_similarity(
            [self.user_item_matrix[user_id]],
            self.user_item_matrix
        )[0]

        similar_users = similarity.argsort()[-top_k-1:-1][::-1]
        recommendations = self.user_item_matrix[similar_users].mean(axis=0)

        return recommendations.argsort()[-top_k:][::-1]
