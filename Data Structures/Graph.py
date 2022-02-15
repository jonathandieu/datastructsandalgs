class Graph:
    def __init__(self) -> None:
        self.adjacency_list = {}

    def print_adj_list(self):
        print(self.adjacency_list.keys())


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