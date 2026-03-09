for i in range(0, 10, 2):
    print("numero for: " + str(i))

    encontrado = False
    numerobuscado = 11
    numeros = [1, 3, 5, 7, 9]
    for numero in numeros:
        if numero == numerobuscado :
            encontrado = True
            break
    print("Numero", numerobuscado, "encontrado:", encontrado)

for i in range(1, 4):
    for j in range(1, 4):
        print("i:" + str(i) + " j:" + str(j))