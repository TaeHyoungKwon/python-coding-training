import unittest


def hello_world():

    def _input_name():
        return input('What is your name?')

    def _get_hello_world(name):
        return 'Hello, {name}, nice to meet you!'.format(name=name)

    def _print_hello_world(string):
        return string

    return _print_hello_world(_get_hello_world(_input_name()))


class TestHelloWorld(unittest.TestCase):
    def test_hello_world(self):
        actual = hello_world()
        self.assertEqual(actual, 'Hello, Brian, nice to meet you!')

