"""
File: bstnode.py
Author: Liz Matthews
"""

class BSTNode(object):
    """Represents a node for a linked binary search tree."""

    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
        self._height = 0
    
    def getHeight(self):
        return self._height
    
    def updateHeight(self):
        self._height = 0
        
        if self.left == None and self.right == None:
            return
        
        if self.left != None:
            self._height = self.left.getHeight()
        
        if self.right != None:
            self._height = max(self._height, self.right.getHeight())
        
        self._height += 1
    
    def isBalanced(self):
        """Returns True if the tree is balaned or False otherwise.
        """        
        
        return abs(self.getBalance()) <= 1

    def getBalance(self):
        """Returns the balance factor for the node."""

        leftHeight = 0
        
        if self.left != None:
            leftHeight = self.left.getHeight()
        
        rightHeight = 0
        if self.right != None:
            rightHeight = self.right.getHeight()
        
        
        return leftHeight - rightHeight
        
    
