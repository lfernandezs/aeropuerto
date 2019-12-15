#!/usr/bin/python3

import sys
from grafo import Grafo
from biblioteca import *

COMANDOS = ["listar_operaciones", "camino_mas", "camino_escalas", "nueva_aerolinea",
"centralidad", "centralidad_aprox", "vacaciones", "itinerario", "exportar_kml"]


'''********************************************************
*             FUNCION PRINCIPAL DEL PROGRAMA              *
********************************************************'''

def main(argv):
    dict_aeropuertos = {}
    grafo_vuelos = Grafo(False)
    coordenadas = {}
    ultima_salida = None
    cargar_datos(argv, dict_aeropuertos, grafo_vuelos, coordenadas)
    for line in sys.stdin:
        ultima_salida = validar_entrada(line.rstrip('\n'), dict_aeropuertos, grafo_vuelos, coordenadas, ultima_salida)

def cargar_datos(argv, dict_aeropuertos, grafo_vuelos, coordenadas):
    ''' Carga los destinos en un diccionario con sus aeropuertos
    como valor y los vuelos en un grafo no dirigido.'''
    ruta_aeropuertos = argv[1]
    ruta_vuelos = argv[2]
    with open(ruta_aeropuertos, 'r') as f_aeropuertos:
        for linea in f_aeropuertos:
            ciudad, codigo, lat, lon = linea.split(',')
            grafo_vuelos.agregar_vertice(codigo)
            if ciudad in dict_aeropuertos: dict_aeropuertos[ciudad].append(codigo)
            else: dict_aeropuertos[ciudad] = [codigo]
            coordenadas[codigo] = (lat, lon.rstrip('\n'))
    with open(ruta_vuelos, 'r') as f_vuelos:
        for linea in f_vuelos:
            i, j, tiempo, precio, vuelos = linea.split(',')
            grafo_vuelos.agregar_arista(i, j, (int(tiempo), int(precio), int(vuelos))) # El peso es una tupla

def validar_entrada(entrada, dict_aeropuertos, grafo_vuelos, coordenadas, ultima_salida):
    entrada = entrada.split(' ')
    comando = entrada[0]
    opciones = ' '.join(entrada[1:]).split(',')
    if comando == "listar_operaciones": listar_operaciones()
    elif comando == "camino_mas": return camino_mas(opciones[0], opciones[1], opciones[2], dict_aeropuertos, grafo_vuelos)
    elif comando == "camino_escalas": return camino_escalas(opciones[0], opciones[1], dict_aeropuertos, grafo_vuelos)
    elif comando == "nueva_aerolinea": nueva_aerolinea(opciones[0], grafo_vuelos)
    elif comando == "centralidad": centralidad(int(opciones[0]), grafo_vuelos)
    elif comando == "centralidad_aprox": centralidad_aprox(int(opciones[0]), grafo_vuelos)
    elif comando == "vacaciones": return vacaciones(opciones[0], int(opciones[1]), dict_aeropuertos, grafo_vuelos)
    elif comando == "itinerario": return itinerario(opciones[0], dict_aeropuertos, grafo_vuelos)
    elif comando == "exportar_kml": exportar_kml(opciones[0], ultima_salida, coordenadas)
    else: print_error(f"El comando {comando} no existe.\n")
    return None

    

'''********************************************************
*               IMPLEMENTACIÓN DE COMANDOS                *
********************************************************'''

def listar_operaciones():
    for i in range(len(COMANDOS) - 1): print(COMANDOS[i+1])

def camino_mas(modo, origen, destino, dict_aeropuertos, grafo_vuelos):
    ''' Dijkstra '''
    modos = {'barato':barato, 'rapido':rapido}
    if not modo in modos or not origen in dict_aeropuertos or not destino in dict_aeropuertos: return print_error(f"Error en {COMANDOS[1]}")
    recorrido = obtener_recorrido(origen, destino, dijkstra, modos[modo], dict_aeropuertos, grafo_vuelos)
    return print_recorrido(recorrido, True)

def camino_escalas(origen, destino, dict_aeropuertos, grafo_vuelos):
    ''' BFS '''
    if not origen in dict_aeropuertos or not destino in dict_aeropuertos: return print_error(f"Error en {COMANDOS[2]}")
    recorrido = obtener_recorrido(origen, destino, bfs, None, dict_aeropuertos, grafo_vuelos)
    return print_recorrido(recorrido, True)

def centralidad(n, grafo_vuelos):
    ''' Betweeness Centrality '''
    cent = betweeness_centrality(grafo_vuelos, frecuencia_inv)
    print_centralidad(cent, n)


def centralidad_aprox(n, grafo_vuelos):
    ''' Betweeness Centrality aprox '''
    if n > len(grafo_vuelos): n = len(grafo_vuelos)
    cent = cent_random_walks(grafo_vuelos, 100, 20, frecuencia)
    print_centralidad(cent, n)

