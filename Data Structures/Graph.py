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

    depth_first_search(my_graph, 'a')
