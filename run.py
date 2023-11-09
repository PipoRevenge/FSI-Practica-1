# Search methods
import search

# Creamos dos problemas de búsqueda GPS con el mapa de Rumanía
ab = search.GPSProblem('A', 'B', search.romania)
oe = search.GPSProblem('O', 'E', search.romania)
gz = search.GPSProblem('G', 'Z', search.romania)
nd = search.GPSProblem('N', 'D', search.romania)
mf = search.GPSProblem('M', 'F', search.romania)
print("1. Busqueda en Anchura.")
print("2. Busqueda en Profundidad.")
print("3. Busqueda con ramificación y acotación.")
print("4. Busqueda con ramificación y acotación con subestimacion.")
opcion = input("Ingresa una opcion (1,2,3 o 4): ")

# Creamos una lista de nombres y variables para cada problema/test
ListaNombres = {"Arad Bucharest": ab, "Oradea Eforie": oe,"Giurgiu Zerind":gz,
                "Neam Dobreta": nd, "Mehadia Fargaras": mf}

# Creamos un bucle for que recorra cada elemento de la lista
for nombre, problema in ListaNombres.items():
    # Imprimimos el nombre y la variable asociada a cada problema
    print(nombre)
    if(opcion == '1'):
        print("Ruta: ", search.breadth_first_graph_search(problema).path())
    elif(opcion == '2'):
        print("Ruta: ", search.depth_first_graph_search(problema).path())
    elif(opcion == '3'):
        print("Ruta: ", search.branch_and_bound_search(problema).path())
    elif(opcion == '4'):
        print("Ruta:", search.branch_and_bound_performance_estimation_search(problema).path())
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

