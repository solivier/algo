# Python program to find closest
# value in Binary search Tree
# This is in O(n) time and O(1) space
from statistics import median

_MIN = -2147483648
_MAX = 2147483648


# Helper function that allocates
# a new node with the given data
# and None left and right poers.
class newNode:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


""" A utility function to insert a new node with 
given key in BST """


def insert(node, key):
    """ If the tree is empty, return a new node """
    if (node == None):
        return newNode(key)

    """ Otherwise, recur down the tree """
    if (key < node.data):
        node.left = insert(node.left, key)
    elif (key > node.data):
        node.right = insert(node.right, key)

    """ return the (unchanged) node pointer """
    return node


""" Function to count nodes in 
	a binary search tree using 
	Morris Inorder traversal"""


def counNodes(root):
    # Initialise count of nodes as 0
    count = 0

    if (root == None):
        return count

    current = root
    while (current != None):

        if (current.left == None):

            # Count node if its left is None
            count += 1

            # Move to its right
            current = current.right

        else:
            """ Find the inorder predecessor of current """
            pre = current.left

            while (pre.right != None and
                   pre.right != current):
                pre = pre.right

            """ Make current as right child of its 
            inorder predecessor """
            if (pre.right == None):

                pre.right = current
                current = current.left
            else:

                pre.right = None

                # Increment count if the current
                # node is to be visited
                count += 1
                current = current.right

    return count


""" Function to find median in 
	O(n) time and O(1) space 
	using Morris Inorder traversal"""


def findMedian(root):
    if (root == None):
        return 0
    count = counNodes(root)
    currCount = 0
    current = root

    while (current != None):

        if (current.left == None):

            # count current node
            currCount += 1

            # check if current node is the median
            # Odd case
            if (count % 2 != 0 and
                    currCount == (count + 1) // 2):
                return prev.data

            # Even case
            elif (count % 2 == 0 and
                  currCount == (count // 2) + 1):
                return (prev.data + current.data) // 2

            # Update prev for even no. of nodes
            prev = current

            # Move to the right
            current = current.right

        else:

            """ Find the inorder predecessor of current """
            pre = current.left
            while (pre.right != None and
                   pre.right != current):
                pre = pre.right

            """ Make current as right child 
                of its inorder predecessor """
            if (pre.right == None):

                pre.right = current
                current = current.left
            else:

                pre.right = None

                prev = pre

                # Count current node
                currCount += 1

                # Check if the current node is the median
                if (count % 2 != 0 and
                        currCount == (count + 1) // 2):
                    return current.data

                elif (count % 2 == 0 and
                      currCount == (count // 2) + 1):
                    return (prev.data + current.data) // 2

                # update prev node for the case of even
                # no. of nodes
                prev = current
                current = current.right

            # Driver Code


if __name__ == '__main__':
    """ Constructed binary tree is 
         50 
        /  \ 
       30   70 
      / \   /  \ 
     20 40  60 80
     
     """

    root = newNode(1)
    insert(root, 3)
    insert(root, 5)
    insert(root, 5)
    insert(root, 6)
    insert(root, 7)
    insert(root, 7)
    insert(root, 7)
    insert(root, 8)
    print("Median of BST is ", findMedian(root))
    print(median([1, 3, 5, 5, 6, 7, 7, 7, 8]))

# 50, 30, 20, 40, 70, 60, 80
# 20, 30, 40, 50, 60, 70, 80
# 1, 3, 5, 5, 6, 7, 7, 7, 8

# This code is contributed
# Shubham Singh(SHUBHAMSINGH10)
