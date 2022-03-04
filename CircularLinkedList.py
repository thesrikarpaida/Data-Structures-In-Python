"""
A Circular Linked List is a Linked List where the last node (tail) points to the first node (head).
"""


# Importing the required classes from the LinkedList.py file
from LinkedList import Node, LinkedList


# This class inherits functions from the parent class LinkedList
# and overrides some of them that require changes.
class CircularLinkedList(LinkedList):

    # Prints the Linked List elements from head to tail
    def display(self):
        # If Linked List is empty, there are no nodes to print.
        if self.head is None:
            print("Linked List empty.")
            return

        x = self.head
        while x.next != self.head:
            print(x.data, end=" -> ")
            x = x.next
        print(x.data)

    # Checks if the given value exists in the LinkedList
    def exists(self, val):
        # If the Linked List is empty, there won't be any value in it to check with.
        # So the given value does not exist in such a case.
        if self.isEmpty():
            return False

        x = self.head
        # Traverse through the Linked List until we find a node with the value given or reach the last node.
        while x.data != val and x.next != self.head:
            x = x.next
        if x.data == val:
            return True
        if x.next is self.head:
            return False

    def pushFirst(self, node):
        super().pushFirst(node)
        self.tail.next = self.head  # Assigning the next of the Tail to the Head

    # Adds a new Node at the end of the LinkedList
    def pushLast(self, node):
        x = Node(node)
        # If Linked List is empty, then this value will be the only one pushed into it.
        # The Head will also point to the pushed node.
        if self.isEmpty():
            self.head = x
        else:
            x.next = self.tail.next
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
        p = None
        # If the first node points to Head as the next node, then it is the only node in the Linked List.
        # Which means that the Linked List will be empty after popping a node.
        # So, we can assign both Head and Tail to None in that case.
        if x.next == self.head:
            return self.popFirst()
        while x.next != self.head:
            p = x
            x = x.next
        v = x.data
        p.next = self.head
        self.size -= 1  # Decreasing the size of the Linked List by 1 after popping a node.
        del x  # Deleting the node object we wish to pop.

        # Returning the popped value
        return v

    # Removes the Node with the given value in the Linked List
    def popByVal(self, val):
        # Cannot pop a value from an empty Linked List
        if self.head is None:
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
            while x.data != val and x.next != self.head:
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
    print("Length:",len(ll))
    ll.display()
    ll.popFirst()
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
    print(ll.isEmpty())
    print("Len:",len(ll))

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
