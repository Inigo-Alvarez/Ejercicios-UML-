from ejercicio3.lugar import Lugar
from ejercicio3.edificio import Edificio

def ejercicio3():
    # Lugar
    santiago = Lugar("Santiago de Compostela", "Galicia", "España")

    # Edificio
    catedral = Edificio(
        nombre="Catedral de Santiago de Compostela",
        culto="Católico",
        material="Granito",
        estilos=["Románico", "Gótico", "Barroco", "Plateresco", "Neoclásico"],
        fecha_inicio=1075,
        fecha_fin=1122,
        fecha_consagracion1=1128,
        fecha_consagracion2="3 de abril de 1211",
        fecha_bic=1896,
        lugar=santiago
    )

    print(catedral)
