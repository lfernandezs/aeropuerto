from grafo import Grafo
from testing import print_test, print_titulo

def grafo_vacio():
    ''' Declaración de variables '''
    g = Grafo()

    ''' Inicio de Pruebas '''
    print_titulo("\nPRUEBAS GRAFO VACÍO\n")
    print_test("La cantidad es 0", g.cantidad == 0)
    print_test("Quitar vértice devuelve False", not g.quitar_vertice("A"))
    print_test("El vertice A no pertenece", not g.vertice_pertenece("A"))
    print_test("Adyancentes devuelve None", not g.adyacentes("A"))
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
    print_titulo("\nPRUEBAS AGREGAR Y QUITAR VERTICES")
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
    print_test("Agregar arista en vertice que no existe, devuelve False", not g.agregar_arista("A", "D", 6))
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


def pruebas():
    grafo_vacio()
    agregar_quitar_vertices()
    agregar_quitar_aristas()

pruebas()