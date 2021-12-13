"""
Tests for the trending_prediction module
"""

import unittest
import pandas as pd
from utubetp.trending_prediction import *



class TestTrendingPred(unittest.TestCase):
    """Class for unittest."""
    df = pd.read_csv('../../data/US_youtube_trending_data.csv')

    def test_smoke(self):
        """Smoke test to ensure the function running."""
        df_cleaned = df_cleaning(df)
        get_video_ids(df_cleaned)
        output_video_dict(df_cleaned)
        get_current_trending(df_cleaned)
        get_current_ids(df_cleaned)
        output_current_dict(df_cleaned)
        pred_current_dict(df_cleaned)
        output_prediction(df_cleaned)
        return

    def test_one_shot(self):
        """One shot test to make sure the cleaned DataFrame has the correct schema"""
        df_cleaned = df_cleaning(df)
        assert list(df_cleaned.columns) == ['video_id', 'title', 'categoryId',
                                            'trending_date', 'view_count']
        return

    def test_edge_not_df(self):
        """
        Edge test with wrong type of data input, to see the function can throw a TypeError.
        """
        df_raw = [1, 2, 3, 4, 5]
        with self.assertRaises(TypeError):
            df_cleaning(df_raw)
        return

    def test_edge_not_cleaned(self):
        """
        Edge test with input of the original DataFrame, to see the function can throw a ValueError.
        """
        df_cleaned = df
        with self.assertRaises(ValueError):
            get_video_ids(df_cleaned)
        return
