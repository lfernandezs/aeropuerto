from grafo import Grafo
from pila import Pila
from biblioteca import bfs, dfs, orden_topologico_bfs, orden_topologico_dfs
from testing import print_test, print_titulo

def pruebas_excepciones():

    ''' Declaración de variables '''
    g = Grafo()

    ''' Inicio de Pruebas '''
    try:
        g.quitar_vertice("A")
    except ValueError:
        print_test("Quitar vértice que no pertenece da una excepción", True)
    try:
        g.adyacentes("A")
    except ValueError:
        print_test("Ver adyacentes de vértice que no existe da una excepción", True)
    try:
        g.agregar_arista("A", "B", 0)
    except ValueError:
        print_test("Agregar arista entre vértices que no existen da una excepción", True)
    g.agregar_vertice("Z")
    try:
        g.agregar_arista("Z", "B", 0)
    except ValueError:
        print_test("Agregar arista entre vértices que no existen da una excepción", True)
    try:
        g.quitar_arista("A", "B")
    except ValueError:
        print_test("Quitar arista entre vértices que no existen da una excepción", True)
    try:
        g.quitar_arista("Z", "B")
    except ValueError:
        print_test("Agregar arista entre vértices que no existen da una excepción", True)
    g.quitar_vertice("Z")
    try:
        g.vertice_aleatorio()
    except ValueError:
        print_test("Obtener un vértice aleatorio de un grafo vacío da una excepcióñ", True)
    try:
        g.son_adyacentes("A", "B")
    except ValueError:
        print_test("Obtener si son adyacentes dos vértices que no existen, da una excepción", True)
    try:
        g.peso_arista("A", "B")
    except ValueError:
        print_test("Obtener peso de aristas que no existen, da una excepción", True)
    g.agregar_vertice("A")
    g.agregar_vertice("B")
    try:
        g.peso_arista("A", "B")
    except ValueError:
        print_test("Obtener peso de aristas que no son adyacentes, da una excepción", True)
    try:
        g.adyacentes("C")
    except ValueError:
        print_test("Obtener adyacentes de un vértice que no existe, da una excepción", True)

def prueba_iterar():

    ''' Declaración de variables '''
    g = Grafo()
    vertices = ["A", "B", "C", "D"]
    for v in vertices:
        g.agregar_vertice(v)
    estado = True
    cont = 0

    ''' Inicio de Pruebas '''
    print_titulo("\nPRUEBAS ITERADOR\n")
    for v in g:
        if v not in vertices:
            estado = False
        cont += 1
    print_test("Se iteró correctamente", estado and cont == len(vertices))         

def grafo_vacio():

    ''' Declaración de variables '''
    g = Grafo()

    ''' Inicio de Pruebas '''
    print_titulo("\nPRUEBAS GRAFO VACÍO\n")
    print_test("La cantidad es 0", g.cantidad == 0)
    print_test("El vertice A no pertenece", not g.vertice_pertenece("A"))
    print_test("Obtener vertices devuelve lista vacía", len(g.obtener_vertices()) == 0)
    print_test("Obtener aristas devuelve lista vacía", len(g.obtener_aristas()) == 0)

