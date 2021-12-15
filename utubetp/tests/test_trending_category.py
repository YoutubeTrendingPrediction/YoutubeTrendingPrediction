"""
Tests for the trending category module
"""

import unittest
import pandas as pd
from utubetp.trending_category import timesplit
from utubetp.trending_category import dataframecombine
from utubetp.trending_category import splitcategory
from utubetp.trending_category import detailtimesplit


class TestCategory(unittest.TestCase):
    """Class for unittest."""

    def test_smoke(self):
        """
        The smoke test makes sure that the function runs well
        """
        df_category = pd.read_csv('./data/US_category_id.csv')
        df_raw = pd.read_csv('./data/US_youtube_trending_data.csv')
        newdataframe = timesplit(df_raw)
        preprocessframe = dataframecombine(newdataframe,df_category)
        outputframe1 = splitcategory(preprocessframe)
        detailtimesplit(outputframe1)
        return

    def test_edge(self):
        """
        Edge test with wrong type of data input, to see if the function
        can throw a TypeError
        """
        df_raw = pd.read_csv('./data/US_category_id.csv')
        randomdata = [1, 5, 8, 0, 3, 4]
        with self.assertRaises(TypeError):
            timesplit(df_raw)
            dataframecombine(randomdata, df_raw)
            splitcategory(df_raw)
            detailtimesplit(df_raw)
