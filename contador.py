import unittest

def test_contador_palabras(phrase):
        contador = {}
        for palabra in phrase.split(' '):
            if palabra in contador:
                contador[palabra] += 1

            else:
                contador[palabra] = 1

        return contador
if __name__ == '__main__':

    unittest.main()
