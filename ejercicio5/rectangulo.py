class Rectangulo:
    def __init__(self, longitud: float, anchura: float, color: str):
        self.longitud = longitud
        self.anchura = anchura
        self.color = color

    def __str__(self):
        return f"Rectángulo {self.color}, {self.longitud}x{self.anchura}"
