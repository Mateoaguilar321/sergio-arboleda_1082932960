import datetime

def crear_evento(nombre, dia, mes, año):
    fecha = datetime.date(año, mes, dia)
    return {"nombre": nombre, "fecha": fecha}

def dias_hasta_evento(fecha_evento):
    hoy = datetime.date.today()
    diferencia = fecha_evento - hoy
    return diferencia.days

def evento_pasado(fecha_evento):
    hoy = datetime.date.today()
    return fecha_evento < hoy

def main():
    nombre = input("Nombre del evento: ")
    dia = int(input("Día: "))
    mes = int(input("Mes: "))
    año = int(input("Año: "))

    evento = crear_evento(nombre, dia, mes, año)
    dias = dias_hasta_evento(evento["fecha"])

    if evento_pasado(evento["fecha"]):
        print(f"El evento ya pasó. Fue hace {abs(dias)} días.")
    elif dias == 0:
        print("El evento es hoy.")
    else:
        print(f"Faltan {dias} días para tu evento.")

if __name__ == "__main__":
    main()