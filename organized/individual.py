from graph import Graph
import random
# klasa jedinki
# prosledjujemo joj pocetni graf
# jedinka je reprezentovana u obliku niza nula i jedinica (niz je velicine broja cvorova u grafu)
# nula oznacava da se cvor (indeks niza oznacava cvor) nalazi u jednom podgrafu
# a jedinica da se naalzi u drugom


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

    # definise nacin poredjenja jedinki

    def __lt__(self, other):
        return self.fitness < other.fitness
    # racunamo u odnosu na broj komponenti podgrafova

    def penalty_function(self):
        self.getSubgraphs()
        ncc1 = len(self.subgraph1.connectedComponents())
        ncc2 = len(self.subgraph2.connectedComponents())

        max1 = self.subgraph1.maxCost()
        max2 = self.subgraph2.maxCost()

        return (ncc1-1)*max1 + (ncc2-1)*max2

    # fitnes raacuna koliko su priblizne vrednosti suma dva podgrafa
    # sto je fitnes manji resenje je bolje
    # penalti funcija sluzi kao kazneni poeni ako dobijemo podgrafove
    # koji nisu povezani

    def value(self):
        w1 = 0
        w2 = 0
        for i in range(self.V):
            if self.code[i]:
                w1 += self.graph.cost[i]
            else:
                w2 += self.graph.cost[i]

        return abs(w1-w2)

    def fitnessFunction(self):

        return self.value() + self.penalty_function()

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
