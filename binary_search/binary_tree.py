import unittest


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def find_value(self, lkpval):
        if lkpval < self.data:
            if self.left is None:
                return str(lkpval) + " Not Found"
            return self.left.find_value(lkpval)
        elif lkpval > self.data:
            if self.right is None:
                return str(lkpval) + " Not Found"
            return self.right.find_value(lkpval)
        else:
            return str(self.data) + ' is found'

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data),
        if self.right:
            self.right.print_tree()


class TestBinaryTree(unittest.TestCase):
    def test(self):
        root = Node(1)
        root.insert(14)
        root.insert(6)
        root.insert(3)
        self.assertEqual("3 is found", root.find_value(3))


if __name__ == '__main__':
    unittest.main()
