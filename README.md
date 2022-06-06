# Romania_Map_Problem_Artificial_intelligence


                                                                              ##sanskar07
## Depth First Search:
Approach: The depth-first search technique is used to traverse or explore data structures such as trees and graphs. Before backtracking, the algorithm starts at the root node and explores as far as possible along each node. So the basic idea is to start at the root or any arbitrary node and mark it, then advance to the next unmarked node and repeat until there are no more unmarked nodes. Then go back and check for any more unmarked nodes to cross. Finally, print the path's nodes.
Algorithm: Create a recursive function that accepts the node's index and a visited array as input. Make the current node a visited node and print it. Call the recursive function using the index of the adjacent node after traversing all nearby and unmarked nodes.

## Depth Limited Search:
Approach: The depth-first search method encounters the unbounded tree problem, which may be solved by setting a boundary or limit on the depth of the search space. This restriction is referred to as the depth limit, and it refines and organises the DFS search technique into a limited loop. This limit is denoted by the letter l, and it gives a solution to the endless path problem that arose previously in the DFS algorithm. As a result, depth restricted search may be thought of as a more refined and expanded version of the DFS algorithm. We may state that the depth restricted search method is run within a finite set of depth called depth limit to prevent the infinite loop situation when executing the codes.
Algorithm : Let begin by locating and repairing a start node. The DFS algorithm is then used to search together with the depth. After that, simply keep checking to see if the current node is the desired node.

## Iterative-Deepening Depth First Search
Approach: The BFS and DFS have not performed well in the uninformed searching strategy in terms of finding the element in the shortest possible time and space. Only that the path will be found in exponential time and space is guaranteed by the methods. So we discovered a way that combines the space competence of DFS with the optimal solution approach of BFS approaches, and we developed a new method called iterative deepening that combines the two. The primary concept here is to use re-computation of border entities rather than stocking them up. Because DFS is used in every re-computation, it takes up less space. Consider utilising BFS in iterative deepening search as well.
Algorithm: Make an iterative deepening search out of a breadth-first search. We may do this by setting aside a DFS that will search up to a certain point. It initially searches to a pre-determined depth limit before generating a route length1. This is accomplished by using the DFS method to create routes of length 1. It then paves way for routes with depth limits of 2, 3, and beyond. It can even remove all previous calculations and recur from the beginning of the loop. As a result, if there is any solution in the tree, it will finally be located because the enumeration is done in sequence.

## Best First Search :
Approach: To hold the costs of nodes with the lowest evaluation function value, we utilise a priority queue or heap. So the implementation is a variant of BFS, with the exception that Queue is replaced with PriorityQueue.
Algorithm :Make two separate lists: OPEN and CLOSED. Begin with the first node (let's say N) and place it in the 'sorted' OPEN list.Rep the previous stages till you reach the GOAL node. If the OPEN list is empty, the loop will EXIT with the value 'False.' In the OPEN list, choose the first/top node (say N) and shift it to the CLOSED list. Take note of the parent node's information as well. If N is a GOAL node, move it to the Closed list and return 'True' to end the loop. The answer may be determined by going backwards on the trail. Expand node N to produce the 'immediate' following nodes linked to node N and add all of them to the OPEN list if N is not the GOAL node.Using an evaluation function f, reorder the nodes in the OPEN list in ascending order (n)

## A* Search 
Approach: To create an open list and a closed list, one can use any data structure, but for the greatest performance, will use a set data structure from C++ STL and a boolean hash table for the closed list.The algorithms are based on Dijkstra's algorithm. The efficiency of the open list will improve if we use a Fibonacci heap instead of a binary heap/self-balancing tree to implement it.  Also to reduce the time taken to calculate g, we will use dynamic programming.
Algorithm : 1.  Initialize the open list
2.  Initialize the closed list
    put the starting node on the open 
    list (you can leave its f at zero)

3.  while the open list is not empty
    a) find the node with the least f on 
       the open list, call it "q"

    b) pop q off the open list
  
    c) generate q's 8 successors and set their 
       parents to q
   
    d) for each successor
        i) if successor is the goal, stop search
        
        ii) else, compute both g and h for successor
          successor.g = q.g + distance between 
                              successor and q
          successor.h = distance from goal to 
          successor (This can be done using many 
          ways, we will discuss three heuristics- 
          Manhattan, Diagonal and Euclidean 
          Heuristics)
          
          successor.f = successor.g + successor.h

        iii) if a node with the same position as 
            successor is in the OPEN list which has a 
           lower f than successor, skip this successor

        iV) if a node with the same position as 
            successor  is in the CLOSED list which has
            a lower f than successor, skip this successor
            otherwise, add  the node to the open list
     end (for loop)
  
    e) push q on the closed list
    end (while loop)
