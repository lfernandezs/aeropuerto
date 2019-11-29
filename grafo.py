import random

class Grafo:
    ''' Representa un Grafo no dirigido, pesado '''

    def __init__(self):
        ''' Crea el grafo '''
        self.grafo = {}
        self.cantidad = 0

    def agregar_vertice(self, vertice):
        ''' Recibe un vértice inmutable y lo agrega al grafo, devuelve True '''
        if not vertice in self.grafo:
            self.grafo[vertice] = {}
            self.cantidad += 1
            return True
        return False

    def quitar_vertice(self, vertice):
        ''' Si existe el vertice, lo elimina y devuelve True '''
        if vertice in self.grafo:
            self.grafo.pop(vertice)
            for v in self.grafo:
                if v in self.grafo[v]:
                    self.grafo[v].pop(vertice)
            self.cantidad -= 1
            return True
        return False

    def agregar_arista(self, vertice_1, vertice_2, peso):
        ''' Recibe dos vertices inmutables y un peso y los une, devuelve True.
        Si la arista ya existía, se modifica el peso. ''' 
        if vertice_1 in self.grafo and vertice_2 in self.grafo:
            self.grafo[vertice_1][vertice_2] = peso
            self.grafo[vertice_2][vertice_1] = peso
            return True
        return False

    def quitar_arista(self, vertice_1, vertice_2):
        ''' Recibe dos vértices y si están unidos, los separa, devuelve True '''
        if vertice_1 in self.grafo and vertice_2 in self.grafo:
            self.grafo[vertice_1].pop(vertice_2)
            self.grafo[vertice_2].pop(vertice_1)
            return True
        return False

    def vertice_pertenece(self, vertice):
        ''' Devuelve True si el vértice pertenece al grafo '''
        return vertice in self.grafo

    def cantidad_vertices(self):
        ''' Devuelve la cantidad de vértices del grafo '''
        return self.cantidad

    def vertice_aleatorio(self):
        ''' Devuelve un vertice aleatorio '''
        if self.cantidad == 0: return None
        return random.choice(self.grafo)


    def son_adyacentes(self, vertice_1, vertice_2):
        ''' Devuelve True si los vertices que recibió son adyacentes '''
        if not vertice_1 in self.grafo: return False
        return vertice_2 in self.grafo[vertice_1]

    def peso_arista(self, vertice_1, vertice_2):
        ''' Recibe dos vértices y si están unidos, devuelve su peso '''
        if self.son_adyacentes(vertice_1, vertice_2):
            return self.grafo[vertice_1][vertice_2]
        return None

    def adyacentes(self, vertice):
        ''' Devuelve una lista con los adyacentes al vértice, sino existe: None '''
        adyacentes = []
        if vertice in self.grafo:
            for v in self.grafo[vertice]:
                adyacentes.append(v)
            return adyacentes
        return None

    def obtener_vertices(self):
        ''' Devuelve una lista con los vértices del grafo '''
        vertices = []
        for vertice in self.grafo: vertices.append(vertice)
        return vertices

    def obtener_artistas(self):
        ''' Devuelve una lista de tuplas: (vertice, adyacente, peso) '''
        aristas = []
        for vertice in self.grafo:
            for adyacente in self.grafo[vertice]:
                aristas.append(vertice, adyacente, self.grafo[vertice][adyacente])
        return aristas