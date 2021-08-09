"""
File: testbalance.py
Tester program for rebalancing a BST.
"""

from linkedBst import LinkedBST
import random

def main():
    tree = LinkedBST()
    print("Adding D B A C F E G")
    tree.add("D")
    tree.add("B")
    tree.add("A")
    tree.add("C")
    tree.add("F")
    tree.add("E")
    tree.add("G")

    print("\nString:\n" + str(tree))    
    print("Left height, right height:", tree._root.left.getHeight(), tree._root.right.getHeight())
    print("Length:", len(tree))
    print("Height:", tree.height())
    print("Balanced:", tree.isBalanced())
    
    tree = LinkedBST(range(1, 16))
    print("\nAdded 1..15:\n" + str(tree))    
    print("Left height, right height:", tree._root.left.getHeight(), tree._root.right.getHeight())
    print("Length:", len(tree))
    print("Height:", tree.height())
    print("Balanced:", tree.isBalanced())
    
    lyst = list(range(1, 16))
    import random
    random.shuffle(lyst)
    tree = LinkedBST(lyst)
    print("\nAdded ", lyst, "\n" + str(tree))    
    print("Left height, right height:", tree._root.left.getHeight(), tree._root.right.getHeight())
    print("Length:", len(tree))
    print("Height:", tree.height())
    print("Balanced:", tree.isBalanced())
    
    print("Testing remove balancing\n")
    lyst = list(range(1, 100))
    random.shuffle(lyst)
    tree = LinkedBST(lyst)
    lyst.sort()
    for i in range(50):
        tree.remove(lyst[i])
        if not tree.isBalanced():
            print(tree._root.left.getHeight(), tree._root.right.getHeight())
            print(tree._root.isBalanced())
            print("unbalanced tree!")
            print(tree)
            input()
    
    print("\nAdded 100, removed 50\n" + str(tree))
    print("Left height, right height:", tree._root.left.getHeight(), tree._root.right.getHeight())
    print("Length:", len(tree))
    print("Height:", tree.height())
    print("Balanced:", tree.isBalanced())
    for i in lyst[0:50]:
        if i in tree:
            print("item i should not be in tree:", i)
    for i in lyst[50:100]:
        if i not in tree:
            print("item i should be in tree:", i)

    
if __name__ == "__main__":
    main()




