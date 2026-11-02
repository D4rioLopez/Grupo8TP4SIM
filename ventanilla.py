from collections import deque

from visitante import Visitante


class Ventanilla:
    def __init__(self, numero: int, habilitada: bool = False) -> None:
        if numero not in {1, 2}:
            raise ValueError("La ventanilla debe ser 1 o 2.")

        self.numero = numero
        self.habilitada = habilitada
        self._cola: deque[Visitante] = deque()

    @property
    def cola(self) -> tuple[Visitante, ...]:
        return tuple(self._cola)

    def habilitar(self) -> None:
        self.habilitada = True

    def deshabilitar(self) -> None:
        self.habilitada = False

    def agregar_visitante(self, visitante: Visitante) -> None:
        if not self.habilitada:
            raise ValueError("No se pueden agregar visitantes a una ventanilla deshabilitada.")
        if any(en_cola.id == visitante.id for en_cola in self._cola):
            raise ValueError("El visitante ya está en la cola de esta ventanilla.")

        visitante.asignar_ventanilla(self.numero)
        self._cola.append(visitante)

    def siguiente_visitante(self) -> Visitante | None:
        if not self.habilitada:
            raise ValueError("No se puede atender en una ventanilla deshabilitada.")
        if not self._cola:
            return None
        return self._cola.popleft()
