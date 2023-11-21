import requests

from words_function import join_words
import unittest
from unittest.mock import Mock, MagicMock, patch
import requests


def mocked_get(*args, **kwargs):
    return "badger-racoon"


class TestWordsFunction(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("A test suite begins")

    def setUp(self):
        print("A test beings")

    def test_simple_words(self):
        to_test = 'hello-world'
        result = join_words('hello', 'world')
        self.assertEqual(result, to_test)

    def test_simple_empty_rows(self):
        result = join_words('', '')
        self.assertEqual(result, '-')

    @unittest.skip('This test was skipped')
    def test_words_skip(self):
        result = join_words('one', 'two')
        self.assertEqual(result, 'one-two')

    @unittest.expectedFailure
    def test_expected_failed(self):
        result = join_words
        self.assertEqual(result, '123-word')

    def test_mock_racoon(self):
        mock = join_words
        mock.join_words = MagicMock(return_value="badger-racoon")

        self.assertEqual(mock.join_words('one','two'), "badger-racoon")




    def test_real_request(self):
        r = requests.get('https://google.com')
        result = r.status_code
        print(result)


    def tearDown(self):
        print("A test ends")

    @classmethod
    def tearDownClass(cls):
        print("A test suite ends")
