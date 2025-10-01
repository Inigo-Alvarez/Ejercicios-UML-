from ejercicio2.persona import Persona

def ejercicio2():
    # Crear personas
    kate = Persona("Kate", "Windsor", "Mujer", apellido_nacimiento="Middleton")
    guillermo = Persona("Guillermo", "Windsor", "Hombre")
    carlos = Persona("Carlos", "Windsor", "Hombre")
    diana = Persona("Diana", "Windsor", "Mujer", apellido_nacimiento="Spencer")

    # Relaciones
    kate.casar_con(guillermo)
    guillermo.agregar_padre(carlos)
    guillermo.agregar_padre(diana)

    # Mostrar resultados
    print(kate)
    print()
    print(guillermo)
    print()
    print(carlos)
    print()
    print(diana)
