import unittest
from unittest.mock import Mock, MagicMock, patch

import requests

from practice import divide_two_numbers


class TestDivideTwoNumbers(unittest.TestCase):

    def test_smoke(self):
        result = divide_two_numbers(2, 2)
        self.assertEqual(result, 1)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide_two_numbers(2, 0)

    @unittest.skip('Cannot calculate')
    def test_skip_test(self):
        divide_two_numbers(6, 3)

    a = 1

    @unittest.skipIf(not a, 'the a is 1')
    def test_skipped(self):
        pass

    def mocked_get(*args, **kwargs):
        return 'You already know Python!'

    @patch("requests.get", side_effect=mocked_get)
    def test_mock(self, mock):
        link = 'https://teachmeskills.by/kursy/qa-avtomatizirovannoe-testirovanie-na-python-online'
        response = requests.get(link)

        self.assertEqual(response, 'You already know Python!')

