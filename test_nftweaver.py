# test_nftweaver.py
"""
Tests for NFTWeaver module.
"""

import unittest
from nftweaver import NFTWeaver

class TestNFTWeaver(unittest.TestCase):
    """Test cases for NFTWeaver class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NFTWeaver()
        self.assertIsInstance(instance, NFTWeaver)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NFTWeaver()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
