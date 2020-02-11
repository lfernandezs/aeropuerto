import sys
from grafo import Grafo
from biblioteca import *

def main(argv):
    dict_aeropuertos = {}
    pais_de_aerop = {}
    grafo_vuelos = Grafo(False)
    cargar_datos(argv, dict_aeropuertos, grafo_vuelos, pais_de_aerop)
    print(recorrer_mundo(grafo_vuelos, "Gotica", pais_de_aerop, dict_aeropuertos))

def cargar_datos(argv, dict_aeropuertos, grafo_vuelos, pais_de_aerop):
    ''' Carga los destinos en un diccionario con sus aeropuertos
    como valor y los vuelos en un grafo no dirigido.'''
    ruta_aeropuertos = argv[1]
    ruta_vuelos = argv[2]
    with open(ruta_aeropuertos, 'r') as f_aeropuertos:
        for linea in f_aeropuertos:
            ciudad, codigo, lat, lon = linea.split(',')
            grafo_vuelos.agregar_vertice(codigo)
            pais_de_aerop[codigo] = ciudad
            if ciudad in dict_aeropuertos: dict_aeropuertos[ciudad].append(codigo)
            else: dict_aeropuertos[ciudad] = [codigo]
    with open(ruta_vuelos, 'r') as f_vuelos:
        for linea in f_vuelos:
            i, j, tiempo, precio, vuelos = linea.split(',')
            grafo_vuelos.agregar_arista(i, j, (int(tiempo), int(precio), int(vuelos))) # El peso es una tupla

def recorrer_mundo(grafo, origen, pais_de_aerop, dict_aeropuertos):
    origen = dict_aeropuertos[origen][0]
    visitados = set()
    visitados.add(origen)
    mejor_camino, mejor_costo = _recorrer_mundo(grafo, origen, visitados, [origen], pais_de_aerop, 0)
    print(mejor_camino, mejor_costo)
    visitados = set()
    print(recorrer_mundo_optimo(grafo, origen, visitados, mejor_camino, mejor_costo, [origen], 0, pais_de_aerop))

def _recorrer_mundo(grafo, v, visitados, camino_actual, pais_de_aerop, costo):
    aux = False
    if pais_de_aerop[v] not in visitados:
        aux = True
        visitados.add(pais_de_aerop[v])
    if len(visitados) == 10:
        return camino_actual, costo
    for w in grafo.adyacentes(v):
        if w in camino_actual: continue
        costo += grafo.peso_arista(v, w, rapido)
        solucion, costo = _recorrer_mundo(grafo, w, visitados, camino_actual + [w], pais_de_aerop, costo)
        if solucion is not None: return solucion, costo
        costo -= grafo.peso_arista(v, w, rapido)
    if aux == True: visitados.remove(pais_de_aerop[v])
    return None, None

def recorrer_mundo_optimo(grafo, v, visitados, mejor_camino, mejor_costo, camino_actual, costo_actual, pais_de_aerop):
    if costo_actual > mejor_costo: return mejor_camino, mejor_costo
    if len(visitados) == 10:
        if costo_actual < mejor_costo: return camino_actual, costo_actual
        else: return mejor_camino, mejor_costo
    for w in grafo.adyacentes(v):
        aux = False
        if pais_de_aerop[w] not in visitados:
            aux = True
            visitados.add(pais_de_aerop[w])
        costo_actual += grafo.peso_arista(v, w, rapido)
        mejor_camino, mejor_costo = recorrer_mundo_optimo(grafo, w, visitados, mejor_camino, mejor_costo, camino_actual + [w], costo_actual, pais_de_aerop)
        costo_actual -= grafo.peso_arista(v, w, rapido)
        if aux == True: visitados.remove(pais_de_aerop[w])
    return mejor_camino, mejor_costo
    

def rapido(peso): return peso[0]

main(sys.argv)

