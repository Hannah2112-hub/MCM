import unittest
from src.Logica.OperacionesMatematicas import OperacionesMatematicas

class PruebaOperacionesMatematicas(unittest.TestCase):
    def setUp(self):
        self.operacion = OperacionesMatematicas()

    def tearDown(self):
        self.operacion = None

    def test_mcm_tresEnteros_retornaMCM(self):
        # Arrange
        numeros = [15, 20, 30]
        resultadoEsperado = 60

        # Do
        resultadoActual = self.operacion.mcm(numeros)

        # Assert
        self.assertEqual(resultadoEsperado, resultadoActual)

    def test_mcm_cuatroEnteros_retornaMCM(self):
        # Arrange
        numeros = [12, 15, 20, 30]
        resultadoEsperado = 60

        # Do
        resultadoActual = self.operacion.mcm(numeros)

        # Assert
        self.assertEqual(resultadoEsperado, resultadoActual)

    def test_mcm_variosNumeros_retornaMCM(self):
        # Arrange
        numeros = [2, 3, 5, 7, 11]
        resultadoEsperado = 2310

        # Do
        resultadoActual = self.operacion.mcm(numeros)

        # Assert
        self.assertEqual(resultadoEsperado, resultadoActual)

    def test_mcm_unNumeroCero_retornaException(self):
        # Arrange
        with self.assertRaises(ValueError):
            self.operacion.mcm([0, 5, 10])

    def test_mcm_dosNumerosCero_retornaException(self):
        # Arrange
        with self.assertRaises(ValueError):
            self.operacion.mcm([0, 0, 5])

if __name__ == '__main__':
    unittest.main()
