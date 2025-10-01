from ejercicio3.lugar import Lugar

class Edificio:
    def __init__(self, nombre, culto, material, estilos, 
                 fecha_inicio, fecha_fin, fecha_consagracion1, 
                 fecha_consagracion2, fecha_bic, lugar=None):
        self.nombre = nombre
        self.culto = culto
        self.material = material
        self.estilos = estilos  # lista de estilos arquitectónicos
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.fecha_consagracion1 = fecha_consagracion1
        self.fecha_consagracion2 = fecha_consagracion2
        self.fecha_bic = fecha_bic
        self.lugar = lugar

    def __str__(self):
        info = f"{self.nombre} ({self.culto})\n"
        info += f"Material: {self.material}\n"
        info += f"Estilos: {', '.join(self.estilos)}\n"
        info += f"Construcción: {self.fecha_inicio} - {self.fecha_fin}\n"
        info += f"Primera consagración: {self.fecha_consagracion1}\n"
        info += f"Segunda consagración: {self.fecha_consagracion2}\n"
        info += f"Declaración BIC: {self.fecha_bic}\n"
        if self.lugar:
            info += f"Ubicación: {self.lugar}\n"
        return info
