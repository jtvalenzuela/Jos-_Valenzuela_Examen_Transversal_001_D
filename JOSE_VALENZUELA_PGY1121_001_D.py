import numpy as np
from os import system
system("cls")
escenario = np.arange(1, 101).reshape(10, 10)

precios = {
    'platinum': 120000,
    'gold': 80000,
    'silver': 50000   
}

registro = {}

def comprar_asiento():
    print("----- Compra de asientos -----")
    fila = int(input("Ingrese la fila del asiento (1-10) "))
    columna = int(input("Ingrese el numero de fila en la cual desea comprar (1-10) "))
    asiento = escenario[fila - 1] [columna - 1]
    
    if asiento in registro:
        print("El asiento ya esta ocupado")
    else:
        run = input("Ingrese el run del asistente: ")
        registro[asiento] = run
        print("El asiento se ha comprado correctamente!\n ")

def mostrar_asientos_disponibles():
    print("----- Asientos Disponibles -----")
    for i in range(10):
        for j in range(10):
            asiento = escenario[i][j]
            if asiento in registro:
                print("X", end="\t")
            else:
                print(asiento, end="\t")
        print()

def mostrar_listado_asistentes():
    print("----- Listado Asistentes -----")
    asistentes_ordenados = sorted(registro.items(), key=lambda x: x[1])
    for asiento, run in asistentes_ordenados:
        print(f"Asiento: {asiento}\t RUN: {run}") 
        
def calcular_ganancias_totales():
    print("----- Ganancias Totales -----")
    ganancias = sum(precios[get_tarifa(asiento)] for asiento in registro)
    print(f"Tipo de entrada Platinum $120000\n Tipo de entrada Gold $80000\n Tipo de entrada Silver $50000\n Total ganado por concepto de asientos: ${ganancias}\n")
    
def get_tarifa(asiento):
    if asiento <= 20:
        return 'platinum'
    elif asiento <= 51:
        return 'gold'
    else:
        return 'silver'

def main():
    while True:
        print("--- Entradas Para el Concierto de Michael Jam ---")
        print("1.- Mostrar asientos disponibles.")
        print("2.- Compra de asientos")
        print("3.- Ver listado de asistentes")
        print("4.- Ganancias Totales")
        print("5.- Salir")
        opc = input("Seleccione una opción: ")
        if opc== "1":
            mostrar_asientos_disponibles()
        elif opc== "2":
            comprar_asiento()
        elif opc== "3":
            mostrar_listado_asistentes()
        elif opc== "4":
            calcular_ganancias_totales()
        elif opc=="5":
            print("José Valenzuela 10/07/2023")
            break
        else:
            print("Opcion invalida. seleccione una opcion valida")
            
main()