#Punto 2

def cargar_empleados():
    empleados = []
    for i in range(5):
        nombre = input(f"Ingrese el nombre del empleado {i+1}: ")
        sueldos = []
        for j in range(3):
            sueldo = float(input(f"Ingrese el sueldo {j+1} de {nombre}: "))
            sueldos.append(sueldo)
        empleados.append([nombre] + sueldos)
    return empleados

# Función imprimir monto total cobrado por cada empleado
def imprimir_totales(empleados):
    for empleado in empleados:
        total_cobrado = sum(empleado[1:])
        print(f"{empleado[0]} cobró un total de ${total_cobrado}")

# Cargar los empleados
empleados = cargar_empleados()

# Imprimir el monto total cobrado por cada empleado
imprimir_totales(empleados)