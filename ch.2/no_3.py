import unittest
from unittest.mock import patch, Mock


def input_name():
    return input('Who said it? ')


def input_quote():
    return input('What is the quote? ')


def print_double_quote():
    return f"{input_name()} says, \"{input_quote()}\""
    

class TestDoubleQuote(unittest.TestCase):

    @patch('no_3.input_name', Mock(return_value='THKwon'))
    @patch('no_3.input_quote', Mock(return_value='Do code so hard.'))
    def test_print_double_quote(self):
        self.assertEqual(print_double_quote(), "THKwon says, \"Do code so hard.\"")
