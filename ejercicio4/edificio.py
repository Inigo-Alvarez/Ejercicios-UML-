from typing import List, Optional
from ejercicio4.lugar import Lugar

class Edificio:
    def __init__(
        self,
        nombre: str,
        culto: str,
        material: str,
        estilos: List[str],
        fecha_inicio: Optional[int],
        fecha_fin: Optional[int],
        fecha_consagracion1: Optional[str],
        fecha_consagracion2: Optional[str],
        fecha_bic: Optional[int],
        lugar: Optional[Lugar] = None,
    ):
        self.nombre = nombre
        self.culto = culto
        self.material = material
        self.estilos = estilos
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.fecha_consagracion1 = fecha_consagracion1
        self.fecha_consagracion2 = fecha_consagracion2
        self.fecha_bic = fecha_bic
        self.lugar = lugar

    def __str__(self) -> str:
        estilos = ", ".join(self.estilos) if self.estilos else "—"
        info = (
            f"{self.nombre} ({self.culto})\n"
            f"Material: {self.material}\n"
            f"Estilos: {estilos}\n"
            f"Construcción: {self.fecha_inicio} - {self.fecha_fin}\n"
            f"Primera consagración: {self.fecha_consagracion1}\n"
            f"Segunda consagración: {self.fecha_consagracion2}\n"
            f"Declaración BIC: {self.fecha_bic}\n"
        )
        if self.lugar:
            info += f"Ubicación: {self.lugar}\n"
        return info

