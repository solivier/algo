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


def number_of_nodes(my_graph, level):
    """
    Calculates the number of nodes at given level
    :param graph: The graph
    :return: Total number of nodes at given level
    """

    source = 0

    # Mark all the vertices as not visited
    visited = [0] * (len(my_graph.graph))

    # Create a queue
    queue = []

    # Result string
    result = ""

    # Mark the source node as
    # visited and enqueue it
    queue.append(source)
    visited[source] = 1

    while queue:

        # Dequeue a vertex from queue
        source = queue.pop(0)

        # Get all adjacent vertices of the
        # dequeued vertex source. If a adjacent
        # has not been visited, then mark it
        # visited and enqueue it

        while my_graph.graph[source] is not None:
            data = my_graph.graph[source].vertex
            if visited[data] == 0:
                queue.append(data)
                visited[data] = visited[source] + 1
            my_graph.graph[source] = my_graph.graph[source].next

    # Counting number of nodes at given level
    result = 0
    for i in range(len(my_graph.graph)):
        if visited[i] == level:
            result += 1
    return result


# Main to test above function
if __name__ == "__main__":

    V = 5
    g = Graph(V)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)

    print(number_of_nodes(g, 2))
