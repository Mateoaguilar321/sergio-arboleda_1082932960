import math

def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_hipotenusa(cateto1, cateto2):
    return math.sqrt(cateto1 ** 2 + cateto2 ** 2)

def calcular_potencia(base, exponente):
    return math.pow(base, exponente)

def main():
    while True:
        print("\nMenú")
        print("1. Calcular área de círculo")
        print("2. Calcular hipotenusa")
        print("3. Calcular potencia")
        print("4. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            radio = float(input("Ingresa el radio: "))
            area = calcular_area_circulo(radio)
            print(f"El área del círculo es {round(area,2)}")

        elif opcion == "2":
            a = float(input("Ingresa el cateto 1: "))
            b = float(input("Ingresa el cateto 2: "))
            h = calcular_hipotenusa(a, b)
            print(f"La hipotenusa es {round(h,2)}")

        elif opcion == "3":
            base = float(input("Ingresa la base: "))
            exponente = float(input("Ingresa el exponente: "))
            resultado = calcular_potencia(base, exponente)
            print(f"El resultado es {round(resultado,2)}")

        elif opcion == "4":
            print("Programa finalizado.")
            break

        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()