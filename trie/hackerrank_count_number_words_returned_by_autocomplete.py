#!/bin/python3

import os
import sys


class TrieNode:
    def __init__(self, char):
        self.char = char
        self.counter = 0
        self.children = {}


class Trie:
    def __init__(self):
        self.root = TrieNode('')
        self.output = []

    def insert(self, word):
        node = self.root

        for char in word:
            if char in node.children:
                node = node.children[char]
                node.counter += 1
            else:
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node
                node.counter += 1


    def query(self, x):
        self.output = []
        node = self.root

        for char in x:
            if char in node.children:
                node = node.children[char]
            else:
                return 0

        return node.counter


#
# Complete the contacts function below.
#

def contacts(queries):
    t = Trie()
    res = []
    for query in queries:
        if query[0] == 'add':
            t.insert(query[1])
        else:
            res.append(t.query(query[1]))

    return res

if __name__ == '__main__':

    queries_rows = int(input())

    queries = []

    for _ in range(queries_rows):
        queries.append(input().rstrip().split())

    result = contacts(queries)

    print(result)


# For each find partial operation, print the number of contact names starting with  on a new line.
#
# Sample Input
#
# 4
# add hack
# add hackerrank
# find hac
# find hak
# Sample Output
#
# 2
# 0
# Explanation
#
# We perform the following sequence of operations:
#
# Add a contact named hack.
# Add a contact named hackerrank.
# Find and print the number of contact names beginning with hac. There are currently two contact names in the application and both of them start with hac, so we print  on a new line.
# Find and print the number of contact names beginning with hak. There are currently two contact names in the application but neither of them start with hak, so we print  on a new line.
