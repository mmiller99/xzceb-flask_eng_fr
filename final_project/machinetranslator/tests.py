import unittest
import sys

#from machinetranslator import translator

from translator import englishToFrench, frenchtoEnglish

class TestEnglishToFrench(unittest.TestCase):
    def test_null_input(self):
        self.assertIsNotNone(englishToFrench(None))
    def test_e_to_f(self):
        self.assertEqual(englishToFrench("Hello"), "Bonjour")

class TestFrenchToEnglish(unittest.TestCase):
    def test_null_input(self):
        self.assertIsNotNone(frenchtoEnglish(None))
    def test_f_to_e(self):
        self.assertEqual(frenchtoEnglish("Bonjour"), "Hello")

unittest.main()