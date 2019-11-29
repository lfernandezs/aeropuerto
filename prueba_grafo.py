from grafo import Grafo
from testing import print_test, print_titulo

def grafo_vacio():
    ''' Declaración de variables '''
    g = Grafo()

    ''' Inicio de Pruebas '''
    print_titulo("\nPRUEBAS GRAFO VACÍO\n")
    print_test("La cantidad es 0", g.cantidad == 0)
    print_test("Quitar vértice devuelve False", not g.quitar_vertice("A"))
    print_test("Quitar arista devuelve False", not g.quitar_arista("A", "A"))
    print_test("El vertice A no pertenece", not g.vertice_pertenece("A"))
    print_test("Vertice aleatorio devuelve None", not g.vertice_aleatorio())
    print_test("son_adyacentes devuelve false", not g.son_adyacentes("A", "B"))
    print_test("El peso de la arista es None", not g.peso_arista("A", "B"))
    print_test("Adyancentes devuelve None", not g.adyacentes("A"))
    print_test("Obtener vertices devuelve lista vacía", len(g.obtener_vertices()) == 0)
    print_test("Obtener aristas devuelve lista vacía", len(g.obtener_artistas()) == 0)

def agregar_quitar_vertices():
    ''' Declaración de variables '''
    g = Grafo()
    a = 'A'
    b = 'B'
    c = 'C'
    d = 'D'
    
    ''' Inicio de Pruebas '''
    print_titulo("\nPRUEBAS AGREGAR Y QUITAR VERTICES")
    print_test("Agregar vertice A devuelve True", g.agregar_vertice(a))
    print_test("La cantidad es 1", g.cantidad_vertices() == 1)
    print_test("El vertice A pertenece al grafo", g.vertice_pertenece(a))
    print_test("Agregar vertice que ya pertenece devuelve False", not g.agregar_vertice(a))
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


def pruebas():
    grafo_vacio()
    agregar_quitar_vertices()
    #agregar_quitar_aristas()
    #prueba_obtener_vertices()
    #prueba_obtener_aristas()

pruebas()