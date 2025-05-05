import unittest
from tiy11_1 import describe_city

class TestCityCountry(unittest.TestCase):
    """Tests for tiy11_1."""
    def test_describe_city(self):
        """Are locations correctly formatted as 'City, Country'?"""
        formatted_location = describe_city('Paris', 'France')
        self.assertEqual(formatted_location, 'Paris, France')

if __name__ == '__main__':
    unittest.main()