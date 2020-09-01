from graph import Graph
from genetic_algorithm import GeneticAlgorithm
from brute_force_algorithm import BruteForce
from greedy_algorithm import GreedyAlgorithm
from simulated_annealing_algorithm import SimulatedAnnealing
import time



def print_solution(solution):
    print('---------------------------------')
    print('Solution: ')
    print('Graph1 - ', solution.subgraph1.adj)
    print('Graph2 - ', solution.subgraph2.adj)
    print('Fitness - ', solution.fitness)
    print('Code - ', solution.code)
    print('---------------------------------')
    print()


def brute_force(graph):
    print('Brute-force: ')
    brute_force = BruteForce(graph)
    solution = brute_force.brute_force()
    print_solution(solution)


def greedy(graph):
    print('Greedy: ')
    greedy_algorithm = GreedyAlgorithm(graph)
    solution = greedy_algorithm.greedy_algorithm()
    print_solution(solution)


def genetic(graph):
    print('Genetic: ')
    nTournament = 6
    probability = 0.05
    nPopulation = 100
    nIterations = 500
    nElite = 30

    genetic = GeneticAlgorithm(
        nPopulation, nIterations, nElite, nTournament, probability, graph)
    solution = genetic.genetic_algorithm()
    print_solution(solution)


def simulated_annealing(graph, nIterations):
    print('Simulated-annealing: ')
    simulated_annealing = SimulatedAnnealing(graph, nIterations)
    solution = simulated_annealing.simulated_annealing()
    print_solution(solution)


if __name__ == "__main__":

    # primer 1
    adjacency_list = {0: [1, 2, 5], 1: [0, 5, 2], 2: [
        0, 1, 3, 5], 3: [2, 4], 4: [3, 5], 5: [0, 1, 2, 4]}
    vertics_cost = {0: 8, 1: 4, 2: 1, 3: 6, 4: 5, 5: 4}
    graph = Graph(adjacency_list, vertics_cost)

    # brute force
    start = time.time()
    brute_force(graph)
    end = time.time()
    time_brute= end - start
    

    # greedy
    start = time.time()
    greedy(graph)
    end = time.time()
    time_greedy= end - start
    

    # genetic
    start = time.time()
    genetic(graph)
    end = time.time()
    time_genetic= end - start
    

    # simulated annealing
    start = time.time()
    simulated_annealing(graph, 10000)
    end = time.time()
    time_simulated= end - start
    
    
    #time 
    print('Brute force  - time:',time_brute)
    print('Greedy       - time:',time_greedy)
    print('Genetic      - time:',time_genetic)
    print('Simulated a. - time:',time_brute)
    
    print('------------------------------------------------------------------------------------')
    

    # primer 2
    adjacency_list = {0: [1, 2], 1: [0, 4], 2: [0, 3], 3: [2, 4], 4: [1, 3]}
    vertics_cost = {0: 4, 1: 7, 2: 1, 3: 4, 4: 9}
    graph = Graph(adjacency_list, vertics_cost)

    # brute force
    start = time.time()
    brute_force(graph)
    end = time.time()
    time_brute= end - start
    

    # greedy
    start = time.time()
    greedy(graph)
    end = time.time()
    time_greedy= end - start
    

    # genetic
    start = time.time()
    genetic(graph)
    end = time.time()
    time_genetic= end - start
    

    # simulated annealing
    start = time.time()
    simulated_annealing(graph, 10000)
    end = time.time()
    time_simulated= end - start
    
    
    #time 
    print('Brute force  - time:',time_brute)
    print('Greedy       - time:',time_greedy)
    print('Genetic      - time:',time_genetic)
    print('Simulated a. - time:',time_brute)
    
    print('------------------------------------------------------------------------------------')

    # # primer 3
    vertics_cost = {0: 3, 1: 2, 2: 5, 3: 1, 4: 4, 5: 8, 6: 2, 7: 3, 8: 2, 9: 4}
    adjacency_list = {0: [1, 2, 3], 1: [0, 3, 4], 2: [0, 5, 6, 7], 3: [0, 1, 8], 4: [
        1, 3], 5: [2, 6, 9], 6: [0, 2, 5, 9], 7: [2, 9], 8: [3], 9: [6, 7]}
    graph = Graph(adjacency_list, vertics_cost)

    # brute force
    start = time.time()
    brute_force(graph)
    end = time.time()
    time_brute= end - start
    

    # greedy
    start = time.time()
    greedy(graph)
    end = time.time()
    time_greedy= end - start
    

    # genetic
    start = time.time()
    genetic(graph)
    end = time.time()
    time_genetic= end - start
    

    # simulated annealing
    start = time.time()
    simulated_annealing(graph, 10000)
    end = time.time()
    time_simulated= end - start
    
    
    #time 
    print('Brute force  - time:',time_brute)
    print('Greedy       - time:',time_greedy)
    print('Genetic      - time:',time_genetic)
    print('Simulated a. - time:',time_brute)
    
    
    print('------------------------------------------------------------------------------------')

    # Primer 4
    vertics_cost = {0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 6, 7: 5, 8: 4, 9: 1, 10: 2, 11: 3, 12: 3, 13: 2,
                    14: 1, 15: 2, 16: 5, 17: 4, 18: 3, 19: 2, 20: 4, 21: 3, 22: 2, 23: 4, 24: 2, 25: 1, 26: 3, 27: 1, 28: 1, 29: 1, 30: 3, 31: 1}
    adjacency_list = {0: [1, 3], 1: [0, 3, 20, 11, 6, 28], 2: [9, 10, 24], 3: [0, 1, 9, 12, 4, 5], 4: [3, 19, 5], 5: [3, 4], 6: [1, 7, 8], 7: [6, 8, 14], 8: [6, 7, 9], 9: [8, 20, 3, 2, 10, 12, 30, 23, 16, 29, 15], 10: [2, 17, 9], 11: [1, 13, 18, 25, 12], 12: [11, 3, 9], 13: [18, 11], 14: [7, 15, 27], 15: [
        14, 12], 16: [22, 23, 17, 9], 17: [16, 10], 18: [19, 11, 27, 13], 19: [18, 27, 4, 31, 26], 20: [1, 9], 21: [28, 22], 22: [29, 21, 16], 23: [16, 9, 24, 30], 24: [23, 31, 2], 25: [28, 11, 29], 26: [19, 31], 27: [14, 18, 19], 28: [21, 1, 25], 29: [25, 22, 9], 30: [23, 9], 31: [19, 26, 24]}
    graph = Graph(adjacency_list, vertics_cost)

    # ULAZI U BESKONACNU PETNJU ILI TAKO NESTO (MORALA SAM DA RESTARTUJEM KOMP)
    # brute force
    #start = time.time()
    #brute_force(graph)
    #end = time.time()
    #time_brute= end - start
    

    # greedy
    start = time.time()
    greedy(graph)
    end = time.time()
    time_greedy= end - start
    

    # genetic
    start = time.time()
    genetic(graph)
    end = time.time()
    time_genetic= end - start
    

    # simulated annealing
    start = time.time()
    simulated_annealing(graph, 10000)
    end = time.time()
    time_simulated= end - start
    
    
    #time 
    #print('Brute force  - time:',time_brute)
    print('Greedy       - time:',time_greedy)
    print('Genetic      - time:',time_genetic)
    print('Simulated a. - time:',time_brute)
