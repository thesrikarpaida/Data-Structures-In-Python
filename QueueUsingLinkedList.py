"""
A Queue is a linear data structure that follows the First-In First-Out (FIFO) order of performing operations.
It is implemented using Linked List in this program.
"""


# The Node class has 2 elements:
#   Data element: Value of the node
#   Next Link: The Linked List node that points to the next node
class Node:

    # Initializing the Node object (constructor)
    def __init__(self, data):
        # Initializing a head node to traverse in the Linked List of the Queue
        self.data = data
        self.next = None


class QueueLL:

    # Initializing the QueueLL object
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # Defining the len(<QueueLL-Obj-Name>) function for the QueueLL object
    def __len__(self):
        return self.size

    # Returns True if the Queue is empty, else returns False
    def isEmpty(self):
        return self.size == 0

    # Prints the elements of the Queue from front to back
    def display(self):
        # Cannot print anything if Queue is empty.
        if self.isEmpty():
            print("Queue is empty.")
            return
        x = self.head
        print("Queue:")
        print("Front",end=" <- ")
        while x != None:
            print(x.data,end=" <- ")
            x = x.next
        print("Back")

    # Adding a new node with the given value at the end of the Queue
    def enqueue(self, val):
        x = Node(val)
        if self.isEmpty():
            self.head = x
        else:
            self.tail.next = x
        self.tail = x
        self.size += 1  # Increasing the size of the Stack by 1 after pushing a node.

    # Removing the node at the front of the Queue and returning its value
    def dequeue(self):
        # Cannot remove any node if the Queue is empty.
        if self.isEmpty():
            print("Queue is empty. Cannot perform operation.")
            return
        x = self.head
        self.head = self.head.next
        v = x.data
        self.size -= 1  # Decreasing the size of the Stack by 1 after popping a node.
        del x  # Deleting the node object we wish to remove.

        # Returning the removed value
        return v

    # Returns the node at the front of the Queue
    def front(self):
        # There won't be any node at the front if Queue is empty.
        if self.isEmpty():
            print("Queue is empty.")
            return
        return self.head.data

    # Returns the node at the back of the Queue (most recently added element)
    def back(self):
        # There won't be any node at the back if Queue is empty.
        if self.isEmpty():
            print("Queue is empty.")
            return
        return self.tail.data

    # Checks if the given value exists in the Queue
    def exists(self, val):
        # If the Queue is empty, there won't be any value in it to check with.
        # So the given value does not exist in such a case.
        if self.isEmpty():
            return False

        x = self.head
        # Traverse through the Queue until we find the value given or reach the last element.
        while x.next != None and x.data != val:
            x = x.next
        if val == x.data:
            return True
        if x.next is None:
            return False


if __name__ == "__main__":
    qu = QueueLL()
    qu.enqueue(1)
    qu.enqueue(2)
    qu.enqueue(3)
    qu.enqueue(4)
    qu.enqueue(5)
    qu.enqueue(16)
    qu.display()
    qu.dequeue()
    qu.display()
    print("Front:", qu.front())
    print("Back:", qu.back())
    print("7 in Queue?", qu.exists(7))
    print("Is Empty:", qu.isEmpty())
    print("Size of Queue:", len(qu))
