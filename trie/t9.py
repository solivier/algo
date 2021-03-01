"""
Implement the T9 phone autocompletion

ex: if I type 4355 it should suggest me all words that matches the assoc number (i.e : hell, hello ...)
"""

import unittest


class TrieNode:
    def __init__(self, number):
        self.number = number
        self.words = []
        self.children = {}
        self.is_end = False


class Trie:
    mapping = {'a': 2, 'b': 2, 'c': 2, 'd': 3, 'e': 3, 'f': 3, 'g': 4, 'h': 4, 'i': 4, 'j': 5, 'k': 5, 'l': 5, 'm': 6, 'n': 6, 'o': 6, 'p': 7, 'q': 7, 'r': 7, 's': 7, 't': 8, 'u': 8, 'v': 8, 'w': 9, 'x': 9, 'y': 9, 'z': 9}

    def __init__(self):
        self.root = TrieNode(0)
        self.output = []

    def insert(self, word):
        node = self.root

        for char in word:
            if self.mapping[char] in node.children:
                node = node.children[self.mapping[char]]
            else:
                new_node = TrieNode(self.mapping[char])
                node.children[self.mapping[char]] = new_node
                node = new_node
        node.words.append(word)
        node.is_end = True

    def dfs(self, node):
        if node.is_end:
            for word in node.words:
                self.output.append(word)

        for child in node.children.values():
            self.dfs(child)

    def query(self, x):
        node = self.root

        for number in x:
            if int(number) in node.children:
                node = node.children[int(number)]
            else:
                return []
        self.dfs(node)

        return self.output


class Test(unittest.TestCase):
    def setUp(self):
        self.t = Trie()
        self.t.insert("was")
        self.t.insert("word")
        self.t.insert("war")
        self.t.insert("what")
        self.t.insert("where")
        self.t.insert("hello")
        self.t.insert("hell")

    def test(self):
        self.assertEqual(self.t.query('4355'), ['hell', 'hello'])

    def test_2(self):
        self.assertEqual(self.t.query('9'), ['was', 'war', 'word', 'what', 'where'])

    def test_3(self):
        self.assertEqual(self.t.query('92'), ['was', 'war'])


if __name__ == '__main__':
    unittest.main()
