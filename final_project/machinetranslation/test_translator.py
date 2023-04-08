import unittest
import translator

class TestTranslator(unittest.TestCase):
    def test_eng_to_french(self):
        self.assertEqual(translator.eng_to_french("Hello"), "Bonjour")
        self.assertEqual(translator.eng_to_french("I'm 24 years old"), "J'ai 24 ans")
        self.assertNotEqual(translator.eng_to_french("How are you?"), "None")

    def test_french_to_eng(self):
        self.assertEqual(translator.fench_to_eng("Bonjour"), "Hello")
        self.assertEqual(translator.fench_to_eng("J'ai 24 ans"), "I'm 24 years old")
        self.assertNotEqual(translator.fench_to_eng("Bonjour"), "None")

if __name__ == "__main__":
    unittest.main()