def agregar_quitar_vertices():

    ''' Declaración de variables '''
    g = Grafo()
    a = 'A'
    b = 'B'
    c = 'C'
    d = 'D'
    vertices = [a, b, c, d]
    
    ''' Inicio de Pruebas '''
    print_titulo("\nPRUEBAS AGREGAR Y QUITAR VERTICES\n")
    print_test("Agregar vertice A devuelve True", g.agregar_vertice(a))
    print_test("La cantidad es 1", g.cantidad_vertices() == 1)
    print_test("El vertice A pertenece al grafo", g.vertice_pertenece(a))
    print_test("La cantidad es 1", g.cantidad_vertices() == 1)
    print_test("Agregar vertice B devuelve True", g.agregar_vertice(b))
    print_test("La cantidad es 2", g.cantidad_vertices() == 2)
    print_test("El vertice B pertenece al grafo", g.vertice_pertenece(b))
    print_test("Agregar vertice que ya pertenece devuelve False", not g.agregar_vertice(a))
    print_test("Agregar vertice C devuelve True", g.agregar_vertice(c))
    print_test("La cantidad es 3", g.cantidad_vertices() == 3)
    print_test("El vertice C pertenece al grafo", g.vertice_pertenece(c))
    print_test("Agregar vertice D devuelve True", g.agregar_vertice(d))
    print_test("La cantidad es 4", g.cantidad_vertices() == 4)
    print_test("El vertice D pertenece al grafo", g.vertice_pertenece(d))
    print_test("Obtener vértice random es a, b, c o d", g.vertice_aleatorio() in vertices)
    vertices_aux = g.obtener_vertices()
    estado = True
    for v in vertices_aux:
        if v not in vertices:
            estado = False
    print_test("Obtener vértices devuelve todos los vértices", estado)
    print_test("Quitar vertice A devuelve True", g.quitar_vertice(a))
    print_test("La cantidad es 3", g.cantidad_vertices() == 3)
    print_test("El vertice A no pertenece al grafo", not g.vertice_pertenece(a))
    print_test("Quitar vertice que no pertenece devuelve False", not g.quitar_vertice(a))
    print_test("La cantidad es 3", g.cantidad_vertices() == 3)
    print_test("Quitar vertice B devuelve True", g.quitar_vertice(b))
    print_test("La cantidad es 2", g.cantidad_vertices() == 2)
    print_test("Quitar vertice que no pertenece devuelve False", not g.quitar_vertice(b))
    print_test("Quitar vertice C devuelve True", g.quitar_vertice(c))
    print_test("La cantidad es 1", g.cantidad_vertices() == 1)
    print_test("Quitar vertice que no pertenece devuelve False", not g.quitar_vertice(c))
    print_test("Quitar vertice D devuelve True", g.quitar_vertice(d))
    print_test("La cantidad es 0", g.cantidad_vertices() == 0)
    print_test("Quitar vertice que no pertenece devuelve False", not g.quitar_vertice(d))

def agregar_quitar_aristas():

    ''' Declaración de variables '''
    g = Grafo()
    a = "A"
    b = "B"
    c = "C"
    g.agregar_vertice(a)
    g.agregar_vertice(b)
    g.agregar_vertice(c)

    ''' Inicio de pruebas '''
    print_titulo("\nPRUEBAS AGREGAR Y QUITAR ARISTAS\n")
    print_test("Agregar arista devuelve True", g.agregar_arista(a, b, 10))
    print_test("Agregar arista devuelve True", g.agregar_arista(b, c, 20))
    print_test("Agregar arista devuelve True", g.agregar_arista(c, a, 30))
    print_test("Obtener peso devuelve 10", g.peso_arista(a, b) == 10)
    print_test("Obtener peso devuelve 20", g.peso_arista(b, c) == 20)
    print_test("Obtener peso devuelve 30", g.peso_arista(c, a) == 30)
    print_test("Los adyacentes a 'A' son 'B' y 'C'", b in g.adyacentes(a) and c in g.adyacentes(a) and len(g.adyacentes(a)) == 2)
    print_test("Los adyacentes a 'B' son 'A' y 'C'", a in g.adyacentes(b) and c in g.adyacentes(b) and len(g.adyacentes(b)) == 2)
    print_test("Los adyacentes a 'C' son 'B' y 'A'", a in g.adyacentes(c) and b in g.adyacentes(c) and len(g.adyacentes(c)) == 2)
    print_test("Quitar arista entre 'A' y 'B' devuelve True", g.quitar_arista(a, b))
    print_test("'A' y 'B' no son adyacentes", b not in g.adyacentes(a) and a not in g.adyacentes(b))
    aristas = [('A', 'C', 30), ('C', 'A', 30), ('B', 'C', 20), ('C', 'B', 20)]
    estado = True
    for arista in g.obtener_aristas():
        if not arista in aristas:
            estado = False
    print_test("obtener_aristas devuelve todas las aristas", estado and len(g.obtener_aristas()) == 2*2)
    print_test("A y C son adyacentes", g.son_adyacentes(a, c))
    print_test("A y B no son adyacentes", not g.son_adyacentes(a, b))

