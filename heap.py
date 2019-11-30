class Heap:
    ''' Representa un heap, con operaciones de encolar, desencolar.
    Cumple la propiedad de heap. '''

    def __init__(self, cmp_func):
        ''' Crea un heap de máximos. Recibe una función de comparación. '''
        self.items = []
        self.cant = 0
        self.cmp_func = cmp_func

    def __len__(self):
        ''' Devuelve la cantidad de elementos en el heap. '''
        return self.cant

    def esta_vacio(self):
        ''' Devuelve True si el heap está vacío. '''
        return self.cant == 0

    def encolar(self, x):
        ''' Encola un elemento x en el heap. '''
        self.items.append(x)
        upheap(self.items, self.cant, self.cmp_func)
        self.cant += 1

    def ver_max(self):
        ''' Devuelve el elemento de mayor prioridad del heap. '''
        if self.esta_vacio(): raise ValueError("El heap está vacío.")
        return self.items[0]

    def desencolar(self):
        ''' Desencola el elemento de mayor prioridad y lo devuelve. '''
        if self.esta_vacio(): raise ValueError("El heap esta vacío.")
        x = self.items[0]
        self.items[0] = self.items[-1]
        self.items.pop()
        self.cant -= 1
        downheap(self.items, self.cant, 0, self.cmp_func)
        return x

''' Funciones Auxiliares '''

def upheap(lista, pos, cmp_func):
    if pos == 0: return
    padre = int((pos - 1) / 2)
    if cmp_func(lista[padre], lista[pos]) < 0:
        swap(lista, padre, pos)
        upheap(lista, padre, cmp_func)

def downheap(lista, tam, pos, cmp_func):
    if pos >= tam: return
    padre = pos
    izq = 2 * pos + 1
    der = 2 * pos + 2
    if izq < tam and cmp_func(lista[padre], lista[izq]) < 0: padre = izq
    if der < tam and cmp_func(lista[padre], lista[der]) < 0: padre = der
    if padre != pos:
        swap(lista, pos, padre)
        downheap(lista, tam, padre, cmp_func)

def swap(lista, pos1, pos2):
    lista[pos1], lista[pos2] = lista[pos2], lista[pos1]