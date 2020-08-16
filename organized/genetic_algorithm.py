import random
from individual import Individual


class GeneticAlgorithm:
    def __init__(self, nPopulation, nIterations, nElite, nTournament, probability, graph):
        self.nPopulation = nPopulation
        self.nIterations = nIterations
        self.nElite = nElite
        self.nTournament = nTournament
        self.probability = probability
        self.graph = graph

    def selection(self, population):
        min = float('inf')
        for i in range(self.nTournament):
            j = random.randrange(len(population))
            if population[j].fitness < min:
                min = population[j].fitness
                k = j
        return k

    def crossover(self, parent1, parent2, child1, child2):
        i = random.randrange(len(parent1.code))
        for j in range(i):
            child1.code[j] = parent1.code[j]
            child2.code[j] = parent2.code[j]
        for j in range(i, len(parent1.code)):
            child1.code[j] = parent2.code[j]
            child2.code[j] = parent1.code[j]

    # mutacija
    def mutation(self, individual):
        for i in range(len(individual.code)):
            if random.random() > self.probability:
                continue
            individual.code[i] = not individual.code[i]

    def genetic_algorithm(self):
        population = []
        newPopulation = []
        for i in range(self.nPopulation):
            population.append(Individual(self.graph, []))
            newPopulation.append(Individual(self.graph, []))

        for iteration in range(self.nIterations):
            population.sort()
            if population[0].fitness == 0:
                break

            # sacuvam elitne jedinke - prvih nElite jedinki ostaju u populaciji
            for i in range(self.nElite):
                newPopulation[i] = population[i]

            for i in range(self.nElite, self.nPopulation, 2):
                k1 = self.selection(population)
                k2 = self.selection(population)

                self.crossover(population[k1], population[k2],
                               newPopulation[i], newPopulation[i+1])

                self.mutation(newPopulation[i])
                self.mutation(newPopulation[i+1])

                newPopulation[i].getSubgraphs()
                newPopulation[i].fitness = newPopulation[i].fitnessFunction()

                newPopulation[i+1].getSubgraphs()
                newPopulation[i+1].fitness = newPopulation[i +
                                                           1].fitnessFunction()
                newPopulation[i].getSubgraphs()
            population = newPopulation

        population.sort()
        return population[0]
