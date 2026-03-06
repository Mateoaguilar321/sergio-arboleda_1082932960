numero = int(input("ingrese un numero para mostrar su tabla de multiplicar: "))
for i in range(1, 11):
    resultado = numero * i
    print(str(numero) + " x " + str(i) + " = " + str(resultado))
    
    for i in range(1, 11): #tabla del 1 al 10
        print("Tabla del " , i)
        for j in range(1, 11): # multiplicacion del 1 al 10
            print(i, "x", j, "=", i * j)
            print() # espacio entre tablas