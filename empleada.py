from visitante import Visitante
from ventanilla import Ventanilla


class Empleada:
    def __init__(self, id: int, ventanilla: Ventanilla) -> None:
        if id <= 0:
            raise ValueError("El ID de la empleada debe ser mayor que cero.")

        self.id = id
        self.ventanilla = ventanilla
        self.visitante_actual: Visitante | None = None

    @property
    def ocupada(self) -> bool:
        return self.visitante_actual is not None

    def atender_siguiente(self) -> Visitante | None:
        if self.ocupada:
            raise ValueError("La empleada ya está atendiendo a un visitante.")

        visitante = self.ventanilla.siguiente_visitante()
        if visitante is not None:
            visitante.iniciar_atencion()
            self.visitante_actual = visitante
        return visitante

    def finalizar_atencion(self) -> Visitante:
        if self.visitante_actual is None:
            raise ValueError("La empleada no tiene un visitante para atender.")

        visitante = self.visitante_actual
        visitante.finalizar_atencion()
        self.visitante_actual = None
        return visitante