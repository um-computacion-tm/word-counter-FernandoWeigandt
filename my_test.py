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

    def test_5_word(self):

        resultado=word_counter('hola soy carlos Y este Es mi test soy numero 465476')

        self.assertEquals(resultado, {'hola': 1, 'soy': 2, 'carlos': 1, 'Y': 1, 'este': 1, 'Es': 1, 'mi': 1, 'test': 1, 'numero': 1, '465476': 1})

if __name__ == '__main__':
    unittest.main()
