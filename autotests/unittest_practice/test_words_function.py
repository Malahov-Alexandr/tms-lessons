import requests
import datetime
from words_function import join_words
import unittest
from unittest.mock import Mock, MagicMock, patch


def current_day():
    days = ['Monday', 'Wednesday', 'Friday']
    the_day = datetime.datetime.now().strftime("%A")
    if the_day in days:
        return True


today = current_day()


def mocked_get(*args, **kwargs):
    return "badger-racoon"


def mocked_status_code(*args, **kwargs):
    return 404


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

    @patch("requests.get", side_effect=mocked_get)
    def test_mocked_google_search(self, mock):
        link = 'https://www.google.com/search?q=badger'
        response = requests.get(link)
        expected_result = "badger-racoon"
        self.assertIn(expected_result, response)

    @unittest.skipIf(today, "Today is not a good day")
    def test_skipped_if_condition(self):
        pass

    def tearDown(self):
        print("A test ends")

    @classmethod
    def tearDownClass(cls):
        print("A test suite ends")
