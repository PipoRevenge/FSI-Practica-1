# Search methods

import search

ab = search.GPSProblem('A', 'B'
                       , search.romania)
oe = search.GPSProblem('O', 'E'
                      , search.romania)


print(search.breadth_first_graph_search(ab).path())
print(search.depth_first_graph_search(ab).path())
print(search.branch_and_bound_performance_estimation_search(ab).path())

# Result 1:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
#Branch and bound
#Resultado G:31 V:24 C: 418
#Ruta: [B, P, R, S, A]

#Branch and bound perfomance
#Resultado G:16 V:6 C: 418
#Ruta: [B, P, R, S, A]

