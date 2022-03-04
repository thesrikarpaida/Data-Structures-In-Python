"""
A Doubly Linked List is a Linked List that has 2 links where one of them points to the next node while the
other one points to the previous node.
"""


# Importing the required classes from the LinkedList.py file
from LinkedList import LinkedList, Node


# This class inherits methods from the parent class LinkedList
# and overrides some of them that require changes.
class DoublyLinkedList(LinkedList):

    # Prints the Linked List elements from head to tail
    def display(self):
        # If Linked List is empty, there are no nodes to print.
        if self.isEmpty():
            print("Linked List empty.")
            return

        x = self.head
        while x.next != None:
            print(x.data, end=" <=> ")
            x = x.next
        print(x.data)

    # Adds a new Node with the given input to the start of the LinkedList
    def pushFirst(self, node):
        x = Node(node)
        # If Linked List is empty, then this value will be the only one pushed into it.
        # The Tail will also point to the pushed node.
        if self.isEmpty():
            self.tail = x
        else:
            x.next = self.head
            self.head.prev = x
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
        else:
            self.head.prev = None
        del x  # Deleting the node object we wish to pop.

        # Returning the popped value
        return v

    # Adds a new Node at the end of the LinkedList
    def pushLast(self, node):
        x = Node(node)
        if self.isEmpty():
            self.head = x
        else:
            self.tail.next = x
            x.prev = self.tail
        self.tail = x
        self.size += 1  # Increasing the size of the Linked List by 1 after pushing a node.

    # Removes the Node at the end of the LinkedList
    def popLast(self):
        # We cannot remove anything from the Linked List if it is empty.
        if self.isEmpty():
            print("Linked List is empty. Cannot remove node.")
            return

        x = self.tail
        self.tail = self.tail.prev
        self.size -= 1  # Decreasing the size of the Linked List by 1 after popping a node.

        # If the Linked List is empty after decreasing the size by 1,
        # it means that there was only 1 node left.
        # So, we can point the Head to None in this case.
        if self.isEmpty():
            self.head = None
        else:
            self.tail.next = None
        v = x.data
        del x  # Deleting the node object we wish to pop.

        # Returning the popped value
        return v

    # Removes the Node with the given value in the Linked List
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
            x.next.prev = p
            self.size -= 1  # Decreasing the size of the Linked List by 1 after popping a node.
            del x  # Deleting the node object we wish to pop.

            # Returning the popped value
            return val

        # This part will run if only the given value does not exist in the Linked List.
        print("Value does not exist in Linked List.")
        return


if __name__ == '__main__':
    ll = DoublyLinkedList()

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
