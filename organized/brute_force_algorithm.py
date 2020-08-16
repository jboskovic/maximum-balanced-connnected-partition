from graph import Graph
import itertools
from individual import Individual
import gc


class BruteForce:
    def __init__(self, graph):
        self.graph = graph

    # proveravamo sva moguca resenja
    # mogucnost predstavljamo u obliku niza 0 i 1
    # u tu svrhu koristimo klasu Individual
    # generisemo sve mogucnosti rasporeda 0 i 1
    # ne pravimo razliku izmedju 1000 i 0111 - obe kombinacije predstavljaju istu podelu grafa na dva podgrafa
    # iz tog razloga solutions uzimamo do pola, nakon polovine se resenja ponavljaju
    def brute_force(self):
        best = [float('inf'), Individual(Graph({}, self.graph.cost), [])]
        vertics = self.graph.V
        combinations = list(itertools.product([0, 1], repeat=vertics))
        combinations = combinations[1:len(combinations)//2]
        for comb in combinations:
            ind = Individual(self.graph, comb)
            suma = ind.value()
            if suma > best[0]:
                continue
            else:
                ind.getSubgraphs()
                if ind.subgraph1.connectedGraph() and ind.subgraph2.connectedGraph():
                    best[0] = suma
                    best[1] = ind

        return best[1]
