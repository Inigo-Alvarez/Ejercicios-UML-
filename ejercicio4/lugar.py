class Lugar:
    def __init__(self, ciudad: str, comunidad: str, pais: str):
        self.ciudad = ciudad
        self.comunidad = comunidad
        self.pais = pais

    def __str__(self) -> str:
        return f"{self.ciudad}, {self.comunidad} ({self.pais})"
