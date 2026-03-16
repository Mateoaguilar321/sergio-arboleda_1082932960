import re

# 1. Función para validar cédula
def validar_cedula(cedula):
    return cedula.isdigit() and 8 <= len(cedula) <= 10

# 2. Función para validar el email
def validar_email(email):
    patron = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(patron, email))

# 3. Función para validar las calificaciones
def validar_calificaciones(calificaciones):
    return all(0 <= calificacion <= 5 for calificacion in calificaciones)

# 4. Función para crear estudiante
def crear_estudiante(cedula, nombre, email, calificaciones):
    if not validar_cedula(cedula):
        return None
    if not validar_email(email):
        return None
    if not validar_calificaciones(calificaciones):
        return None
    promedio = calcular_promedio(calificaciones)
    return {"cedula": cedula, "nombre": nombre, "email": email, "promedio": promedio}

# 5. Función para calcular el promedio
def calcular_promedio(calificaciones):
    return round(sum(calificaciones) / len(calificaciones), 2)

# 6. Función para clasificar el desempeño según el promedio
def clasificar_desempeño(promedio):
    if promedio >= 4.5:
        return "Excelente"
    elif promedio >= 4.0:
        return "Muy bueno"
    elif promedio >= 3.5:
        return "Bueno"
    elif promedio >= 3.0:
        return "Satisfactorio"
    else:
        return "Necesita mejorar"

# 7. Función para listar los estudiantes
def listar_estudiantes(lista_estudiantes):
    print("Cédula    | Nombre        | Promedio | Desempeño")
    print("----------------------------------------------")
    for estudiante in lista_estudiantes:
        desempeño = clasificar_desempeño(estudiante["promedio"])
        print(f"{estudiante['cedula']} | {estudiante['nombre']} | {estudiante['promedio']} | {desempeño}")

# 8. Función principal con menú
def main():
    lista_estudiantes = []
    while True:
        print("\nMenú:")
        print("1. Agregar estudiante")
        print("2. Ver lista de estudiantes")
        print("3. Buscar estudiante por cédula")
        print("4. Salir")
        
        opcion = input("Seleccione una opción (1-4): ")

        if opcion == '1':
            cedula = input("Cédula: ")
            nombre = input("Nombre: ")
            email = input("Email: ")
            calificaciones = list(map(float, input("Calificaciones (separadas por coma): ").split(',')))

            estudiante = crear_estudiante(cedula, nombre, email, calificaciones)
            if estudiante:
                lista_estudiantes.append(estudiante)
                desempeño = clasificar_desempeño(estudiante["promedio"])
                print(f"Estudiante agregado exitosamente. Promedio: {estudiante['promedio']} | Desempeño: {desempeño}")
            else:
                print("Datos inválidos. El estudiante no fue agregado.")

        elif opcion == '2':
            listar_estudiantes(lista_estudiantes)

        elif opcion == '3':
            cedula_buscada = input("Cédula a buscar: ")
            estudiante_encontrado = next((estudiante for estudiante in lista_estudiantes if estudiante["cedula"] == cedula_buscada), None)
            if estudiante_encontrado:
                desempeño = clasificar_desempeño(estudiante_encontrado["promedio"])
                print(f"{estudiante_encontrado['nombre']} | Promedio: {estudiante_encontrado['promedio']} | Desempeño: {desempeño}")
            else:
                print("Estudiante no encontrado.")

        elif opcion == '4':
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()