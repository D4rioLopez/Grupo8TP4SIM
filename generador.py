class Generador:
    """Generador congruencial lineal con los parámetros del trabajo práctico."""

    def __init__(self, x0: int = 1234, a: int = 1714, c: int = 1221, m: int = 3922):
        if m <= 0:
            raise ValueError("El módulo m debe ser mayor que cero.")
        if not 0 <= x0 < m:
            raise ValueError("La semilla x0 debe estar entre 0 y m - 1.")

        self._estado = x0
        self.a = a
        self.c = c
        self.m = m

    @property
    def estado(self) -> int:
        """Devuelve el último valor entero generado."""
        return self._estado

    def generar(self) -> float:
        """Avanza el generador y devuelve un número pseudoaleatorio en [0, 1)."""
        self._estado = (self.a * self._estado + self.c) % self.m
        return self._estado / self.m