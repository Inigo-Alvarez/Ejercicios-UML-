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

from ejercicio2.ejercicio2 import ejercicio2

if __name__ == "__main__":
    ejercicio2()

from ejercicio3.ejercicio3 import ejercicio3

if __name__ == "__main__":
    ejercicio3()

from ejercicio4.ejercicio4 import ejercicio4

if __name__ == "__main__":
    ejercicio4()


from ejercicio5.circulo import Circulo
from ejercicio5.rectangulo import Rectangulo
from ejercicio5.cuadrado import Cuadrado
from ejercicio5.elipse import Elipse

def main():
    # Crear objetos
    c = Circulo("gris", 10)
    r = Rectangulo(12, 6, "naranja")
    q = Cuadrado(8, "azul")
    e = Elipse(14, 7, "amarillo")

    # Mostrar información
    print(c)
    print(r)
    print(q)
    print(e)

if __name__ == "__main__":
    main()
