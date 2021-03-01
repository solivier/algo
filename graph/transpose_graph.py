class AdjNode:
    """
    A class to represent the adjacency list of the node
    """

    def __init__(self, data):
        """
        Constructor
        :param data : vertex
        """
        self.vertex = data
        self.next = None


class Graph:
    """
    Graph Class ADT
    """

    def __init__(self, vertices):
        """
        Constructor
        :param vertices : Total vertices in a graph
        """
        self.V = vertices
        self.graph = [None] * self.V

    def add_edge(self, source, destination):
        """
        add edge
        :param source: Source Vertex
        :param destination: Destination Vertex
        """

        # Adding the node to the source node
        node = AdjNode(destination)
        node.next = self.graph[source]
        self.graph[source] = node

        # Adding the source node to the destination if undirected graph

        # Intentionally commented the lines
        # node = AdjNode(source)
        # node.next = self.graph[destination]
        # self.graph[destination] = node

    def print_graph(self):
        """
        A function to print a graph
        """
        for i in range(self.V):
            print("Adjacency list of vertex {}\n head".format(i), end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print(" \n")


def transpose(my_graph):
    """
    Transpose the given graph
    :param graph: The graph
    :return: a new transposed graph of the given graph
    """

    new_graph = Graph(my_graph.V)  # Creating a new graph

    for source in range(my_graph.V):

        while my_graph.graph[source] is not None:

            destination = my_graph.graph[source].vertex
            # Now the source is destination and vice versa
            new_graph.add_edge(destination, source)
            my_graph.graph[source] = my_graph.graph[source].next

    return new_graph


# Main program to test the above function
if __name__ == "__main__":

    V = 5
    g = Graph(V)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)

    new_g = transpose(g)
    new_g.print_graph()
