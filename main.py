from ejercicio1.figuras import Elipse, Cuadrado, Rectangulo, Circulo

def main():
    # Instancias según el enunciado del Ejercicio 1
    e1 = Elipse("Amarillo", eje_mayor=3, eje_menor=1)
    c2 = Cuadrado("Azul", longitud=1.5)
    r1 = Rectangulo("Naranja", longitud=3, anchura=1)
    c1 = Circulo("Negro", diametro=1)

    print("=== Objetos geométricos del Ejercicio 1 ===")
    for figura in [e1, c2, r1, c1]:
        print(figura)

if __name__ == "__main__":
    main()
