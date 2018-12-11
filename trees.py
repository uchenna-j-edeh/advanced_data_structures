
from unittest import TestCase

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insertLeft(self, nodeData):
        """
        If node has no left child, add a node to the tree
        When node has a left child however, insert a node and push the existing child downone level in the tree
        Mirror the same thing in right
        """
        if self.left == None:
            self.left = Node(nodeData)
        else:
            t = Node(nodeData)
            t.left = self.left
            self.left = t


    def insertRight(self, nodeData):
        if self.right == None:
            self.right = Node(nodeData)
        else:
            t = Node(nodeData)
            t.right = self.right
            self.right = t

    def getRight(self):
        return self.right

    def getLeft(self):
        return self.left

    def setRootValue(self, data):
        self.data = data

    def getRootValue(self):
        return self.data

def BuildSpecialTree():
    nodeA = Node('a')
    
    nodeA.insertRight('c')
    nodeA.insertLeft('b')
    nodeA.getRight().insertRight('f')
    nodeA.getRight().insertLeft('e')

    # nodeA.left = Node('d')
    nodeA.getLeft().insertRight('d')

    return nodeA

if __name__ == '__main__':
    # node = Node('a')
    # print(node.getRootValue())
    # print(node.getLeft())

    # node.insertLeft('b')
    # print(node.getLeft())
    # print(node.getLeft().getRootValue())

    # node.insertRight('c')
    # print(node.getRight())
    # print(node.getRight().getRootValue())
    # node.getRight().setRootValue('Hello Uchenna')
    # print(node.getRight().getRootValue())

    # root = BuildSpecialTree()

    ttree = BuildSpecialTree()

    # ttree.getRightChild().getRootVal()
    if ttree.getLeft().getRight().getRootValue() == 'd':
        print("Success! d is Right child of b")
    if ttree.getRight().getLeft().getRootValue() =='e':
        print("Success! e is left child of c")


    print(ttree.getRight().getRootValue())
    if ttree.getRight().getRootValue() == 'c':
        print("Success! c is Right child of a")






