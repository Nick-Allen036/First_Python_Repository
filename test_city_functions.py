import unittest
from city_functions import FormatCityCountry

class CityCountryTestCase(unittest.TestCase):
    """Tests for city country formatting module"""
    
    def test_city_country_format(self):
        """Do city and country with a space between in title-case work"""
        formatted_city_country = FormatCityCountry('syracuse', 'new york')
        self.assertEqual(formatted_city_country, 'Syracuse, New York')
                         
if __name__ == '__main__':
    unittest.main()

