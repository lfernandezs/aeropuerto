import sys
from grafo import Grafo
from biblioteca import *

COMANDOS = ("listar_operaciones", "camino_mas", "camino_escalas", "nueva_aerolinea", "centralidad_aprox", "salir")

dict_aeropuertos = {}
grafo_vuelos = Grafo(True)
grafo_rutas = Grafo(False)

'''********************************************************
*             FUNCION PRINCIPAL DEL PROGRAMA              *
********************************************************'''

def main(argv, dict_aeropuertos, grafo_vuelos):
    # Cargar datos
    if not cargar_datos(argv, dict_aeropuertos, grafo_vuelos): return
    # Valido la entrada
    entrada = ""
    while entrada != "salir":
        entrada = input("Ingrese un comando: ")
        validar_entrada(entrada.split(' '))

def cargar_datos(argv, dict_aeropuertos, grafo_vuelos):
    ''' Carga los destinos en un diccionario con sus aeropuertos
    como valor y los vuelos en un grafo.'''
    if len(argv) != 3: return False # Mensaje?
    ruta_aeropuertos = argv[1]
    ruta_vuelos = argv[2]
    with open(ruta_aeropuertos, 'r') as f_aeropuertos: # Checkear que exista
        for linea in f_aeropuertos:
            ciudad, codigo, lat, lon = linea.split(',') # Lat y lon?
            grafo_vuelos.agregar_vertice(codigo)
            grafo_rutas.agregar_vertice(codigo)
            if ciudad in dict_aeropuertos: dict_aeropuertos[ciudad].append(codigo)
            else: dict_aeropuertos[ciudad] = [codigo]
    with open(ruta_vuelos, 'r') as f_vuelos:
        for linea in f_vuelos:
            i, j, tiempo, precio, vuelos = linea.split(',')
            grafo_vuelos.agregar_arista(i, j, (int(precio), int(tiempo), int(vuelos))) # El peso es una tupla
            grafo_rutas.agregar_arista(i, j, (int(precio), int(tiempo), int(vuelos))) # Ver si es necesario todo esto
    return True

def validar_entrada(entrada): # Faltan validar cosas
    if not entrada[0] in COMANDOS:
        print("El comando", entrada[0], "no existe.")
        return
    if entrada[0] == COMANDOS[0]: listar_operaciones()
    elif entrada[0] == COMANDOS[1]:
        modo, origen, destino = ' '.join(entrada[1:]).split(',')
        return camino_mas(modo, origen, destino)
    elif entrada[0] == COMANDOS[2]:
        origen, destino = ' '.join(entrada[1:]).split(',')
        return camino_escalas(origen, destino)
    elif entrada[0] == COMANDOS[3]:
        return nueva_aerolinea(entrada[1])
    elif entrada[0] == COMANDOS[4]:
        return centralidad_aprox(int(entrada[1]))
    elif entrada[0] == COMANDOS[-1]: return

'''********************************************************
*               IMPLEMENTACIÓN DE COMANDOS                *
********************************************************'''

def listar_operaciones():
    for comando in COMANDOS: print(comando)

def camino_mas(modo, origen, destino):
    ''' Dijkstra '''
    modos = {'barato':barato, 'rapido':rapido}
    if not modo in modos or not origen in dict_aeropuertos or not destino in dict_aeropuertos: return print_error(COMANDOS[1])
    trayecto = obtener_camino(origen, destino, dijkstra, modos[modo])
    if not trayecto: return print("No hay forma de llegar.")
    for v in trayecto[:0:-1]: print(v, end='->')
    print(trayecto[0])

def camino_escalas(origen, destino):
    ''' BFS '''
    if not origen in dict_aeropuertos or not destino in dict_aeropuertos: return print_error(COMANDOS[2])
    trayecto = obtener_camino(origen, destino, bfs, None)
    if not trayecto: return print("No hay forma de llegar.")
    for v in trayecto[:0:-1]: print(v, end='->')
    print(trayecto[0])

#def centralidad(n)
    ''' Betweeness Centrality '''


def centralidad_aprox(n): # Checkeaer si cent_random_walks está bien implementado
    ''' Betweeness Centrality aprox '''
    cent = cent_random_walks(grafo_vuelos, 10, 10, frecuencia)
    aux = [(k, v) for k, v in cent.items()]
    aux = sorted(aux, key=lambda x: x[1], reverse=True)
    for i in range(n-1): print(aux[i][0], end=', ')
    print(aux[n-1][0])

#def pagerank(n)
    ''' Pagerank '''

def nueva_aerolinea(ruta):
    ''' Árbol de tendido mínimo '''
    with open(ruta, 'w') as f:
        rutas = mst_prim(grafo_rutas, barato) 
        for v in rutas:
            for w in rutas.adyacentes(v):
                f.write(f'{v}, {w}\n')
    print('OK')

#def recorrer_mundo(origen)
    '''BackTracking?'''

#def recorrer_mundo_aprox(origen)
    '''Greedy?'''

#def vacaciones(origen, n)
    ''' Backtracking '''

#def itinerario(ruta)
    ''' Orden Topológico '''

#def exportar_kml(archivo)

'''********************************************************
*                 FUNCIONES AUXILIARES                    *
********************************************************'''

''' validaciones '''
def print_error(comando): print(f"Error en comando {comando}")

''' camino_escalas '''
def barato(peso): return peso[0]

def rapido(peso): return peso[1]

def frecuencia(peso): return peso[2]

def obtener_camino(origen, destino, func, extra): # func es la función que se utiliza para obtener el camino.
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
                dist = dist_aux
                padres = padres_aux
    while aerop_destino != None:
        trayecto.append(aerop_destino)
        aerop_destino = padres[aerop_destino]
    return trayecto

main(sys.argv, dict_aeropuertos, grafo_vuelos)