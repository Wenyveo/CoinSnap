# test_coinsnap.py
"""
Tests for CoinSnap module.
"""

import unittest
from coinsnap import CoinSnap

class TestCoinSnap(unittest.TestCase):
    """Test cases for CoinSnap class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CoinSnap()
        self.assertIsInstance(instance, CoinSnap)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CoinSnap()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
