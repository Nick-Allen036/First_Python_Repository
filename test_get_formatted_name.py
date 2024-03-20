import unittest
from city_functions import FormatCityCountry
from pcc_all_chapter_notes import get_formatted_name


class NameTestCase(unittest.TestCase):
    """Tests for name_function.py"""

    def test_first_last_name(self):  # method must start w/ test to run
        """Do names like 'Janice Joplin' work"""
        formatted_name = get_formatted_name('janice', 'joplin')
        self.assertEqual(formatted_name, 'Janice Joplin')

    # It's fine to have long descriptive test names
    def test_first_last_middle_name(self):
        """Do names like 'paul thomas anderson' work"""
        formatted_name = get_formatted_name('paul', 'anderson', 'thomas')
        self.assertEqual(formatted_name, 'Paul Thomas Anderson')


if __name__ == '__main__':  # so that only runs in main file, not frameworks
    unittest.main()


