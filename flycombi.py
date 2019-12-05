import sys
from grafo import Grafo
from biblioteca import *

COMANDOS = ("listar_operaciones", "camino_mas", "salir")

dict_aeropuertos = {}
grafo_vuelos = Grafo(True)

def main(argv, dict_aeropuertos, grafo_vuelos):
    # Cargar datos
    if not cargar_datos(argv, dict_aeropuertos, grafo_vuelos): return
    # Valido la entrada
    print('3')
    entrada = ""
    while entrada != "salir":
        entrada = input("Ingrese un comando: ")
        validar_entrada(entrada.split(' '))

def cargar_datos(argv, dict_aeropuertos, grafo_vuelos):
    if len(argv) != 3: return False # Mensaje?
    ruta_aeropuertos = argv[1]
    ruta_vuelos = argv[2]
    with open(ruta_aeropuertos, 'r') as f_aeropuertos: # Checkear que exista
        for linea in f_aeropuertos:
            ciudad, codigo, lat, lon = linea.split(',') # Lat y lon?
            grafo_vuelos.agregar_vertice(codigo)
            if ciudad in dict_aeropuertos: dict_aeropuertos[ciudad].append(codigo)
            else: dict_aeropuertos[ciudad] = [codigo]
    with open(ruta_vuelos, 'r') as f_vuelos:
        for linea in f_vuelos:
            i, j, tiempo, precio, vuelos = linea.split(',')
            grafo_vuelos.agregar_arista(i, j, (precio, tiempo, vuelos)) # El peso es una tupla
    return True

def validar_entrada(entrada):
    if not entrada[0] in COMANDOS:
        print("El comando", entrada[0], "no existe.")
        return
    if entrada[0] == COMANDOS[0]: listar_operaciones()
    elif entrada[0] == COMANDOS[1]:
        if len(entrada) != 4: return print_error(entrada[0])
        modo, origen, destino = entrada[1].split(',')
        camino_mas(modo, origen, destino)
    elif entrada[0] == COMANDOS[1]: return



def listar_operaciones():
    for comando in COMANDOS: print(comando)

def camino_mas(modo, origen, destino):
    modos = {'barato':barato, 'rapido':rapido}
    if not modo in modos or not origen in dict_aeropuertos or not destino in dict_aeropuertos: return print_error(COMANDOS[1])
    aerop_destino = None
    padres = None
    dist = float('inf')
    trayecto = []
    for v in dict_aeropuertos[origen]:
        for w in dict_aeropuertos[destino]:
            padres_aux, dist_aux = dijkstra(grafo_vuelos, v, modos[modo])
            if dist_aux[w] < dist:
                aerop_destino = w
                dist = dist_aux
                padres = padres_aux
    if dist == float('inf'): print("No hay forma de llegar.")
    while padres[aerop_destino] != None:
        trayecto.append(aerop_destino)
        aerop_destino = padres[aerop_destino]
    for v in trayecto[-1]: print(v, end='->')
    print(aerop_destino)  


def barato(peso): return peso[0]

def rapido(peso): return peso[1]

def print_error(comando): print(f"Error en comando {comando}")

    

main(sys.argv, dict_aeropuertos, grafo_vuelos)