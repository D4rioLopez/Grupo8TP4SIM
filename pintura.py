from visitante import EstadoVisitante, Visitante


class Pintura:
    def __init__(self, capacidad: int = 80) -> None:
        if capacidad <= 0:
            raise ValueError("La capacidad de la sala debe ser mayor que cero.")

        self.capacidad = capacidad
        self._visitantes: dict[int, Visitante] = {}

    @property
    def cantidad_personas(self) -> int:
        return len(self._visitantes)

    @property
    def visitantes(self) -> tuple[Visitante, ...]:
        return tuple(self._visitantes.values())

    def ingresar(self, visitante: Visitante) -> None:
        if visitante.estado is not EstadoVisitante.EN_SALA_PINTURA:
            raise ValueError("El visitante debe salir de fotografía para ingresar a pintura.")
        if visitante.id in self._visitantes:
            raise ValueError("El visitante ya está en la sala de pintura.")
        if self.cantidad_personas >= self.capacidad:
            raise ValueError("La sala de pintura alcanzó su capacidad máxima.")

        self._visitantes[visitante.id] = visitante

    def salir(self, visitante: Visitante) -> None:
        if self._visitantes.get(visitante.id) is not visitante:
            raise ValueError("El visitante no está en la sala de pintura.")

        visitante.retirarse()
        del self._visitantes[visitante.id]