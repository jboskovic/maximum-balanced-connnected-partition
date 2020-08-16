from graph import Graph
from individual import Individual


class GreedyAlgorithm:
    def __init__(self, graph):
        self.graph = graph

    def costSubgraph(self, code):
        w1 = 0
        w2 = 0
        for i in range(len(code)):
            if code[i]:
                w2 += self.graph.cost[i]
            else:
                w1 += self.graph.cost[i]
        return (w1, w2)

    def greedy_algorithm(self):
        cost = {k: v for k, v in sorted(
            self.graph.cost.items(), key=lambda item: item[1], reverse=True)}
        code = [1] * self.graph.V
        indeks = list(cost.keys())[0]
        code[indeks] = 0
        w1, w2 = self.costSubgraph(code)
        w = self.graph.getCostSum()

        while w1 < w/2:
            v0 = []
            for i in range(len(code)):
                if code[i] == 1:
                    temp = code.copy()
                    temp[i] = 0
                    ind = Individual(self.graph, temp)
                    ind.getSubgraphs()
                    if ind.subgraph1.connectedGraph() and ind.subgraph2.connectedGraph():
                        v0.append(i)
            min = float('inf')
            node = -1
            for i in range(len(v0)):
                if self.graph.cost[v0[i]] < min:
                    min = self.graph.cost[v0[i]]
                    node = v0[i]
            if self.graph.cost[node] < (w-2*w1):
                code[node] = 0
                w1, w2 = self.costSubgraph(code)
            else:
                break

        return Individual(self.graph, code)
