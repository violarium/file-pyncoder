import unittest
from lib.filters import *


class TestLibFilters(unittest.TestCase):
    def test_regexp_filters(self):
        """
        Test regexp filters
        """
        reg = '.*te?s(t|T)$'

        regexp_filter = match_regexp(reg)
        non_regexp_filter = do_not_match_regexp(reg)

        correct = ['test', 'hello_test', 'tsT']
        incorrect = ['Test', 'hello', 'tests']

        for item in correct:
            self.assertTrue(regexp_filter(item))
            self.assertFalse(non_regexp_filter(item))

        for item in incorrect:
            self.assertFalse(regexp_filter(item))
            self.assertTrue(non_regexp_filter(item))

    def test_extension_filters(self):
        """
        Text extension filters
        """
        extensions_list = 'jpeg,png,gif'

        ext_filter = has_extension(extensions_list)
        non_ext_filter = has_no_extension(extensions_list)

        correct = ['test.jpeg', 'test.png', 'test.gif']
        incorrect = ['test.txt', 'test.py', 'test.rb', 'test.php']
        for item in correct:
            self.assertTrue(ext_filter(item))
            self.assertFalse(non_ext_filter(item))
        for item in incorrect:
            self.assertFalse(ext_filter(item))
            self.assertTrue(non_ext_filter(item))