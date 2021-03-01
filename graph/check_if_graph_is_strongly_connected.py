

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


# Helper Function of DFS. Might be useful
def dfs(g, source, visited):
    """
    Function to print a DFS of graph
    :param graph: The graph
    :param source: starting vertex
    :return: returns the traversal in a string
    """

    graph = copy.deepcopy(g)

    # Create a stack for DFS
    stack = []

    # Result string
    result = ""

    # Push the source
    stack.append(source)

    while stack:

        # Pop a vertex from stack
        source = stack[-1]
        stack.pop()

        if not visited[source]:
            result += str(source)
            visited[source] = True

        # Get all adjacent vertices of the popped vertex source.
        # If a adjacent has not been visited, then push it
        while graph.graph[source] is not None:
            data = graph.graph[source].vertex
            if not visited[data]:
                stack.append(data)
            graph.graph[source] = graph.graph[source].next

    return result


def is_strongly_connected(graph):
    """
    Finds if the graph is strongly connected or not
    :param graph: The graph
    :return: returns True if the graph is strongly connected, otherwise False
    """

    # Step 1: Do DFS traversal starting from the first vertex.
    result = dfs(graph, 0)

    # If DFS traversal doesn't visit all vertices, then return false
    if graph.V != len(result):
        return False

    # Step 2: Create a reversed graph
    graph2 = transpose(graph)

    # Step 3: Do DFS for reversed graph starting from the first vertex.
    # Staring Vertex must be same starting point of first DFS
    result = dfs(graph2, 0)

    # If all vertices are not visited in second DFS, then
    # return false
    if graph2.V != len(result):
        return False

    return True


# Main program to test the above code
if __name__ == "__main__":

    V = 5
    g1 = Graph(V)
    g1.add_edge(0, 1)
    g1.add_edge(1, 2)
    g1.add_edge(2, 3)
    g1.add_edge(2, 4)
    g1.add_edge(3, 0)
    g1.add_edge(4, 2)
    print("Yes" if is_strongly_connected(g1) else "No")

    g2 = Graph(V)
    g2.add_edge(0, 1)
    g2.add_edge(1, 2)
    g2.add_edge(2, 3)
    g2.add_edge(2, 4)
    print("Yes" if is_strongly_connected(g2) else "No")
