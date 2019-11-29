class Cola:
    ''' Representa a una cola, con operaciones de encolar y
    desencolar. Cumple FIFO. '''
    
    def __init__(self):
        ''' Crea una cola vacía. '''
        self.items = []

    def encolar(self, x):
        ''' Encola el elemento x. '''
        self.items.append(x)

    def desencolar(self):
        ''' Elimina el primer elemento de la cola y lo devuelve.
        Si la cola está vacía, devuelve None '''
        if self.esta_vacia(): raise ValueError("La cola está vacía.")
        return self.items.pop(0)

    def esta_vacia(self):
        ''' Devuelve True si la cola está vacía, sino False '''
        return len(self.items) == 0

    def ver_primero(self):
        ''' Devuelve el primer elemento de la cola '''
        return self.items[0]

    
