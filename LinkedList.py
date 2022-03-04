"""
A Linked List is a linear data structure where elements are not stored at contiguous memory locations.
The elements are linked using pointers. Each node has a value and a link that points to the next node.
"""


# The node class has 3 elements:
#   Data element: Value of the node
#   Next Link: The Linked List node that points to the next node
#   Prev Link: The Linked List node that points to the previous node
class Node:

    # Initializing the Node object (constructor)
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:

    # Initializing the LinkedList object (constructor)
    def __init__(self):
        self.head = None
        self.size = 0  # Initializing the size of the Linked List to 0.
        self.tail = None

    # Defining the len(<LinkedList-Obj-Name>) function for the LinkedList object
    def __len__(self):
        return self.size

    # Prints the Linked List elements from head to tail
    def display(self):
        # If Linked List is empty, there are no nodes to print.
        if self.isEmpty():
            print("Linked List empty.")
            return

        x = self.head
        while x.next != None:
            print(x.data, end=" -> ")
            x = x.next
        print(x.data)

    # Returns True if the LinkedList is empty, else returns False
    def isEmpty(self):
        # Returns true when the size of the Linked List is 0.
        return self.size == 0

    # Checks if the given value exists in the LinkedList
    def exists(self, val):
        # If the Linked List is empty, there won't be any value in it to check with.
        # So the given value does not exist in such a case.
        if self.isEmpty():
            return False

        x = self.head
        # Traverse through the Linked List until we find a node with the value given or reach the last node.
        while x.data != val and x.next != None:
            x = x.next
        if x.data == val:
            return True
        if x.next is None:
            return False

    # Adds a new Node with the given input to the start of the LinkedList
    def pushFirst(self, node):
        x = Node(node)
        # If Linked List is empty, then this value will be the only one pushed into it.
        # The Tail will also point to the pushed node.
        if self.isEmpty():
            self.tail = x
        else:
            x.next = self.head
        self.head = x
        self.size += 1  # Increasing the size of the Linked List by 1 after pushing a node.

    # Removes the Node at the start of the LinkedList and returns the value
    def popFirst(self):
        # We cannot remove anything from the Linked List if it is empty.
        if self.isEmpty():
            print("Linked List empty. Cannot remove node.")
            return

        x = self.head
        self.head = self.head.next
        self.size -= 1  # Decreasing the size of the Linked List by 1 after popping a node.
        v = x.data
        # After deleting the node, if the Linked List is empty, then the Tail also points to None.
        if self.isEmpty():
            self.tail = None
        del x  # Deleting the node object we wish to pop.

        # Returning the popped value
        return v

    # Adds a new Node at the end of the LinkedList
    def pushLast(self, node):
        x = Node(node)
        # If Linked List is empty, then this value will be the only one pushed into it.
        # The Head will also point to the pushed node.
        if self.isEmpty():
            self.head = x
        else:
            self.tail.next = x
        self.tail = x
        self.size += 1  # Increasing the size of the Linked List by 1 after pushing a node.

    # Removes the Node at the end of the LinkedList and returns the value
    def popLast(self):
        # We cannot remove anything from the Linked List if it is empty.
        if self.isEmpty():
            print("Linked List is empty. Cannot remove node.")
            return

        x = self.head
        # If the first node points to None as the next node, then it is the only node in the Linked List.
        # Which means that the Linked List will be empty after popping a node.
        # So, we can assign both Head and Tail to None in that case.
        if x.next is None:
            v = x.data
            self.head = None
            self.tail = None
        else:
            p = None
            while x.next != None:
                p = x
                x = x.next
            v = x.data
            self.tail = p
            p.next = None
        self.size -= 1  # Decreasing the size of the Linked List by 1 after popping a node.
        del x  # Deleting the node object we wish to pop.

        # Returning the popped value
        return v

    # Removes the Node with the given value in the Linked List and returns the value
    def popByVal(self, val):
        # Cannot pop a value from an empty Linked List
        if self.isEmpty():
            print("Linked List is empty.")
            return

        # Checking if a node with the given value exists or not.
        if self.exists(val):
            x = self.head
            p = None

            # Initially, x is the first node. If the value is in x,
            # then we can pop it by using the popFirst() method.
            if x.data == val:
                return self.popFirst()

            # Traverse through the Linked List until we find a node with the value given or reach the last node.
            while x.data != val and x.next != None:
                p = x
                x = x.next

            # If the next node is None, then it will be the last node,
            # which can be popped by using the popLast() method.
            if x.next is None:
                return self.popLast()
            p.next = x.next
            self.size -= 1  # Decreasing the size of the Linked List by 1 after popping a node.
            del x  # Deleting the node object we wish to pop.

            # Returning the popped value
            return val

        # This part will run if only the given value does not exist in the Linked List.
        print("Value does not exist in Linked List.")
        return


if __name__ == '__main__':
    ll = LinkedList()

    ll.display()
    ll.pushLast(1)
    ll.display()
    ll.pushLast(2)
    ll.display()
    ll.pushLast(4)
    ll.display()
    ll.pushLast(8)
    ll.display()
    ll.pushLast(16)
    ll.display()
    ll.pushFirst(3)
    ll.display()
    ll.popLast()
    ll.display()
    ll.popFirst()
    ll.display()
    ll.popByVal(0)
    ll.display()

    '''
    print("-" * 15, "Linked List Operations", "-" * 15)
    print("1. Insert at start")
    print("2. Insert at last")
    print("3. Remove at start")
    print("4. Remove at last")
    print("5. Remove by value")
    print("6. Display Linked List")
    '''

    '''
    lst = list(map(int,input("Enter space separated integers to add to Linked List:\n").split()))
    for i in lst:
        ll.pushLast(i)
    ll.display()
    '''
