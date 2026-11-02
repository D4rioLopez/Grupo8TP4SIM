from visitante import EstadoVisitante, Visitante


class Fotografia:
    def __init__(self) -> None:
        self._visitantes: dict[int, Visitante] = {}

    @property
    def cantidad_personas(self) -> int:
        return len(self._visitantes)

    @property
    def visitantes(self) -> tuple[Visitante, ...]:
        return tuple(self._visitantes.values())

    def ingresar(self, visitante: Visitante) -> None:
        if visitante.estado is not EstadoVisitante.EN_SALA_FOTOGRAFIA:
            raise ValueError("El visitante debe finalizar la atención antes de ingresar.")
        if visitante.id in self._visitantes:
            raise ValueError("El visitante ya está en la sala de fotografía.")

        self._visitantes[visitante.id] = visitante

    def salir(self, visitante: Visitante, ir_a_pintura: bool) -> None:
        if self._visitantes.get(visitante.id) is not visitante:
            raise ValueError("El visitante no está en la sala de fotografía.")

        visitante.salir_de_fotografia(ir_a_pintura)
        del self._visitantes[visitante.id]