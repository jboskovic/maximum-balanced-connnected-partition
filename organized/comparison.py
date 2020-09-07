from graph import Graph
from genetic_algorithm import GeneticAlgorithm
from brute_force_algorithm import BruteForce
from greedy_algorithm import GreedyAlgorithm
from simulated_annealing_algorithm import SimulatedAnnealing
import time
from cached_fitness import cached
import matplotlib.pyplot as plt 
  


def brute_force(graph):
    cached.clear()
    start = time.time()
    brute_force = BruteForce(graph)
    solution = brute_force.brute_force()
    end = time.time()
    duration = end - start
    return duration


def greedy(graph):
    cached.clear()
    start = time.time()

    greedy_algorithm = GreedyAlgorithm(graph)
    solution = greedy_algorithm.greedy_algorithm()
    end = time.time()
    duration = end - start
    return duration

def genetic(graph):
    cached.clear()
    start = time.time()
    nTournament = 6
    probability = 0.05
    nPopulation = 100
    nIterations = 500
    nElite = 30

    genetic = GeneticAlgorithm(
        nPopulation, nIterations, nElite, nTournament, probability, graph)
    solution = genetic.genetic_algorithm()
    end = time.time()
    duration = end - start
    return duration

def simulated_annealing(graph, nIterations):
    cached.clear()
    start = time.time()
    simulated_annealing = SimulatedAnnealing(graph, nIterations)
    solution = simulated_annealing.simulated_annealing()
    end = time.time()
    duration = end - start
    return duration
    

def simulated_annealing_fitness(graph, nIterations):
    simulated_annealing = SimulatedAnnealing(graph, nIterations)
    solution = simulated_annealing.simulated_annealing()
    return solution.fitness

def genetic_population(graph,pop):
    nTournament = 6
    probability = 0.05
    nPopulation = pop
    nIterations = 500
    nElite = 30

    genetic = GeneticAlgorithm(
        nPopulation, nIterations, nElite, nTournament, probability, graph)
    solution = genetic.genetic_algorithm()
    return solution.fitness

def genetic_iterations(graph,ite):
    nTournament = 6
    probability = 0.05
    nPopulation = 50
    nIterations = ite
    nElite = 10

    genetic = GeneticAlgorithm(
        nPopulation, nIterations, nElite, nTournament, probability, graph)
    solution = genetic.genetic_algorithm()
    return solution.fitness

