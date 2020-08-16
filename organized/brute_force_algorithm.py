from graph import Graph
from itertools import combinations
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
        k = vertics//2
        done = False
        for i in range(1, k):
            combes = list(combinations(range(vertics), k))
            for comb in combes:
                code = [0] * vertics
                for index in comb:
                    code[index] = 1
                ind = Individual(self.graph, code)
                suma = ind.value()
                if suma > best[0]:
                    continue
                else:
                    ind.getSubgraphs()
                    if ind.subgraph1.connectedGraph() and ind.subgraph2.connectedGraph():
                        best[0] = suma
                        best[1] = ind

        return best[1]
