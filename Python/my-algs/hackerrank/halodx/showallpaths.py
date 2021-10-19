from collections import deque, Counter
from collections import defaultdict

class Graph:
    """
    Directed graph with adjacency list
    Count all possible strings that can be generated from an FSM
    """

    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.graph = defaultdict(list)

    def new_edge(self, node1, node2):
        self.graph[node1].append(node2)

    def solution_util(self, start_node, end_node, visited, path):

        # visit node
        visited[start_node] = True
        path.append(start_node)

        # root of recursion
        if start_node == end_node:
            print(path)
        else:
            # Recurse all children
            for i in self.graph[start_node]:
                if visited[i] == False:
                    self.solution_util(i, end_node, visited, path)

        # reset data
        path.pop()
        visited[start_node] = False

    def solution(self, start_node, end_node):

        # bootstrap data for recursive function
        visited = [False] * (self.num_nodes)
        path = []

        self.solution_util(start_node, end_node, visited, path)


#     Time: O(num_nodes^num_nodes).
#     Auxiliary space: O(num_nodes^num_nodes).

if __name__=='__main__':
    #import doctest
    #doctest.testfile('test5.txt')
    #doctest.testmod(verbose=True)

    # Create a graph given in the above diagram

