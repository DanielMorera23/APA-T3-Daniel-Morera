"""
Módulo de álgebra de vectores.

Autor: Daniel Morera Torra

Tests unitarios:
    >>> v1 = Vector([1, 2, 3])
    >>> v2 = Vector([4, 5, 6])
    >>> v1 * 2
    Vector([2, 4, 6])
    >>> v1 * v2
    Vector([4, 10, 18])
    >>> v1 @ v2
    32
    >>> v3 = Vector([2, 1, 2])
    >>> v4 = Vector([0.5, 1, 0.5])
    >>> v3 // v4
    Vector([1.0, 2.0, 1.0])
    >>> v3 % v4
    Vector([1.0, -1.0, 1.0])
"""


class Vector:
    """Clase que representa un vector de n dimensiones."""

    def __init__(self, componentes):
        """
        Constructor del vector.

        Args:
            componentes (list): Lista de valores numéricos.
        """
        self.componentes = list(componentes)

    def __repr__(self):
        """Representación del vector."""
        return f"Vector({self.componentes})"

    def __eq__(self, other):
        """Compara dos vectores componente a componente."""
        return all(abs(a - b) < 1e-9 for a, b in zip(self.componentes, other.componentes))

    def __add__(self, other):
        """Suma de dos vectores."""
        return Vector([a + b for a, b in zip(self.componentes, other.componentes)])

    def __mul__(self, other):
        """
        Producto de Hadamard (vector * vector) o multiplicación por escalar (vector * número).

        Args:
            other: Vector o número escalar.

        Returns:
            Vector resultado.
        """
        if isinstance(other, Vector):
            return Vector([a * b for a, b in zip(self.componentes, other.componentes)])
        return Vector([a * other for a in self.componentes])

    def __rmul__(self, other):
        """Permite escalar * vector."""
        return self.__mul__(other)

    def __matmul__(self, other):
        """
        Producto escalar de dos vectores.

        Args:
            other (Vector): Otro vector.

        Returns:
            float: Producto escalar.
        """
        return sum(a * b for a, b in zip(self.componentes, other.componentes))

    def __floordiv__(self, other):
        """
        Componente de self paralela a other.

        Args:
            other (Vector): Vector de referencia.

        Returns:
            Vector: Componente tangencial.
        """
        return ((self @ other) / (other @ other)) * other

    def __mod__(self, other):
        """
        Componente de self perpendicular a other.

        Args:
            other (Vector): Vector de referencia.

        Returns:
            Vector: Componente normal.
        """
        return Vector([a - b for a, b in zip(self.componentes, (self // other).componentes)])


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)