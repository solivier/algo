class Node:
    def __init__(self, value):
        self.value = value
        self.children = None


class Tree:
    def __init__(self):
        self.root = Node("")

    def insert(self, value):
        node = self.root
        for char in value:
            if node.children is not None and char == node.children.value:
                continue
            node.children = Node(char)
            node = node.children


t = Tree()
t.insert("work")
