def recorrer_mundo(grafo, v, visitados, camino_actual):
    visitados.add(v) # Si está en un país no visitado
    if len(visitados) == 10:
        return camino_actual
    for w in grafo.adyacentes(v):
        solucion = recorrer_mundo(grafo, w, visitados, camino_actual + [w])
        if solucion is not None: return solucion
    visitados.remove(v)
    return None