"""
A Binary Tree is a tree whose elements have 0 to 2 children. They are named left child and right child.
Each child itself is another element and can have 0 to 2 children.
"""


# Importing the required class from the Queue.py file
from Queue import Queue


# The node class has 3 elements:
#   Data element: Value of the node
#   Left Link: Points to the left child
#   Right Link: Points to the right child
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:

    # Initializing the BinaryTree object (constructor)
    def __init__(self):
        self.root = None
        self.count = 0  # Initializing the size of the Binary Tree to 0.

    # Defining the len(<BinaryTree-Obj-Name>) function for the BinaryTree object
    def __len__(self):
        return self.count

    # Prints the elements in the order: Left child, Parent, Right child
    def inorder(self, root):
        if root != None:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

    # Prints the elements in the order: Parent, Left child, Right child
    def preorder(self, root):
        if root != None:
            print(root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    # Prints the elements in the order: Left child, Right child, Parent
    def postorder(self, root):
        if root != None:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=" ")

    # Prints the elements of each level
    def levelorder(self):
        q = Queue()
        t = self.root
        print(t.data, end=" ")
        q.enqueue(t)

        while len(q) > 0:
            t = q.dequeue()

            if t.left != None:
                print(t.left.data, end=" ")
                q.enqueue(t.left)
            if t.right != None:
                print(t.right.data, end=" ")
                q.enqueue(t.right)

    # Inserts a new node with the given value into the Binary Tree
    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
            return
        q = Queue()
        q.enqueue(self.root)

        while len(q) > 0:
            t = q.dequeue()

            if t.left is None:
                t.left = Node(val)
                break
            else:
                q.enqueue(t.left)

            if t.right is None:
                t.right = Node(val)
                break
            else:
                q.enqueue(t.right)
        self.count += 1  # Increasing the size of the Binary Tree by 1 after inserting a node.

    # Prints the height of the Binary Tree
    def height(self, t):
        if t != None:
            l = self.height(t.left)
            r = self.height(t.right)

            if l > r:
                return l + 1
            return r + 1
        return 0

    # Removes the node with the given value from the Binary Tree
    def delete(self, val):
        # Cannot delete a value if the Tree is empty.
        if self.root is None:
            print("Tree is empty. Cannot perform operation.")
            return

        # If the root has only one element
        if self.root.left is None and self.root.right is None:
            # Delete the element if the one element is the value given
            if self.root.data == val:
                self.root = None
                self.count -= 1
                return
            print("Value does not exist in the Binary Tree.")
            return
        key = None
        q = Queue()
        q.enqueue(self.root)
        t = None

        while len(q) > 0:
            t = q.dequeue()
            if t.data == val:
                key = t
            if t.left != None:
                q.enqueue(t.left)
            if t.right != None:
                q.enqueue(t.right)

        if key is None:
            print("Value does not exist in the Binary Tree.")
            return
        x = t.data
        va = t
        t = None
        q2 = Queue()
        q.enqueue(self.root)
        while len(q) > 0:
            t = q.dequeue()
            if t is va:
                t = None
                break
            if t.right != None:
                if t.right is va:
                    t.right = None
                    break
                q.enqueue(t.right)
            if t.left != None:
                if t.left is va:
                    t.left = None
                    break
                q.enqueue(t.left)
        self.count -= 1  # Decreasing the size of the Binary Tree by 1 after deleting a node.
        key.data = x



if __name__ == '__main__':
    bt = BinaryTree()
    #node = None
    bt.insert(1)
    bt.insert(2)
    bt.preorder(bt.root)
    print()
    bt.insert(3)
    bt.insert(4)
    bt.preorder(bt.root)
    print()
    bt.insert(5)
    bt.insert(6)
    bt.preorder(bt.root)
    print()
    bt.insert(7)
    bt.preorder(bt.root)
    print()
    bt.delete(3)
    bt.preorder(bt.root)
    print()
    print("Height:",bt.height(bt.root))
    print("Level Order:")
    bt.levelorder()
