class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
        self.path = []


class Graph:
    def bfs(self, root):
        queue = [root]

        while len(queue) > 0:
            n = len(queue)

            for i in range(n):
                node = queue.pop()
                if i == 0 or i == n - 1:
                    print(node.value, end=" ")

                if node.left:
                    queue.insert(0, node.left)
                if node.right:
                    queue.insert(0, node.right)



tree = Node(15)
tree.left = Node(10)
tree.left.left = Node(8)
tree.left.right = Node(12)
tree.right = Node(20)
tree.right.right = Node(25)
tree.right.left = Node(16)

g = Graph()
g.bfs(tree)
