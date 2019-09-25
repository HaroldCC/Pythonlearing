import unittest

from country_codes import get_country_code


class CountryTestCase(unittest.TestCase):
    def funcname(self):
        """测试get_country_code"""
        country_name = get_country_code('United States')
        self.assertEqual(country_name, 'US')


unittest.main()
