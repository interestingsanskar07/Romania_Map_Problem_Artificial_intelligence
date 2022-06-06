from queue import PriorityQueue
from collections import defaultdict

src = "Arad"
target = "Bucharest"
maxDepth = 3
global visited
visited = set()

global path
path = []

global parent
parent = set()
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

    def neighbours(self, node):
        return self.edges[node]

    def get_cost(self, from_node, to_node):
        return self.weights[(from_node + to_node)]

    def get_path(self,target):
            g = target
            while g is not None:
                path.append(g)

            path.reverse()
            # printing the path to our destination city
            print(path)

    def DLS(self, src, target, maxDepth):
        if src == target:
            return True
        if maxDepth <= 0:
            return False

        # Recur for all the vertices adjacent to this vertex
        for i in self.edges:
            visited.add(i)
            parent.add(i)
            print(i, end="\n")
            if self.DLS(i, target, maxDepth - 1):
                # total_cost = self.get_cost(i,target)
                self.get_path(target)
                return True
        return False

    # IDDFS to search if target is reachable from v.
    # It uses recursive DLS()
    def IDDFS(self, src, target, maxDepth):

        # Repeatedly depth-limit search till the
        # maximum depth
        for i in range(maxDepth):
            if self.DLS(src, target, i):
                # total_cost = self.get_cost(i,target)
                self.get_path(target)
                return True
        return False



graph = Graph()
if graph.IDDFS(src, target, maxDepth):
    print("\nTarget is reachable from source " +
         "within max depth")
else :
    print("\nTarget is NOT reachable from source " +
          "within max depth")
