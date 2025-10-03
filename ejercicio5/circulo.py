class Circulo:
    def __init__(self, color: str, diametro: float):
        self.color = color
        self.diametro = diametro

    def __str__(self):
        return f"Círculo de color {self.color} y diámetro {self.diametro}"
