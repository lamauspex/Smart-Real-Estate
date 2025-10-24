# apps/ml/services.py
from .models import Property
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd


class RecommendationService:
    def __init__(self):
        self.similarity_matrix = None
        self.properties_df = None

    def build_similarity_matrix(self):
        properties = Property.objects.all().values()
        df = pd.DataFrame(properties)

        # Создаем признаки для похожести
        features = pd.get_dummies(df[['property_type', 'area', 'price']])
        self.similarity_matrix = cosine_similarity(features)
        self.properties_df = df

    def get_similar_properties(self, property_id, limit=5):
        if self.similarity_matrix is None:
            self.build_similarity_matrix()

        prop_idx = self.properties_df[self.properties_df['id']
                                      == property_id].index[0]
        similar_scores = list(enumerate(self.similarity_matrix[prop_idx]))
        similar_scores = sorted(
            similar_scores, key=lambda x: x[1], reverse=True)

        similar_properties = []
        for i, score in similar_scores[1:limit+1]:
            prop_id = self.properties_df.iloc[i]['id']
            similar_properties.append(Property.objects.get(id=prop_id))

        return similar_properties
