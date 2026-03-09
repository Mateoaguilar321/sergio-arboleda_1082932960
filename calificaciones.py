# Sistema de registro de estudiantes

# Lista para almacenar los estudiantes
estudiantes = []

# Acumulador para la suma de calificaciones
suma_calificaciones = 0

# Variables para el estudiante con mayor y menor calificación
mejor_estudiante = None
peor_estudiante = None
max_calificacion = float('-inf')
min_calificacion = float('inf')

# Bucle para 5 estudiantes
for i in range(1, 6):
    print(f"\nEstudiante {i}:")

    # Pedir nombre
    nombre = input("Nombre: ").strip()
    while not nombre:
        print("El nombre no puede estar vacío.")
        nombre = input("Nombre: ").strip()

    # Pedir edad con validación
    while True:
        try:
            edad = int(input("Edad: "))
            if 5 <= edad <= 100:
                break
            else:
                print("La edad debe estar entre 5 y 100.")
        except ValueError:
            print("Por favor, ingresa un número entero para la edad.")

    # Pedir calificación con validación
    while True:
        try:
            calificacion = float(input("Calificación (0-5): "))
            if 0 <= calificacion <= 5:
                break
            else:
                print("La calificación debe estar entre 0 y 5.")
        except ValueError:
            print("Por favor, ingresa un número decimal para la calificación.")

    # Agregar a la lista
    estudiante = {
        'nombre': nombre,
        'edad': edad,
        'calificacion': calificacion
    }
    estudiantes.append(estudiante)

    # Actualizar acumulador
    suma_calificaciones += calificacion

    # Actualizar mejor y peor estudiante
    if calificacion > max_calificacion:
        max_calificacion = calificacion
        mejor_estudiante = estudiante
    if calificacion < min_calificacion:
        min_calificacion = calificacion
        peor_estudiante = estudiante

# Calcular promedio
promedio = suma_calificaciones / 5

# Mostrar resultados
print("\n--- Resultados ---")
print(f"Estudiante con la calificación más alta: {mejor_estudiante['nombre']} ({mejor_estudiante['calificacion']})")
print(f"Estudiante con la calificación más baja: {peor_estudiante['nombre']} ({peor_estudiante['calificacion']})")
print(f"Calificación promedio: {promedio:.2f}")
