import unittest

from empleada import Empleada
from fotografia import Fotografia
from pintura import Pintura
from visitante import EstadoVisitante, Visitante
from ventanilla import Ventanilla


class EntidadesTests(unittest.TestCase):
    def test_visitante_recorre_ventanilla_fotografia_y_pintura(self):
        visitante = Visitante(id=1, puerta_ingreso="A", hora_ingreso=9)
        ventanilla = Ventanilla(numero=1)
        ventanilla.habilitar()
        ventanilla.agregar_visitante(visitante)
        empleada = Empleada(id=1, ventanilla=ventanilla)

        self.assertIs(empleada.atender_siguiente(), visitante)
        self.assertTrue(empleada.ocupada)
        self.assertIs(empleada.finalizar_atencion(), visitante)
        self.assertEqual(visitante.estado, EstadoVisitante.EN_SALA_FOTOGRAFIA)

        fotografia = Fotografia()
        fotografia.ingresar(visitante)
        self.assertEqual(fotografia.cantidad_personas, 1)
        fotografia.salir(visitante, ir_a_pintura=True)

        pintura = Pintura()
        pintura.ingresar(visitante)
        pintura.salir(visitante)

        self.assertEqual(visitante.estado, EstadoVisitante.RETIRADO)
        self.assertEqual(fotografia.cantidad_personas, 0)
        self.assertEqual(pintura.cantidad_personas, 0)
        self.assertFalse(empleada.ocupada)

    def test_ventanilla_deshabilitada_no_acepta_visitantes(self):
        ventanilla = Ventanilla(numero=1)
        visitante = Visitante(id=1, puerta_ingreso="B", hora_ingreso=10)

        with self.assertRaises(ValueError):
            ventanilla.agregar_visitante(visitante)

    def test_pintura_rechaza_ingreso_al_superar_capacidad(self):
        pintura = Pintura(capacidad=1)
        visitante_1 = Visitante(id=1, puerta_ingreso="A", hora_ingreso=9)
        visitante_2 = Visitante(id=2, puerta_ingreso="B", hora_ingreso=9)
        visitante_1.estado = EstadoVisitante.EN_SALA_PINTURA
        visitante_2.estado = EstadoVisitante.EN_SALA_PINTURA

        pintura.ingresar(visitante_1)
        with self.assertRaises(ValueError):
            pintura.ingresar(visitante_2)


if __name__ == "__main__":
    unittest.main()
