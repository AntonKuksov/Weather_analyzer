import unittest

from .Weather_analyzer import is_not_number


class BtcPriceTestCase(unittest.TestCase):
    def test_checking_of_input_in_form(self):
        input = 46
        answer = is_not_number(input)  # The bitcoin returned changes over time!
        self.assertEqual(answer, False)