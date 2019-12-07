import random

class Grafo:
    ''' Representa un Grafo '''

    def __init__(self, dirigido = True):
        ''' Crea el grafo '''
        self.grafo = {}
        self.cantidad = 0
        self.dirigido = dirigido

    def __iter__(self):
        ''' Devuelve un iterador del grafo '''
        return iter(self.obtener_vertices())
    
    def __len__(self):
        ''' Devuelve el largo del grafo '''
        return len(self.grafo)

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

    def agregar_arista(self, vertice_1, vertice_2, peso=0):
        ''' Recibe dos vertices inmutables y un peso y los une.
        Si la arista ya existía, se modifica el peso. ''' 
        if vertice_1 in self.grafo and vertice_2 in self.grafo:
            self.grafo[vertice_1][vertice_2] = peso
            if not self.dirigido:
                self.grafo[vertice_2][vertice_1] = peso
            return True
        raise ValueError("El vértice no pertenece al grafo")

    def quitar_arista(self, vertice_1, vertice_2):
        ''' Recibe dos vértices y si están unidos, los separa, devuelve True '''
        if vertice_1 in self.grafo and vertice_2 in self.grafo:
            if vertice_2 in self.grafo[vertice_1]:
                self.grafo[vertice_1].pop(vertice_2)
                if not self.dirigido:
                    self.grafo[vertice_2].pop(vertice_1)
                return True
            return False
        raise ValueError("El vértice no pertenece al grafo")

    def vertice_pertenece(self, vertice):
        ''' Devuelve True si el vértice pertenece al grafo '''
        return vertice in self.grafo

    def cantidad_vertices(self):
        ''' Devuelve la cantidad de vértices del grafo '''
        return self.cantidad

    def vertice_aleatorio(self):
        ''' Devuelve un vertice aleatorio '''
        if self.cantidad == 0: raise ValueError("El grafo no tiene vértices")
        return random.choice(list(self.grafo))

    def vertice_aleatorio_peso(self, pesos):
        ''' Devuelve un vértice aleatorio, priorizando los que tengan aristas de más peso.
        pesos en un diccionario de vertice_vecino:peso. '''
        total = sum(pesos.values())
        rand = random.uniform(0, total)
        acum = 0
        for vertice, peso_arista in pesos.items():
            if acum + peso_arista >= rand:
                return vertice
            acum += peso_arista

    def son_adyacentes(self, vertice_1, vertice_2):
        ''' Devuelve True si los vertices que recibió son adyacentes '''
        if not vertice_1 in self.grafo and not vertice_2 in self.grafo: raise ValueError("El vértice no pertenece al grafo")
        return vertice_2 in self.grafo[vertice_1]

    def peso_arista(self, vertice_1, vertice_2, peso_func):
        ''' Recibe dos vértices y si están unidos, devuelve su peso. También
        recibe una función para devolver el peso (el peso no necesariamente es un entero). '''
        if self.son_adyacentes(vertice_1, vertice_2):
            return peso_func(self.grafo[vertice_1][vertice_2])
        raise ValueError("No son adyacentes.")

    def adyacentes(self, vertice):
        ''' Devuelve una lista con los adyacentes al vértice. '''
        adyacentes = []
        if vertice in self.grafo:
            for v in self.grafo[vertice]:
                adyacentes.append(v)
            return adyacentes
        raise ValueError(f"El vértice {vertice} no pertenece al grafo")

    def obtener_vertices(self):
        ''' Devuelve una lista con los vértices del grafo '''
        vertices = []
        for vertice in self.grafo: vertices.append(vertice)
        return vertices

    def obtener_aristas(self):
        ''' Devuelve una lista de tuplas: (vertice, adyacente, peso) '''
        aristas = []
        for vertice in self.grafo:
            for adyacente in self.grafo[vertice]:
                aristas.append((vertice, adyacente, self.grafo[vertice][adyacente]))
        return aristas