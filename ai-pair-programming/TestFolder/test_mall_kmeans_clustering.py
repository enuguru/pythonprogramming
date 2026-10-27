import unittest
import pandas as pd
from mall_kmeans_clustering import load_data

class TestMallKMeansClustering(unittest.TestCase):
    def test_load_data(self):
        df = load_data('Mall_Customers.csv')
        self.assertIsInstance(df, pd.DataFrame)
        self.assertIn('Annual Income (k$)', df.columns)
        self.assertIn('Spending Score (1-100)', df.columns)
        self.assertIn('Age', df.columns)

if __name__ == "__main__":
    unittest.main()
