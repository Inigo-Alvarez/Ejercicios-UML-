class Cuadrado:
    def __init__(self, longitud: float, color: str):
        self.longitud = longitud
        self.color = color

    def __str__(self):
        return f"Cuadrado {self.color} de lado {self.longitud}"
