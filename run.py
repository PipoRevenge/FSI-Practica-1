# Search methods

import search

ab = search.GPSProblem('A', 'B'
                       , search.romania)
oe = search.GPSProblem('O', 'E'
                      , search.romania)
ListaNombres ={"Arad Bucharest", "Oradea Eforie"}

print(search.breadth_first_graph_search(ab).path())
print(search.depth_first_graph_search(ab).path())
print(search.branch_and_bound_performance_estimation_search(ab).path())

# Creamos dos problemas de búsqueda GPS con el mapa de Rumanía
ab = search.GPSProblem('A', 'B', search.romania)
oe = search.GPSProblem('O', 'E', search.romania)
gz = search.GPSProblem('G', 'Z', search.romania)
nd = search.GPSProblem('N', 'D', search.romania)
mf = search.GPSProblem('M', 'F', search.romania)


# Creamos una lista de nombres y variables para cada problema
ListaNombres = {"Arad Bucharest": ab, "Oradea Eforie": oe,"Giurgiu Zerind":gz,
                "Neam Dobreta": nd, "Mehadia Fargaras": mf}

# Creamos un bucle for que recorra cada elemento de la lista
for nombre, problema in ListaNombres.items():
    # Imprimimos el nombre y la variable asociada a cada problema
    print(nombre)
    # Resolvemos el problema usando tres algoritmos de búsqueda diferentes y los imprimimos
    #Por depurar comenta los metodos que no quieras ver por pereza a cambiartodo
    #print("Búsqueda en anchura:", search.breadth_first_graph_search(problema).path())
    #print("Búsqueda en profundidad:", search.depth_first_graph_search(problema).path())
    print("Búsqueda con ramificación y acotación:", search.branch_and_bound_performance_estimation_search(problema).path())
    # Dejamos una línea en blanco para separar cada problema
    print()

# Result 1:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
#Branch and bound
#Resultado G:31 V:24 C: 418
#Ruta: [B, P, R, S, A]

#Branch and bound perfomance
#Resultado G:16 V:6 C: 418
#Ruta: [B, P, R, S, A]

