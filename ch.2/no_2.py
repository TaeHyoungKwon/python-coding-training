import unittest
from unittest.mock import Mock, patch


def input_word():
    return input('What is the input string? ')


def count_word():
    word = input_word()
    return '{} has {} characters'.format(word, str(len(word)))


@patch('no_2.input_word', Mock(return_value='abcde'))
class Test(unittest.TestCase):
    def test_count_word(self):
        self.assertEqual(count_word(), 'abcde has 5 characters')

    def test_input_word(self):
        actual = input_word()
        self.assertEqual(actual, 'abcde')
