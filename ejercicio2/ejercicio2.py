from ejercicio2.lugar import Lugar
from ejercicio2.cuadro import Cuadro

def ejercicio2():
    # Lugar original
    louvre = Lugar("Museo del Louvre", "París", "Francia")
    # Lugar réplica
    prado = Lugar("Museo del Prado", "Madrid", "España")

    # Cuadro original
    original = Cuadro(
        titulo="La Gioconda",
        cronologia="1503 - 1516",
        tecnica="Óleo",
        subtecnica="Sfumato",
        soporte="Madera de álamo",
        autor="Leonardo da Vinci",
        estado="Regular",
        lugar=louvre
    )

    # Cuadro réplica
    replica = Cuadro(
        titulo="Gioconda de El Prado",
        cronologia="1503 - 1516",
        tecnica="Óleo",
        subtecnica="Pincelada simple",
        soporte="Madera de nogal",
        autor="Anónimo",
        estado="Bueno",
        lugar=prado,
        replica_de=original
    )

    print(original)
    print(replica)
