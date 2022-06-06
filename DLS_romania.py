from queue import PriorityQueue
from collections import defaultdict



src = "Arad"
target = "Bucharest"
maxDepth = 3

global visited

visited = set()
class Graph:
    def __init__(self):
        self.edges = {"Arad": ["Zerind", "Timisoara", "Sibiu"], "Zerind": ["Oradea"], "Oradea": ["Sibiu"],
                      "Timisoara": ["Lugoj"], "Lugoj": ["Mehadia"], "Mehadia": ["Dobreta"], "Dobreta": ["Craiova"],
                      "Sibiu": ["Fagaras", "RimnicuVilcea"], "Craiova": ["RimnicuVilcea", "Pitesti"],
                      "RimnicuVilcea": ["Craiova", "Pitesti"], "Fagaras": ["Bucharest"], "Pitesti": ["Bucharest"],
                      "Bucharest": ["Giurgiu", "Urziceni"], "Urziceni": ["Hirsova", "Vaslui"], "Hirsova": ["Eforie"],
                      "Vaslui": ["Lasi"], "Lasi": ["Neamt"]}
        self.weights = {"AradZerind": 75, "ZerindOradea": 71, "AradTimisoara": 118, "TimisoaraLugoj": 111,
                        "LugojMehadia": 70, "MehadiaDobreta": 75, "AradSibiu": 140, "OradeaSibiu": 151,
                        "DobretaCraiova": 120, "CraiovaRimnicuVilcea": 146, "CraiovaPitesti": 138, "SibiuFagaras": 99,
                        "SibiuRimnicuVilcea": 80, "RimnicuVilceaPitesti": 97, "RimnicuVilceaCraiova": 146,
                        "FagarasBucharest": 211, "PitestiBucharest": 101, "BucharestGiurgiu": 90,
                        "BucharestUrziceni": 85, "UrziceniHirsova": 98, "HirsovaEforie": 86, "UrziceniVaslui": 142,
                        "VasluiLasi": 92, "LasiNeamt": 87}
        self.heuristic_values = {"Arad" : 366,"Bucharest": 0,"Craiova": 160,"Dobreta" : 242,"Eforie": 161,"Fagaras": 176,
                          "Giurgiu": 77,"Hirsowa":151,"Lasi": 226,"Lugoj": 244,"Mehadia": 241,"Neamt": 234,"Oradea": 380,
                          "Pitesti": 100,"Rimnicu Vilcea": 193,"Sibiu": 253,"Timisoara": 329,"Urziceni": 80,"Vaslui": 199,
                          "Zerind": 374}

    def neighbours(self, node):
        return self.edges[node]

    def get_cost(self, from_node, to_node):
        return self.weights[(from_node + to_node)]

    def DFSUtil(self, node, visited):
        # Mark the current node as visited and print it
        visited.add(node)
        print(node, end="\n")

        # recur for all the vertices adjacent to this vertex
        for neighbour in self.edges:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)

    def DFS(self):
        # create a set to store all visited vertices
        # call the recursive helper function to print DFS traversal starting from all
        # vertices one by one
        for vertex in self.edges:
            if vertex not in visited:
                self.DFSUtil(vertex, visited)

    def DLS(self, src, target, maxDepth):

        if src == target:
            return True
        if maxDepth <= 0:
            return False

        # Recur for all the vertices adjacent to this vertex
        for i in self.edges:
            visited.add(i)
            print(i, end="\n")
            if self.DLS(i, target, maxDepth - 1):
                return True
        return False

graph = Graph()
graph.DLS("Arad","Bucharest",3)
