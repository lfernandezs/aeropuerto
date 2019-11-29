from grafo import Grafo
from cola import Cola

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
                padre[w] = v
                orden[w] = orden[v] + 1
                q.encolar(w)
    return padre, orden