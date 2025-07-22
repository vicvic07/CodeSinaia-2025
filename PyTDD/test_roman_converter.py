import unittest
from roman_converter import roman_convertor

class TestInvalidInput(unittest.TestCase):
    # ======== Step 1 ======== no input, return None
    def test_no_input(self):
        self.assertEqual(roman_convertor(None), None)
    def test_string (self):
        self.assertEqual(roman_convertor('Imi place schaorma'), None)
    def test_decimal (self):
        self.assertEqual(roman_convertor(3.14), None)
    def test_range(self):
        self.assertEqual(roman_convertor (0), None)
    def test_range2(self):
        self.assertEqual(roman_convertor(4000), None)
    def test_1_5 (self):
        for i in range (1, 5):
            out=''
            num=i
            while (num):
                num=num-1
                out+='I'
            self.assertEqual (roman_convertor (i), out)
    def test_5 (self):
        self.assertEqual (roman_convertor (5), 'V')
    def test_50 (self):
        self.assertEqual (roman_convertor (50), 'L')