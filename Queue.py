"""
A Queue is a linear data structure that follows the First-In First-Out (FIFO) order of performing operations.
It is implemented using list (array) in this program.
"""


class Queue:

    # Initializing the Queue object
    def __init__(self):
        self.data = list()

    # Defining the len(<Queue-Obj-Name>) function for the Queue object
    def __len__(self):
        return len(self.data)

    # Returns True if the Queue is empty, else returns False
    def isEmpty(self):
        return len(self.data) == 0

    # Checks if the given value exists in the Queue
    def exists(self, val):
        return val in self.data

    # Prints the elements of the Queue from front to back
    def display(self):
        # Cannot print anything if Queue is empty.
        if self.isEmpty():
            print("Queue is empty.")
            return
        print("Queue:\nFront", end=" <- ")
        for i in self.data:
            print(i, end=" <- ")
        print("Back")

    # Adding a new node with the given value at the end of the Queue
    def enqueue(self, val):
        self.data.append(val)

    # Removing the node at the front of the Queue and returning its value
    def dequeue(self):
        # Cannot remove any node if the Queue is empty.
        if self.isEmpty():
            print("Queue is empty. Cannot perform operation.")
            return

        return self.data.pop(0)

    # Returns the node at the front of the Queue
    def front(self):
        # There won't be any node at the front if Queue is empty.
        if self.isEmpty():
            print("Queue is empty.")
            return
        return self.data[0]

    # Returns the node at the back of the Queue (most recently added element)
    def back(self):
        # There won't be any node at the back if Queue is empty.
        if self.isEmpty():
            print("Queue is empty.")
            return
        return self.data[-1]


if __name__ == "__main__":
    qu = Queue()
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
