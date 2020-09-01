from graph import Graph
import random
# klasa jedinki
# prosledjujemo joj pocetni graf
# jedinka je reprezentovana u obliku niza nula i jedinica (niz je velicine broja cvorova u grafu)
# nula oznacava da se cvor (indeks niza oznacava cvor) nalazi u jednom podgrafu
# a jedinica da se naalzi u drugom
from cached_fitness import cached


class Individual:
    def __init__(self, graph, code):
        self.graph = graph
        self.code = []
        self.V = len(graph.adj)
        if code == []:
            for i in range(self.V):
                self.code.append(random.random() < 0.5)
        else:
            self.code = code

        self.fitness = self.fitnessFunction()
        self.subgraph1 = Graph([], [])
        self.subgraph2 = Graph([], [])

    # definise nacin poredjenja jedinki

    def __lt__(self, other):
        return self.fitness < other.fitness

    # penalti funcija sluzi kao kazneni poeni ako dobijemo podgrafove
    # koji nisu povezani
    # racunamo u odnosu na broj komponenti podgrafova

    def penalty_function(self):
        graph1, graph2 = self.getSubgraphs()
        self.subgraph1 = graph1
        self.subgraph2 = graph2
        ncc1 = len(graph1.connectedComponents())
        ncc2 = len(graph2.connectedComponents())

        max1 = graph1.maxCost()
        max2 = graph2.maxCost()

        return (ncc1-1)*max1 + (ncc2-1)*max2

    def value(self):
        w1 = 0
        w2 = 0
        for i in range(self.V):
            if self.code[i]:
                w1 += self.graph.cost[i]
            else:
                w2 += self.graph.cost[i]

        return abs(w1-w2)

    # fitnes raacuna koliko su priblizne vrednosti suma dva podgrafa
    # sto je fitnes manji resenje je bolje
    def fitnessFunction(self):
        code = ''.join(str(v) for v in self.code)
        if code in cached:
            return cached[code]
        else:
            cache = self.value() + self.penalty_function()
            cached[code] = cache
            return cache

    def getSubgraphs(self):
        graph1 = Graph(self.graph.adj.copy(), self.graph.cost)
        graph2 = Graph(self.graph.adj.copy(), self.graph.cost)
        for i in range(self.V):
            if self.code[i]:
                graph2 = graph2.remove_node(i)
            else:
                graph1 = graph1.remove_node(i)
        self.subgraph1 = graph1
        self.subgraph2 = graph2
        return (graph1, graph2)
