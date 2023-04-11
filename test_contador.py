import unittest
from contador import test_contador_palabras

class TestCountWords(unittest.TestCase):

    def test_simple(self):

        result = test_contador_palabras('hola')

        self.assertEqual(result, {'hola': 1})


    def test_complex(self):

        result = test_contador_palabras('hola como estas hola')

        self.assertEqual(

            result,

            {

                'hola': 2,

                'como': 1,

                'estas': 1,

            },

        )

if __name__ == '__main__':

    unittest.main()
        
