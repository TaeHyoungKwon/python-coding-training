import unittest
from unittest.mock import patch, Mock


def input_noun():
    return input('Enter a noun: ')


def input_verb():
    return input('Enter a verb: ')


def input_adjective():
    return input('Enter a adjective: ')


def input_adverb():
    return input('Enter a adjective: ')


def print_sentence():
    verb = input_verb()
    adjective = input_adjective()
    noun = input_noun()
    adverb = input_adverb()
    return f'Do you {verb} your {adjective} {noun} {adverb}? That\'s hilarious!'


class TestMadLibs(unittest.TestCase):
    @patch('no_4.input_noun', Mock(return_value='dog'))
    @patch('no_4.input_verb', Mock(return_value='walk'))
    @patch('no_4.adjective', Mock(return_value='blue'))
    @patch('no_4.adverb', Mock(return_value='quickly'))
    def test_mad_libs(self):
        actual = print_sentence()
        self.assertEqual(actual, 'Do you walk your blue dog quickly? That\'s hilarious!')
