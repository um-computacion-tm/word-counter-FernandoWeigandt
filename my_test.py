import unittest
from Word_counters import *

class TestWordCount(unittest.TestCase):

    def test_1_word(self):

        resultado=word_counter('hola')

        self.assertEquals(resultado,{'hola': 1})

    def test_2_word(self):

        resultado=word_counter('hola hola')

        self.assertEquals(resultado,{'hola': 2})

    def test_3_word(self):

        resultado=word_counter('hola hola hola')

        self.assertEquals(resultado,{'hola': 3})

    def test_4_word(self):

        resultado=word_counter('hola hola hola hola')

        self.assertEquals(resultado,{'hola': 4})


if __name__ == '__main__':
    unittest.main()