def nueva_aerolinea(ruta, grafo_vuelos):
    ''' Árbol de tendido mínimo '''
    with open(ruta, 'w') as f:
        rutas = mst_prim(grafo_vuelos, barato) 
        for v in rutas:
            for w in rutas.adyacentes(v):
                tiempo, precio, vuelos = grafo_vuelos.peso_arista(v, w, peso)
                f.write(f'{v},{w},{tiempo},{precio},{vuelos}\n')
    print('OK')

def vacaciones(origen, n, dict_aeropuertos, grafo_vuelos):
    ''' Backtracking '''
    for aeropuerto in dict_aeropuertos[origen]:
        recorrido = ciclo_largo_n(grafo_vuelos, aeropuerto, n)
        if recorrido: break
    if not recorrido:
        print("No se encontró recorrido.")
        return None
    return print_recorrido(recorrido, False)

def itinerario(ruta, dict_aeropuertos, grafo_vuelos):
    ''' Orden Topológico '''
    with open(ruta, 'r') as f:
        grafo = Grafo()
        ciudades_a_visitar = f.readline().rstrip('\n').split(',')
        for ciudad in ciudades_a_visitar: grafo.agregar_vertice(ciudad)
        for linea in f:
            ciudad_i, ciudad_j = linea.rstrip('\n').split(',')
            grafo.agregar_arista(ciudad_i, ciudad_j, None)
        orden_posible = orden_topologico_bfs(grafo)
        if not orden_posible:
            print_error("No hay orden posible.\n")
            return None
        print(', '.join(orden_posible))
        recorrido = []
        for i in range(len(orden_posible) - 1):
            recorrido.append(camino_escalas(orden_posible[i], orden_posible[i+1], dict_aeropuertos, grafo_vuelos))
    for i in range(len(recorrido)):
        recorrido[i] = recorrido[i][:-7]
    return print(' -> '.join(recorrido))


def exportar_kml(archivo, ultima_salida, coordenadas):
    print(ultima_salida)
    intro = '\
<?xml version="1.0" encoding="UTF-8"?>\n\
<kml xmlns="http://www.opengis.net/kml/2.2">\n\
    <Document>\n\
        <name>KML de ejemplo</name>\n\
        <description>Un ejemplo introductorio para mostrar lasintaxis KML.</description>\n'
    fin = '\
    </Document>\n\
</kml>'
    if not ultima_salida: return print("No se pudo exportar kml", file=sys.stderr)
    aeropuertos = ultima_salida.split(' -> ')
    with open(archivo, 'w') as f:
        f.write(intro)
        for a in aeropuertos:
            f.write(f'\
        <Placemark>\n\
            <name>{a}</name>\n\
            <Point>\n\
                <coordinates>{", ".join(coordenadas[a])}</coordinates>\n\
            </Point>\n\
        </Placemark>\n\n')
        for i in range(len(aeropuertos)-1):
            f.write(f'\
        <Placemark>\n\
            <LineString>\n\
                <coordinates>{", ".join(coordenadas[aeropuertos[i]])} {", ".join(coordenadas[aeropuertos[i+1]])}</coordinates>\n\
            </LineString>\n\
        </Placemark>\n\n')
        f.writelines(fin)
    print("OK")


'''********************************************************
*                 FUNCIONES AUXILIARES                    *
********************************************************'''

def print_error(mensaje): sys.stderr.write(mensaje)

def peso(peso): return peso

def rapido(peso): return peso[0]

def barato(peso): return peso[1]

def frecuencia(peso): return peso[2]

def frecuencia_inv(peso): return (1000 / frecuencia(peso)) # Divido 1000 porque Python divide mal por números chicos

def obtener_recorrido(origen, destino, func, extra, dict_aeropuertos, grafo_vuelos): # func es el algoritmo que se utiliza para obtener el camino.
    aerop_destino = None
    padres = None
    dist = float('inf')
    trayecto = []
    for v in dict_aeropuertos[origen]:
        for w in dict_aeropuertos[destino]:
            if extra: padres_aux, dist_aux = func(grafo_vuelos, v, extra)
            else: padres_aux, dist_aux = func(grafo_vuelos, v)
            if dist_aux[w] < dist:
                aerop_destino = w
                dist = dist_aux[w]
                padres = padres_aux
    while aerop_destino != None:
        trayecto.append(aerop_destino)
        aerop_destino = padres[aerop_destino]
    return trayecto

def print_recorrido(recorrido, reversed):
    if reversed: recorrido = recorrido[::-1]
    resul = ' -> '.join(recorrido)
    print(resul)
    return resul

def print_centralidad(cent, n):
    aux = [(k, v) for k, v in cent.items()]
    aux = sorted(aux, key=lambda x: x[1], reverse=True)
    for i in range(n-1): print(aux[i][0], end=', ')
    print(aux[n-1][0])

main(sys.argv)