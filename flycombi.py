import sys
from grafo import Grafo
from biblioteca import *

COMANDOS = ["listar_operaciones", "camino_mas", "camino_escalas", "nueva_aerolinea",
"centralidad", "centralidad_aprox", "vacaciones", "itinerario", "exportar_kml", "salir"]

''' Variables Globales '''
dict_aeropuertos = {}
grafo_vuelos = Grafo(False)
coordenadas = {}
ultima_salida = "" # Ir actualizando esto

'''********************************************************
*             FUNCION PRINCIPAL DEL PROGRAMA              *
********************************************************'''

def main(argv, dict_aeropuertos, grafo_vuelos):
    global ultima_salida
    cargar_datos(argv, dict_aeropuertos, grafo_vuelos)
    while ultima_salida != "salir":
        entrada = input("Ingrese un comando: ")
        ultima_salida = validar_entrada(entrada)

def cargar_datos(argv, dict_aeropuertos, grafo_vuelos):
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

def validar_entrada(entrada):
    entrada = entrada.split(' ')
    comando = entrada[0]
    opciones = ' '.join(entrada[1:]).split(',')
    print(opciones)
    if comando == "listar_operaciones": listar_operaciones()
    elif comando == "camino_mas": return camino_mas(opciones[0], opciones[1], opciones[2])
    elif comando == "camino_escalas": return camino_escalas(opciones[0], opciones[1])
    elif comando == "nueva_aerolinea": nueva_aerolinea(opciones[0])
    elif comando == "centralidad": centralidad(int(opciones[0]))
    elif comando == "centralidad_aprox": centralidad_aprox(int(opciones[0]))
    elif comando == "vacaciones": return vacaciones(opciones[0], int(opciones[1]))
    elif comando == "itinerario": return itinerario(opciones[0])
    elif comando == "exportar_kml": exportar_kml(opciones[0])
    elif comando == "salir": return "salir"
    else: print_error(f"El comando {comando} no existe.\n")
    return None

    

'''********************************************************
*               IMPLEMENTACIÓN DE COMANDOS                *
********************************************************'''

def listar_operaciones():
    for comando in COMANDOS: print(comando)

def camino_mas(modo, origen, destino):
    ''' Dijkstra '''
    modos = {'barato':barato, 'rapido':rapido}
    if not modo in modos or not origen in dict_aeropuertos or not destino in dict_aeropuertos: return print_error(f"Error en {COMANDOS[1]}")
    recorrido = obtener_recorrido(origen, destino, dijkstra, modos[modo])
    return print_recorrido(recorrido, True)

def camino_escalas(origen, destino):
    ''' BFS '''
    if not origen in dict_aeropuertos or not destino in dict_aeropuertos: return print_error(COMANDOS[2])
    recorrido = obtener_recorrido(origen, destino, bfs, None)
    return print_recorrido(recorrido, True)

def centralidad(n):
    ''' Betweeness Centrality '''
    cent = betweeness_centrality(grafo_vuelos, frecuencia_inv)
    print_centralidad(cent, n)


def centralidad_aprox(n): # Checkear si cent_random_walks está bien implementado
    ''' Betweeness Centrality aprox '''
    if n > len(grafo_vuelos): n = len(grafo_vuelos)
    cent = cent_random_walks(grafo_vuelos, 50, 10, frecuencia)
    print_centralidad(cent, n)

#def pagerank(n)
    ''' Pagerank '''

def nueva_aerolinea(ruta):
    ''' Árbol de tendido mínimo '''
    with open(ruta, 'w') as f:
        rutas = mst_prim(grafo_vuelos, barato) 
        for v in rutas:
            for w in rutas.adyacentes(v):
                f.write(f'{v}, {w}\n')
    print('OK')

#def recorrer_mundo(origen)
    '''BackTracking?'''

#def recorrer_mundo_aprox(origen)
    '''Greedy?'''

def vacaciones(origen, n):
    ''' Backtracking '''
    for aeropuerto in dict_aeropuertos[origen]:
        recorrido = ciclo_largo_n(grafo_vuelos, aeropuerto, n)
        if recorrido: break
    if not recorrido:
        print("No se encontró recorrido.")
        return None
    return print_recorrido(recorrido, False)

def itinerario(ruta):
    ''' Orden Topológico '''
    with open(ruta, 'r') as f:
        grafo = Grafo()
        ciudades_a_visitar = f.readline().rstrip('\n').split(',')
        for ciudad in ciudades_a_visitar: grafo.agregar_vertice(ciudad)
        for linea in f:
            ciudad_i, ciudad_j = linea.rstrip('\n').split(',')
            grafo.agregar_arista(ciudad_i, ciudad_j, None)
        orden_posible = orden_topologico_bfs(grafo) # Preguntar como hago para ver si hay ciclo con O.T dfs
        if not orden_posible:
            print_error("No hay orden posible.\n")
            return None
        print(', '.join(orden_posible))
        recorrido = []
        for i in range(len(orden_posible) - 1):
            recorrido.append(camino_escalas(orden_posible[i], orden_posible[i+1]))
    return ' -> '.join(recorrido) # Ver como exportar kml.


def exportar_kml(archivo):
    print(ultima_salida)
    intro = ['<?xml version="1.0" encoding="UTF-8"?>\n', '<kml xmlns="http://www.opengis.net/kml/2.2">\n',\
'\t<Document>\n', '\t\t<name>KML de ejemplo</name>\n', '\t\t<description>Un ejemplo introductorio para mostrar la\
sintaxis KML.</description>\n']
    fin = ['\t</Document>\n', '</kml>\n']
    if not ultima_salida: return print("No se pudo exportar kml", file=sys.stderr)
    aeropuertos = ultima_salida.split(' -> ')
    with open(archivo, 'w') as f:
        f.writelines(intro)
        for a in aeropuertos:
            f.write(f'\t\t<Placemark>\n\t\t\t<name>{a}</name>\n\t\t\t<Point>\n\
\t\t\t\t<coordinates>{", ".join(coordenadas[a])}</coordinates>\n\
\t\t\t</Point>\n\t\t</Placemark>\n')
        for i in range(len(aeropuertos)-1):
            f.write(f'\t\t<Placemark>\n\t\t\t<LineString>\n\
\t\t\t\t<coordinates>{", ".join(coordenadas[aeropuertos[i]])} {", ".join(coordenadas[aeropuertos[i+1]])}</coordinates>\n\
\t\t\t</LineString>\n\t\t</Placemark>\n')
        f.writelines(fin)
    print("OK")


'''********************************************************
*                 FUNCIONES AUXILIARES                    *
********************************************************'''

''' validaciones '''
def print_error(mensaje): sys.stderr.write(mensaje)

''' camino_escalas '''
def rapido(peso): return peso[0]

def barato(peso): return peso[1]

def frecuencia(peso): return peso[2]

def frecuencia_inv(peso): return (1000 / frecuencia(peso))

def obtener_recorrido(origen, destino, func, extra): # func es el algoritmo que se utiliza para obtener el camino.
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

main(sys.argv, dict_aeropuertos, grafo_vuelos)