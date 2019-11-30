from grafo import Grafo
from cola import Cola
from pila import Pila

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

def orden_topologico_dfs(grafo, v, pila, visitados):
    visitados.add(v)
    for w in grafo.adyacentes(v):
        if w not in visitados:
            orden_topologico_dfs(grafo, w, pila, visitados)
    pila.apilar(v)