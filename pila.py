class Pila:
    ''' Representa una pila, con operaciones de apilar y
    desapilar. Cumple FIFO. '''

    def __init__(self):
        ''' Crea una pila vacía '''
        self.items = []

    def apilar(self, x):
        ''' Apila el elemento x. '''
        self.items.append(x)

    def desapilar(self):
        ''' Elimina el elemento del tope de la pila y
        lo devuelve. Si la pila está vacía, lanza una excepción. '''
        if self.esta_vacia(): raise ValueError("La pila está vacía.")
        return self.items.pop()

    def esta_vacia(self):
        ''' Si la pila está vacía, devuelve True. '''
        return len(self.items) == 0

    def ver_tope(self):
        ''' Devuelve el tope de la pila. '''
        if self.esta_vacia(): raise ValueError("La pila está vacía.")
        return self.items[-1]

    def pila_a_lista(self):
        return self.items[::-1]