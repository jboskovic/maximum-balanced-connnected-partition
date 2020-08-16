# graf je predstavljen kao mapa
class Graph:
    # ajdacency_list - mapira cvorove u listu cvorova sa kojima je povezan
    # cost - niz cena cvorova
    # V - broj cvorova
    def __init__(self, adjacency_list, cost):
        self.cost = cost
        self.adj = adjacency_list
        self.V = len(self.adj)

    # DFS obilazak grafa
    # povratna vrednost - lista cvorova
    def DFSUtil(self, temp, node, visited):
        visited[node] = True
        temp.append(node)
        for v in self.adj.get(node):
            if visited[v] == False:
                temp = self.DFSUtil(temp, v, visited)
        return temp

    # povratna vreednost - lista komponenti
    def connectedComponents(self):
        visited = {}
        cc = []
        for k in self.adj.keys():
            visited[k] = False
        for (k, v) in self.adj.items():
            if visited[k] == False:
                temp = []
                cc.append(self.DFSUtil(temp, k, visited))
        return cc
    # funkcija vraca novi graf koji ne sadrzi cvor node (kao ni njegove grane)
    # izbacujemo cvor i sve grane koje polaze iz tog cvora

    def remove_node(self, node):
        newAdj = {}
        for (k, v) in self.adj.items():
            if k == node:
                continue
            else:
                newAdj[k] = []
                for i in range(len(v)):
                    if v[i] != node:
                        newAdj[k].append(v[i])

        return Graph(newAdj, self.cost)

    # povratna vrednost funkcije je najveca cena cvora iz datog grafa
    def maxCost(self):
        maks = -float('inf')
        # prolazimo kroz sve cvovore koji se nalaze u grafu
        for (k, v) in self.adj.items():
            if self.cost[k] > maks:
                maks = self.cost[k]
        return maks

    def connectedGraph(self):
        return len(self.connectedComponents()) == 1

    def getCostSum(self):
        suma = 0
        for (k, v) in self.cost.items():
            suma += v
        return suma
