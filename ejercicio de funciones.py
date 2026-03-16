def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return round(imc, 2)

def clasificar_imc(imc):
    if imc < 18.5:
        return "Bajo peso"
    elif 18.5 <= imc < 25:
        return "Peso normal"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidad"

def main():
    peso = float(input("Ingresa tu peso en kg: "))
    altura = float(input("Ingresa tu altura en metros: "))

    imc = calcular_imc(peso, altura)
    clasificacion = clasificar_imc(imc)

    print(f"Tu IMC es {imc} y tu clasificación es: {clasificacion}")

if __name__ == "__main__":
    main()