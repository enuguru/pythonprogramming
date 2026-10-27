import unittest
import pandas as pd
from mall_kmeans_clustering import plot_income_vs_spending, plot_age_vs_spending

class TestMallKMeansPlots(unittest.TestCase):
    def setUp(self):
        self.df = pd.DataFrame({
            'Annual Income (k$)': [15, 16, 17],
            'Spending Score (1-100)': [39, 81, 6],
            'Age': [19, 21, 20]
        })

    def test_plot_income_vs_spending(self):
        # Should not raise any exceptions
        plot_income_vs_spending(self.df)

    def test_plot_age_vs_spending(self):
        # Should not raise any exceptions
        plot_age_vs_spending(self.df)

if __name__ == "__main__":
    unittest.main()
