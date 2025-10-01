from ejercicio2.lugar import Lugar

class Cuadro:
    def __init__(self, titulo, cronologia, tecnica, subtecnica, soporte, autor, estado, lugar=None, replica_de=None):
        self.titulo = titulo
        self.cronologia = cronologia
        self.tecnica = tecnica
        self.subtecnica = subtecnica
        self.soporte = soporte
        self.autor = autor
        self.estado = estado
        self.lugar = lugar
        self.replica_de = replica_de

    def __str__(self):
        info = f"'{self.titulo}' ({self.cronologia}), {self.tecnica}, {self.subtecnica}, soporte: {self.soporte}\n"
        info += f"Autor: {self.autor}, Estado: {self.estado}\n"
        if self.lugar:
            info += f"Ubicación: {self.lugar}\n"
        if self.replica_de:
            info += f"Es réplica de: {self.replica_de.titulo}\n"
        return info
