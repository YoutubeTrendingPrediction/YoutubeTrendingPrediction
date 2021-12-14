"""
Tests for the trending_tags module
"""

import unittest
import numpy as np
import trending_tags



class TestKnn(unittest.TestCase):

    def test_smoke(self):
        """
        Simple smoke test to make sure function runs.
        """
        tag_df = trending_tags.split_tags()
        trending_tags.select_year_and_month(tag_df,2021,2021,10,10)

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
        return

suite = unittest.TestLoader().loadTestsFromTestCase(TestKnn)
_ = unittest.TextTestRunner().run(suite)
# if __name__ == '__main__':
#     unittest.main()