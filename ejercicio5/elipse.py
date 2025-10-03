class Elipse:
    def __init__(self, eje_mayor: float, eje_menor: float, color: str):
        self.eje_mayor = eje_mayor
        self.eje_menor = eje_menor
        self.color = color

    def __str__(self):
        return f"Elipse {self.color}, eje mayor {self.eje_mayor}, eje menor {self.eje_menor}"
