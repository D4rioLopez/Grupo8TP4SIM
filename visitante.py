from dataclasses import dataclass
from enum import Enum


class EstadoVisitante(Enum):
    ARRIBANDO = "Arribando"
    ESPERANDO_VENTANILLA = "Esperando en ventanilla"
    SIENDO_ATENDIDO = "Siendo atendido"
    EN_SALA_FOTOGRAFIA = "En sala de fotografía"
    EN_SALA_PINTURA = "En sala de pintura"
    RETIRADO = "Retirado"


@dataclass
class Visitante:
    id: int
    puerta_ingreso: str
    hora_ingreso: float
    ventanilla_asignada: int | None = None
    estado: EstadoVisitante = EstadoVisitante.ARRIBANDO

    def __post_init__(self) -> None:
        if self.id <= 0:
            raise ValueError("El ID del visitante debe ser mayor que cero.")
        if self.puerta_ingreso not in {"A", "B", "C"}:
            raise ValueError("La puerta de ingreso debe ser A, B o C.")
        if self.hora_ingreso < 0:
            raise ValueError("La hora de ingreso no puede ser negativa.")

    def asignar_ventanilla(self, numero: int) -> None:
        if self.estado is not EstadoVisitante.ARRIBANDO:
            raise ValueError("Solo se puede asignar una ventanilla a un visitante que está arribando.")
        if numero not in {1, 2}:
            raise ValueError("La ventanilla debe ser 1 o 2.")

        self.ventanilla_asignada = numero
        self.estado = EstadoVisitante.ESPERANDO_VENTANILLA

    def iniciar_atencion(self) -> None:
        if self.estado is not EstadoVisitante.ESPERANDO_VENTANILLA:
            raise ValueError("El visitante no está esperando en una ventanilla.")
        self.estado = EstadoVisitante.SIENDO_ATENDIDO

    def finalizar_atencion(self) -> None:
        if self.estado is not EstadoVisitante.SIENDO_ATENDIDO:
            raise ValueError("El visitante no está siendo atendido.")
        self.estado = EstadoVisitante.EN_SALA_FOTOGRAFIA

    def salir_de_fotografia(self, ir_a_pintura: bool) -> None:
        if self.estado is not EstadoVisitante.EN_SALA_FOTOGRAFIA:
            raise ValueError("El visitante no está en la sala de fotografía.")
        self.estado = (
            EstadoVisitante.EN_SALA_PINTURA
            if ir_a_pintura
            else EstadoVisitante.RETIRADO
        )

    def retirarse(self) -> None:
        if self.estado is not EstadoVisitante.EN_SALA_PINTURA:
            raise ValueError("El visitante no está en la sala de pintura.")
        self.estado = EstadoVisitante.RETIRADO
