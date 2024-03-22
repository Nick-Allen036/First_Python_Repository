from city_functions import FormatCityCountry
import pytest 

def test_first_last_name():
    formatted_name = FormatCityCountry('pittsburgh', 'pennsylvannia)')
    assert formatted_name == 'Janet Jackson' # statement assert, if True, goes to next line, else: error
    