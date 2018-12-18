"""
Binary trees
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


    def insert_left(self, child):
        if self.left is None:
            self.left = child
        else:
            child.left = self.left # push current node down one level
            self.left = child
        
    def insert_right(self, child):
        if self.right is None:
            self.right = child
        else:
            child.right = self.right # push current node down one level
            self.right = child

