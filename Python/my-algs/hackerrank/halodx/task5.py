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
        self.counter = 0

    def new_edge(self, node1, node2):
        self.graph[node1].append(node2)

    def solution_util(self, start_node, end_node, visited):

        # visit node
        visited[start_node] = True

        # root of recursion
        if start_node == end_node:
            self.counter += 1
        else:
            # Recurse all children
            for i in self.graph[start_node]:
                if visited[i] == False:
                    self.solution_util(i, end_node, visited)

        # reset data
        visited[start_node] = False

    def solution(self, start_node, end_node):

        # bootstrap data for recursive function
        visited = [False] * (self.num_nodes)

        self.solution_util(start_node, end_node, visited)
        print(self.counter)
        self.counter = 0


if __name__=='__main__':
    import doctest
    doctest.testfile('test5.txt')
    doctest.testmod(verbose=True)
