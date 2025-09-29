class Figura:
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return f"{self.__class__.__name__} (Color: {self.color})"


class Elipse(Figura):
    def __init__(self, color, eje_mayor, eje_menor):
        super().__init__(color)
        self.eje_mayor = eje_mayor
        self.eje_menor = eje_menor

    def __str__(self):
        return f"Elipse (Color: {self.color}, Eje Mayor: {self.eje_mayor}, Eje Menor: {self.eje_menor})"


class Cuadrado(Figura):
    def __init__(self, color, longitud):
        super().__init__(color)
        self.longitud = longitud

    def __str__(self):
        return f"Cuadrado (Color: {self.color}, Longitud: {self.longitud})"


class Rectangulo(Figura):
    def __init__(self, color, longitud, anchura):
        super().__init__(color)
        self.longitud = longitud
        self.anchura = anchura

    def __str__(self):
        return f"Rectángulo (Color: {self.color}, Longitud: {self.longitud}, Anchura: {self.anchura})"


class Circulo(Figura):
    def __init__(self, color, diametro):
        super().__init__(color)
        self.diametro = diametro

    def __str__(self):
        return f"Círculo (Color: {self.color}, Diámetro: {self.diametro})"
