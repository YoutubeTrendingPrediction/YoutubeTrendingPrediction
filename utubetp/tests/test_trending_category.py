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

    def test_smoke(self):
     """
     The smoke test makes sure that the function runs well
     """
     df_category=pd.read_csv('./data/US_category_id.csv')
     df=pd.read_csv('./data/US_youtube_trending_data.csv')
     newdataframe= timesplit(df)
     preprocessframe=dataframecombine(newdataframe,df_category)
     outputframe1=splitcategory(preprocessframe)
     outputframe2=detailtimesplit(outputframe1)
     return
  

    def test_edge(self):
    """
    Edge test with wrong type of data input, to see if the function
    can throw a TypeError
    """
    df=pd.read_csv('../data/US_category_id.csv')
    randomdata=[a,b,c,d,3,4]
    with self.assertRaises(TypeError):
        timesplit(df)
        dataframecombine(randomdata,df)
        splitcategory(df)
        detailtimesplit(df)
