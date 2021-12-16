"""
Tests for the trending category module
"""

import unittest
import pandas as pd
from utubetp.trending_category import timesplit


class TestCategory(unittest.TestCase):
    """Class for unittest."""

    def test_smoke(self):
        """
        The smoke test makes sure that the function runs well
        """
        pd.read_csv('./data/US_category_id.csv')
        df_raw = pd.read_csv('./data/US_youtube_trending_data.csv')
        timesplit(df_raw)

    def test_edge(self):
        """
        Edge test with wrong type of data input, to see if the function
        can throw a TypeError
        """
        df_raw = [1, 2, 3, 4, 5]
        with self.assertRaises(TypeError):
            timesplit(df_raw)
