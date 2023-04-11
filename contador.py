import unittest

class testcontadordepalabras(unittest.TestCase):

    def test_contador_palabras(self):
        palabras = ["hola", "la", "casa", "la"]
        contador = {}
        for palabra in palabras:
            if palabra in contador:
                contador[palabra] += 1

            else:
                contador[palabra] = 1

        self.assertEqual(contador["hola"], 1)
        self.assertEqual(contador["la"], 2)
        self.assertEqual(contador["casa"], 1)

if __name__ == '__main__':
        unittest.main
