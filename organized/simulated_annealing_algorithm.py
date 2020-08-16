from graph import Graph
from individual import Individual
import random


class SimulatedAnnealing:
    def __init__(self, graph, nIterations):
        self.graph = graph
        self.nIterations = nIterations

    def initialize(self):
        code = []
        for i in range(self.graph.V):
            if random.random() > 0.5:
                code.append(1)
            else:
                code.append(0)
        return code

    def invert(self, code):
        j = random.randrange(len(code))
        code[j] = not code[j]
        return j

    def restore(self, j, code):
        code[j] = not code[j]

    def simulated_annealing(self):
        currentResult = self.initialize()
        currentValue = Individual(self.graph, currentResult)
        bestValue = Individual(self.graph, currentResult)

        for i in range(1, self.nIterations):
            j = self.invert(currentResult)
            newValue = Individual(self.graph, currentResult)
            if newValue.fitness < currentValue.fitness:
                currentValue = Individual(self.graph, newValue.code)
            else:
                p = 1.0 / i**0.5
                q = random.uniform(0, 1)
                if p > q:
                    currentValue = Individual(self.graph, newValue.code)
                else:
                    self.restore(j, currentResult)

            if newValue.fitness < bestValue.fitness:
                bestValue = Individual(self.graph, newValue.code)

        return bestValue
