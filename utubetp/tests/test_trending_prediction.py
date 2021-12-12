"""
Tests for the trending_prediction module
"""

import unittest
import numpy as np
from utubetp.trending_prediction import *



class TestKnn(unittest.TestCase):

    def test_smoke(self):
        """
        Simple smoke test to make sure function runs.
        """
        
        return

    def test_one_shot1(self):
        """
        One shot test.
        """
        
        return

    def test_one_shot2(self):
        """
        One shot test.
        """
        
        return

    def test_one_shot3(self):
        """
        One shot test3. 
        """
        
        return

    def test_edge_n_out_of_range(self):
        """
        Edge test to make sure the function throws a ValueError
        """
        
        return

    def test_edge_input_is_not_number(self):
        """
        Edge test to make sure the function throws a ValueError
        """
        

suite = unittest.TestLoader().loadTestsFromTestCase(TestKnn)
_ = unittest.TextTestRunner().run(suite)
# if __name__ == '__main__':
#     unittest.main()