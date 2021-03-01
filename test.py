class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)
        self.visited = []

    def dfs(self, start):
        if start:
            self.visited.append(start.value)
            self.dfs(start.left)
            self.dfs(start.right)

    def dfs2(self, start):
        if start:
            self.dfs2(start.left)
            self.visited.append(start.value)
            self.dfs2(start.right)

    def bfs(self, start: Node):

        queue = [start]

        while len(queue) > 0:
            self.visited.append(queue[-1].value)
            node = queue.pop()

            if node.left:
                queue.insert(0, node.left)
            if node.right:
                queue.insert(0, node.right)

    def bfs2(self, start: Node):

        queue = [start]

        while len(queue) > 0:
            self.visited.append(queue[-1].value)
            node = queue.pop()

            if node.left:
                queue.insert(0, node.left)
            if node.right:
                queue.insert(0, node.right)


tree = BinaryTree(12)
tree.root.left = Node(54)
tree.root.left.right = Node(56)
tree.root.left.left = Node(77)
tree.root.left.right.left = Node(982)

tree.root.right = Node(3)
tree.root.right.right = Node(67)
tree.root.right.left = Node(78)
tree.root.right.right.left = Node(34)

tree.bfs2(tree.root)
#print(tree.visited)





