class Persona:
    def __init__(self, nombre, apellido, sexo, apellido_nacimiento=None):
        self.nombre = nombre
        self.apellido = apellido
        self.apellido_nacimiento = apellido_nacimiento
        self.sexo = sexo
        self.conyuge = None
        self.padres = []

    def casar_con(self, otra_persona):
        self.conyuge = otra_persona
        otra_persona.conyuge = self

    def agregar_padre(self, padre):
        self.padres.append(padre)

    def __str__(self):
        info = f"{self.nombre} {self.apellido} ({self.sexo})"
        if self.apellido_nacimiento:
            info += f", nacida {self.apellido_nacimiento}"
        if self.conyuge:
            info += f"\n  Casado con: {self.conyuge.nombre} {self.conyuge.apellido}"
        if self.padres:
            padres_str = ", ".join([f"{p.nombre} {p.apellido}" for p in self.padres])
            info += f"\n  Hijo de: {padres_str}"
        return info
