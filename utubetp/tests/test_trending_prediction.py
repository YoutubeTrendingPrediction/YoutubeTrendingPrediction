"""
Tests for the trending_prediction module
"""

import unittest
import pandas as pd
from utubetp.trending_prediction import df_cleaning
from utubetp.trending_prediction import get_current_ids
from utubetp.trending_prediction import get_current_trending
from utubetp.trending_prediction import get_video_ids
from utubetp.trending_prediction import output_current_dict
from utubetp.trending_prediction import output_prediction
from utubetp.trending_prediction import output_video_dict
from utubetp.trending_prediction import pred_current_dict


class TestTrendingPred(unittest.TestCase):
    """Class for unittest."""

    @classmethod
    def test_smoke(cls):
        """Smoke test to ensure the function running."""
        df_raw = pd.read_csv('./data/US_youtube_trending_data.csv')
        df_cleaned = df_cleaning(df_raw)
        get_video_ids(df_cleaned)
        output_video_dict(df_cleaned)
        get_current_trending(df_cleaned)
        get_current_ids(df_cleaned)
        output_current_dict(df_cleaned)
        pred_current_dict(df_cleaned)
        output_prediction(df_cleaned)

    @classmethod
    def test_one_shot(cls):
        """One shot test to make sure the cleaned DataFrame has the correct schema"""
        df_raw = pd.read_csv('./data/US_youtube_trending_data.csv')
        df_cleaned = df_cleaning(df_raw)
        assert list(df_cleaned.columns) == ['video_id', 'title', 'categoryId',
                                            'trending_date', 'view_count']

    def test_edge_not_df(self):
        """
        Edge test with wrong type of data input, to see the function can throw a TypeError.
        """
        df_raw = [1, 2, 3, 4, 5]
        with self.assertRaises(TypeError):
            df_cleaning(df_raw)

    def test_edge_not_cleaned(self):
        """
        Edge test with input of the original DataFrame, to see the function can throw a ValueError.
        """
        df_raw = pd.read_csv('./data/US_youtube_trending_data.csv')
        df_cleaned = df_raw
        with self.assertRaises(ValueError):
            get_video_ids(df_cleaned)
