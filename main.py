from ClasePlanAhorro import PlanAhorro
from Menu import Menu
import csv

if __name__ == '__main__':
    archivo = open("Planes.csv")
    reader = csv.reader(archivo, delimiter=";")
    planes = []
    for fila in reader:
        cod = int(fila[0])
        modelo = str(fila[1])
        version = str(fila[2])
        precio = float(fila[3])
        cantCuotas = int(fila[4])
        cantCuotasLic = int(fila[5])
        planes.append(PlanAhorro(cod, modelo, version, precio, cantCuotas, cantCuotasLic))
    PlanAhorro.ModificarPlan(cantCuotas)
    PlanAhorro.ModicarLic(cantCuotasLic)
    print("1: Actualizar el valor del vehículo de cada plan")
    print("2: Mostrar código del plan, modelo y versión del vehículo")
    print("3: Mostrar el monto que se debe haber pagado para licitar el vehículo")
    print("4: Modificar la cantidad cuotas que debe tener pagas para licitar.")
    op = int(input("Elija una opcion:"))
    menu = Menu(planes, op)
    menu.MenuOp()
