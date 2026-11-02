import unittest

from generador import Generador


class GeneradorTests(unittest.TestCase):
    def test_genera_la_secuencia_con_los_parametros_del_trabajo(self):
        generador = Generador()

        self.assertAlmostEqual(generador.generar(), 2339 / 3922)
        self.assertEqual(generador.estado, 2339)
        self.assertAlmostEqual(generador.generar(), 1983 / 3922)
        self.assertEqual(generador.estado, 1983)

    def test_rechaza_modulo_no_positivo(self):
        with self.assertRaises(ValueError):
            Generador(m=0)

    def test_rechaza_semilla_fuera_del_modulo(self):
        with self.assertRaises(ValueError):
            Generador(x0=3922)


if __name__ == "__main__":
    unittest.main()
