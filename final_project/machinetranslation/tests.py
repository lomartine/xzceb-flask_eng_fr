import unittest
from translator import french_to_english, english_to_french

class test_en_to_fr(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french("Null"), "Null")
        self.assertEqual(english_to_french("Hello"), "Bonjour")

    def test2(self):
        self.assertEqual(french_to_english("Null"), "Null")
        self.assertEqual(french_to_english("Bonjour"), "Hello")

unittest.main()