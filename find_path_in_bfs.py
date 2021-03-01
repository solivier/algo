class Graph:

    # Constructor
    def __init__(self):
        # default dictionary to store graph
        self.graph = {}

    # function to add an edge to graph
    def addEdge(self, u, v):
        if u in self.graph:
            self.graph[u].append(v)
        else:
            self.graph[u] = []
            self.graph[u].append(v)

    def BFS(self, s):
        stack = [s]
        distance = {1: -1, 2: -1, 3: -1, 4: -1, 5: -1, s: 0}
        path = {1: '', 2: '', 3: '', 4: '', 5: '', s: ''}

        while stack:
            node = stack.pop()

            if node in self.graph:
                children = self.graph[node]

                for i in children:
                    if distance[i] == -1:
                        distance[i] = distance[node] + 1
                        path[i] = path[node] + str(node) + '-'
                        stack.insert(0, i)
        return distance, path


g = Graph()
g.addEdge(1, 2)
g.addEdge(1, 5)
g.addEdge(2, 3)
g.addEdge(3, 4)

print(g.BFS(1))