def prueba_bfs():

    ''' Declaración de variables '''
    g = Grafo()
    g.agregar_vertice("1")
    g.agregar_vertice("2")
    g.agregar_vertice("3")
    g.agregar_vertice("4")
    g.agregar_vertice("5")
    g.agregar_arista("3", "2", 0)
    g.agregar_arista("2", "1", 0)
    g.agregar_arista("2", "5", 0)
    g.agregar_arista("4", "1", 0)
    g.agregar_arista("4", "5", 0)

    ''' Inicio de pruebas '''
    print_titulo("\nPRUEBAS BFS\n")
    padres, orden = bfs(g, "3")
    print_test("Orden de 3 es 0", orden["3"] == 0)
    print_test("Orden de 2 es 1", orden["2"] == 1)
    print_test("Orden de 1 es 2", orden["1"] == 2)
    print_test("Orden de 5 es 2", orden["5"] == 2)
    print_test("Orden de 4 es 3", orden["4"] == 3)
    print_test("Padre de 3 es None", padres["3"] == None)
    print_test("Padre de 2 es 3", padres["2"] == "3")
    print_test("Padre de 1 es 2", padres["1"] == "2")
    print_test("Padre de 5 es 2", padres["5"] == "2")
    print_test("Padre de 4 es 1 o 5", padres["4"] == "1" or padre["4"] == "5")

def prueba_dfs():

    ''' Declaración de variables '''
    g = Grafo()
    g.agregar_vertice("1")
    g.agregar_vertice("2")
    g.agregar_vertice("3")
    g.agregar_vertice("4")
    g.agregar_vertice("5")
    g.agregar_arista("3", "2", 0)
    g.agregar_arista("2", "1", 0)
    g.agregar_arista("2", "5", 0)
    g.agregar_arista("4", "1", 0)
    g.agregar_arista("4", "5", 0)

    ''' Inicio de pruebas '''
    print_titulo("\nPRUEBAS DFS\n")
    print("    1    ")
    print("  /   \  ")
    print(" 2--3  4 ")
    print("  \   /  ")
    print("    5    ")
    visitados = set()
    padre = {}
    orden = {}
    padre["3"] = None
    orden["3"] = 0
    dfs(g, "3", visitados, padre, orden)
    for vertice in padre:
        print(vertice, end = ' -> ')
        print(padre[vertice])
        print("orden:", orden[vertice])

def prueba_orden_topologico():

    ''' Declaración de variables '''
    g = Grafo(True)
    g.agregar_vertice("Remera")
    g.agregar_vertice("Buzo")
    g.agregar_vertice("Guantes")
    g.agregar_vertice("Medias")
    g.agregar_vertice("Zapatillas")
    g.agregar_vertice("Ropa interior")
    g.agregar_vertice("Pantalones")
    g.agregar_vertice("Cinturón")
    g.agregar_arista("Remera", "Buzo")
    g.agregar_arista("Remera", "Guantes")
    g.agregar_arista("Medias", "Zapatillas")
    g.agregar_arista("Ropa interior", "Pantalones")
    g.agregar_arista("Pantalones", "Zapatillas")
    g.agregar_arista("Pantalones", "Cinturón")
    ''' Inicio de pruebas '''
    print_titulo("\nPRUEBAS ORDEN TOPOLÓGICO\n")
    print("BFS:", orden_topologico_bfs(g))

    visitados = set()
    pila = Pila()
    for v in g:
        if v not in visitados:
            orden_topologico_dfs(g, v, pila, visitados)
    print("DFS:", pila.pila_a_lista())

def pruebas(): # FALTAN PRUEBAS GRAFO DIRIGIDO
    pruebas_excepciones()
    prueba_iterar()
    grafo_vacio()
    agregar_quitar_vertices()
    agregar_quitar_aristas()
    prueba_bfs()
    prueba_dfs()
    prueba_orden_topologico()

pruebas()