if __name__ == "__main__":
    
    # primer 1
    adjacency_list1 = {0: [1, 2, 5], 1: [0, 5, 2], 2: [
        0, 1, 3, 5], 3: [2, 4], 4: [3, 5], 5: [0, 1, 2, 4]}
    vertics_cost1 = {0: 8, 1: 4, 2: 1, 3: 6, 4: 5, 5: 4}
    graph1 = Graph(adjacency_list1, vertics_cost1)

    # brute force
    brute_time1=brute_force(graph1)

    # greedy
    greedy_time1=greedy(graph1)

    # genetic
    genetic_time1=genetic(graph1)

    # simulated annealing
    simulated_time1=simulated_annealing(graph1,3000)

    # primer 2
    adjacency_list2 = {0: [1, 2], 1: [0, 4], 2: [0, 3], 3: [2, 4], 4: [1, 3]}
    vertics_cost2 = {0: 4, 1: 7, 2: 1, 3: 4, 4: 9}
    graph2 = Graph(adjacency_list2, vertics_cost2)

    # brute force
    brute_time2=brute_force(graph2)

    # greedy
    greedy_time2=greedy(graph2)

    # genetic
    genetic_time2=genetic(graph2)

    # simulated annealing
    simulated_time2=simulated_annealing(graph2,3000)
    

    # # primer 3
    vertics_cost3 = {0: 3, 1: 2, 2: 5, 3: 1, 4: 4, 5: 8, 6: 2, 7: 3, 8: 2, 9: 4}
    adjacency_list3 = {0: [1, 2, 3], 1: [0, 3, 4], 2: [0, 5, 6, 7], 3: [0, 1, 8], 4: [
        1, 3], 5: [2, 6, 9], 6: [0, 2, 5, 9], 7: [2, 9], 8: [3], 9: [6, 7]}
    graph3 = Graph(adjacency_list3, vertics_cost3)
    
    # brute force
    brute_time3=brute_force(graph3)

    # greedy
    greedy_time3=greedy(graph3)

    # genetic
    genetic_time3=genetic(graph3)

    # simulated annealing
    simulated_time3=simulated_annealing(graph3,3000)
    
    # Primer 4
    vertics_cost4 = {0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 6, 7: 5, 8: 4, 9: 1, 10: 2, 11: 3, 12: 3, 13: 2,
                    14: 1, 15: 2, 16: 5, 17: 4, 18: 3, 19: 2, 20: 4, 21: 3, 22: 2, 23: 4, 24: 2, 25: 1, 26: 3, 27: 1, 28: 1, 29: 1, 30: 3, 31: 1}
    adjacency_list4= {0: [1, 3], 1: [0, 3, 20, 11, 6, 28], 2: [9, 10, 24], 3: [0, 1, 9, 12, 4, 5], 4: [3, 19, 5], 5: [3, 4], 6: [1, 7, 8], 7: [6, 8, 14], 8: [6, 7, 9], 9: [8, 20, 3, 2, 10, 12, 30, 23, 16, 29, 15], 10: [2, 17, 9], 11: [1, 13, 18, 25, 12], 12: [11, 3, 9], 13: [18, 11], 14: [7, 15, 27], 15: [
        14, 12], 16: [22, 23, 17, 9], 17: [16, 10], 18: [19, 11, 27, 13], 19: [18, 27, 4, 31, 26], 20: [1, 9], 21: [28, 22], 22: [29, 21, 16], 23: [16, 9, 24, 30], 24: [23, 31, 2], 25: [28, 11, 29], 26: [19, 31], 27: [14, 18, 19], 28: [21, 1, 25], 29: [25, 22, 9], 30: [23, 9], 31: [19, 26, 24]}
    graph4 = Graph(adjacency_list4, vertics_cost4)

    # greedy
    greedy_time4=greedy(graph4)

    # genetic
    genetic_time4=genetic(graph4)

    # simulated annealing
    simulated_time4=simulated_annealing(graph4,3000)
    


    
    #simulirano kaljenje (poredjenje rezlutata sa brojem iteracija) (primer 4)
    simulated10000=simulated_annealing_fitness(graph4,10000)
    simulated5000=simulated_annealing_fitness(graph4,5000)
    simulated3000=simulated_annealing_fitness(graph4,3000)
    simulated2000=simulated_annealing_fitness(graph4,2000)
    simulated1000=simulated_annealing_fitness(graph4,1000)
    simulated500=simulated_annealing_fitness(graph4,500)
    simulated400=simulated_annealing_fitness(graph4,400)
    simulated300=simulated_annealing_fitness(graph4,300)
    simulated200=simulated_annealing_fitness(graph4,200)
    simulated100=simulated_annealing_fitness(graph4,100)
    
    y = [simulated5000,simulated3000,simulated2000, simulated1000, simulated500, simulated400, simulated300, simulated200, simulated100] 
    x = [5000,3000,2000,1000,500,400,300,200,100] 
    
    plt.plot(x, y) 
  
    plt.xlabel('iterations') 
    plt.ylabel('fitness') 
    plt.title('') 
    
    plt.show() 
    
    #genetski alogritam (poredjenje velicine populacije sa rezultatom) (primer 3)
    genetic30=genetic_population(graph3,30)
    genetic40=genetic_population(graph3,40)
    genetic50=genetic_population(graph3,50)
    genetic60=genetic_population(graph3,60)
    genetic70=genetic_population(graph3,70)
    genetic80=genetic_population(graph3,80)
    genetic90=genetic_population(graph3,90)
    genetic100=genetic_population(graph3,100)
    genetic110=genetic_population(graph3,110)
    
    x1=[30,40,50,60,70,80,90,100,110]
    y1=[genetic30,genetic40,genetic50,genetic60,genetic70,genetic80,genetic90,genetic100,genetic110]
    
    plt.plot(x1,y1)
    
    plt.xlabel('population')
    plt.ylabel('fitness')
    plt.title('Poredjenje velicine sa rezultatom')
    
    plt.show()
    
    #genetski algoritam (poredjenje broj iteracija sa rezultatom, za broj populaija=50) (primer3)
    
    genetic_100=genetic_iterations(graph3, 100)
    genetic_200=genetic_iterations(graph3, 200)
    genetic_300=genetic_iterations(graph3, 300)
    genetic_400=genetic_iterations(graph3, 400)
    genetic_500=genetic_iterations(graph3, 500)
    genetic_600=genetic_iterations(graph3, 600)
    genetic_700=genetic_iterations(graph3, 700)
    genetic_800=genetic_iterations(graph3, 800)
    genetic_900=genetic_iterations(graph3, 900)
    genetic_1000=genetic_iterations(graph3, 1000)
    
    x2=[100,200,300,400,500,600,700,800,900,1000]
    y2=[genetic_100,genetic_200,genetic_300,genetic_400,genetic_500,genetic_600,genetic_700,genetic_800,genetic_900,genetic_1000]
    
    plt.plot(x2,y2)
    
    plt.xlabel('iterations')
    plt.ylabel('fitness')
    plt.title('Poredjenje iteracija sa rezultatom')
    
    plt.show()
    
    #vreme (primer 3)

    left = [1, 2, 3, 4] 
    height = [brute_time3,greedy_time3,genetic_time3,simulated_time3] 
    tick_label = ['brute', 'greedy', 'genetic', 'sa'] 
  
    plt.bar(left, height, tick_label = tick_label, 
        width = 0.8, color = ['red', 'green','blue','orange']) 

    plt.xlabel('algorithm') 
    plt.ylabel('time - secunds') 
    plt.title('') 
  
    plt.show() 
    
     #vreme (primer 4)
    
    left = [1, 2, 3] 
    height = [greedy_time4, genetic_time4, simulated_time4] 
    tick_label = ['greedy', 'genetic', 'sa'] 
  
    plt.bar(left, height, tick_label = tick_label, 
        width = 0.8, color = [ 'green','blue','orange']) 

    plt.xlabel('algorithm') 
    plt.ylabel('time - secunds') 
    plt.title('') 
  
    plt.show() 
