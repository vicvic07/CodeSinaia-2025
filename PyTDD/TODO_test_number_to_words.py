import unittest
from TODO_number_to_words import number_to_words

class TestNums(unittest.TestCase):
    
    # TODO
    # Adauga codul pentru unit tests aici
    def test_1 (self):
        self.assertEqual (number_to_words ('Imi place schaorma'), None)
    def test_2 (self):
        self.assertEqual (number_to_words (None), None)
    def test_3 (self):
        self.assertEqual (number_to_words (1), 1)