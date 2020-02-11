from grafo import Grafo
from cola import Cola
from pila import Pila
from heap import Heap
import random

def bfs(grafo,  origen):
    visitados = set()
    padres = {}
    orden = {}
    q = Cola()
    visitados.add(origen)
    padres[origen] = None
    orden[origen] = 0
    q.encolar(origen)
    while not q.esta_vacia():
        v = q.desencolar()
        for w in grafo.adyacentes(v):
            if w not in visitados:
                visitados.add(w)
                padres[w] = v
                orden[w] = orden[v] + 1
                q.encolar(w)
    return padres, orden

def dfs(grafo, v, visitados, padre, orden):
    ''' Para recorrer un grafo no conexo, llamar a dfs para cada nodo no visitado '''
    visitados.add(v)
    for w in grafo.adyacentes(v):
        if w not in visitados:
            padre[w] = v
            orden[w] = orden[v] + 1
            dfs(grafo, w, visitados, padre, orden)

def orden_topologico_bfs(grafo):
    ''' Precondición: el grafo debe ser dirigido '''
    grado = {}
    for v in grafo: grado[v] = 0
    for v in grafo:
        for w in grafo.adyacentes(v):
            grado[w] += 1
    q = Cola()
    for v in grafo:
        if grado[v] == 0: q.encolar(v)
    resul = []
    while not q.esta_vacia():
        v = q.desencolar()
        resul.append(v)
        for w in grafo.adyacentes(v):
            grado[w] -= 1
            if grado[w] == 0:
                q.encolar(w)
    if len(resul) == len(grafo): return resul
    else: return None # Hay ciclo

def orden_topologico_dfs(grafo):
    visitados = set()
    pila = Pila()
    for v in grafo:
        if v not in visitados: _orden_topologico_dfs(grafo, v, pila, visitados)
    return pila.pila_a_lista()

def _orden_topologico_dfs(grafo, v, pila, visitados):
    visitados.add(v)
    for w in grafo.adyacentes(v):
        if w not in visitados:
            _orden_topologico_dfs(grafo, w, pila, visitados)
    pila.apilar(v)

def dijkstra(grafo, origen, peso_func):
    ''' La funcion de comparacion recibe (distancia, vertice) '''
    dist = {}
    padre = {}
    for v in grafo: dist[v] = float("inf")
    dist[origen] = 0
    padre[origen] = None
    q = Heap(cmp_tuplas)
    q.encolar((dist[origen], origen))
    while not q.esta_vacio():
        v = q.desencolar()[1]
        for w in grafo.adyacentes(v):
            if dist[v] + grafo.peso_arista(v, w, peso_func) < dist[w]:
                dist[w] = dist[v] + grafo.peso_arista(v, w, peso_func)
                padre[w] = v
                q.encolar((dist[w], w))
    return padre, dist

def cmp_tuplas(tupla1, tupla2):
    if tupla1[0] > tupla2[0]: return -1
    if tupla1[0] < tupla2[0]: return 1
    return 0

def mst_prim(grafo, peso_func): # función de comparación
    v = grafo.vertice_aleatorio()
    visitados = set()
    visitados.add(v)
    q = Heap(cmp_tuplas)
    arbol = Grafo()
    for vertice in grafo: arbol.agregar_vertice(vertice)
    for w in grafo.adyacentes(v):
        q.encolar((grafo.peso_arista(v, w, peso_func), v, w))
    while not q.esta_vacio():
        peso, v, w = q.desencolar()
        if w in visitados: continue
        arbol.agregar_arista(v, w, peso)
        visitados.add(w)
        for u in grafo.adyacentes(w):
            if u not in visitados:
                q.encolar((grafo.peso_arista(w, u, peso_func), w, u))
    return arbol

def cent_random_walks(grafo, k, l, peso_func):
    cent = {}
    for v in grafo: cent[v] = 0
    for i in range(k):
        origen = grafo.vertice_aleatorio()
        for j in range(l):
            pesos = {}
            for v in grafo.adyacentes(origen):
                if v != None: pesos[v] = grafo.peso_arista(origen, v, peso_func)
            origen = elemento_aleatorio_peso(pesos)
            if not origen: break
            cent[origen] += 1
    return cent

def elemento_aleatorio_peso(pesos):
    ''' Devuelve un elemento aleatorio, priorizando los que tengan más peso.
    pesos: diccionario de elemento:peso. '''
    total = sum(pesos.values())
    rand = random.uniform(0, total)
    acum = 0
    for elemento, peso in pesos.items():
        if acum + peso >= rand:
            return elemento
        acum += peso

def betweeness_centrality(grafo, peso_func):
    cent = {}
    for v in grafo: cent[v] = 0
    for v in grafo:
        padre, dist = dijkstra(grafo, v, peso_func)
        cent_aux = {}
        for w in grafo: cent_aux[w] = 0
        vertices_ordenados = ordenar_vertices(grafo, dist) # 
        for w in vertices_ordenados:
            if padre[w]: cent_aux[padre[w]] += 1 + cent_aux[w]
        for w in grafo:
            if w == v: continue
            cent[w] += cent_aux[w]
    return cent

def ordenar_vertices(grafo, dist):
    vertices = [v for v in grafo]
    return quicksort(vertices, dist)
	
def quicksort(lista, dist): 
	if len(lista) < 2:
		return lista
	mayores, med, menores = particionar(lista, dist)
	return quicksort(mayores, dist) + [med] + quicksort(menores, dist)

def particionar(lista, dist):
    pivote = lista[0]
    menores = []
    mayores = []
    for i in range(1, len(lista)):
        if dist[lista[i]] < dist[pivote]:
            menores.append(lista[i])
        else:
            mayores.append(lista[i])
    return mayores, pivote, menores

def ciclo_largo_n(grafo, origen, n):
    visitados = set()
    camino_actual = [origen]
    return _ciclo_largo_n(grafo, origen, origen, n, visitados, camino_actual)

def _ciclo_largo_n(grafo, v, origen, n, visitados, camino_actual):
    visitados.add(v)
    if len(camino_actual) == n:
        if origen in grafo.adyacentes(v): return camino_actual + [origen]
        return None
    for w in grafo.adyacentes(v):
        if w in visitados: continue
        camino = _ciclo_largo_n(grafo, w, origen, n , visitados, camino_actual + [w])
        if camino: return camino
    visitados.remove(v)
    return None



