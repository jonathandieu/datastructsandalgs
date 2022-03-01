from lib2to3.pgen2.token import NEWLINE
from operator import ne
from os import sep


class Graph:
    def __init__(self) -> None:
        self.adjacency_list = {}

    def print_adj_list(self):
        print(self.adjacency_list)
        for vertex, edges in self.adjacency_list.items():
            print(f"vertex: {vertex} has edge(s) to: {self.adjacency_list[vertex]}")
            if len(edges) == 0:
                print("This vertex has no edges.")



    def add_vertex(self, vertex) -> None:
        """
        Adds new vertex to the graph
        """
        # Only add the vertex if it doesn't already exist in the graph
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []
        else:
            print("That vertex already exists.")

    def add_edge(self, vertex1, vertex2, edge_weight=0):
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            temp = [vertex2, edge_weight] # Python only lets us append one thing at a time, so we need to append the whole list
            self.adjacency_list[vertex1].append(temp)


def iterative_depth_first_search(graph: Graph, source_node) -> None:
    stack = [source_node] # Initialize stack with just the source_node in it

    # As long as the stack has something in it, loop through and traverse.
    while stack:
        current = stack.pop() # Assign a current node to process
        print(current)

        for neighbor_node in graph.adjacency_list[current]:
            stack.append(neighbor_node)

def recursive_depth_first_search(graph: Graph, source_node) -> None:
    # Consider the source_node as the current node
    print(source_node)
    for neighbor_node in graph.adjacency_list[source_node]:
        recursive_depth_first_search(graph, neighbor_node)

# Driver Code
if __name__ == "__main__":
    my_graph = Graph()
    my_graph.adjacency_list = {
        "a": ['c', 'b'],
        "b": ['d'],
        "c": ['e'],
        "d": ['f'],
        "e": [],
        "f": []
    }

    print("Iterative DFS: ")
    iterative_depth_first_search(my_graph, 'a')

    print("Recursive DFS: ")
    recursive_depth_first_search(my_graph, 'a')

    print("Before adding vertex: ")
    my_graph.print_adj_list()

    my_graph.add_vertex("new_node")
    print("After adding vertex: ")
    my_graph.print_adj_list()

    my_graph.add_edge("new_node", "a")
    print("After adding edge between 'new_node' and 'a':")
    my_graph.print_adj_list()


    my_graph.add_edge("new_node", "b", 6)
    print("After adding edge between 'new_node' and 'b':")
    my_graph.print_adj_list()
