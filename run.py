# Search methods
import search

# Five GPS search problems with the map of Romania
ab = search.GPSProblem('A', 'B', search.romania)
oe = search.GPSProblem('O', 'E', search.romania)
gz = search.GPSProblem('G', 'Z', search.romania)
nd = search.GPSProblem('N', 'D', search.romania)
mf = search.GPSProblem('M', 'F', search.romania)
print("1. Breadth First Search.")
print("2. Depth First Search.")
print("3. Branch and Bound Search.")
print("4. Branch and Bound Search Performance Estimation Search.")
option = input("Enter an option(1,2,3 o 4): ")

# Dictionary with names and variables of problems
NamesList = {"Arad Bucharest": ab, "Oradea Eforie": oe, "Giurgiu Zerind":gz,
                "Neam Dobreta": nd, "Mehadia Fargaras": mf}

# A for loop to walk through the array NamesList
for name, problem in NamesList.items():
    #Print the name asociated to each problem
    print(name)
    #For each problem, the indicated algorithm is made
    if(option == '1'):
        print("Ruta: ", search.breadth_first_graph_search(problem).path())
    elif(option == '2'):
        print("Ruta: ", search.depth_first_graph_search(problem).path())
    elif(option == '3'):
        print("Ruta: ", search.branch_and_bound_search(problem).path())
    elif(option == '4'):
        print("Ruta:", search.branch_and_bound_performance_estimation_search(problem).path())
    print()

# Result 1:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450

