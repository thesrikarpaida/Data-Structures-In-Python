"""
A Stack is a linear data structure that follows the Last-In First-Out (LIFO) order in performing operations.
It is implemented using Linked List in this program.
"""


# The Node class has 2 elements:
#   Data element: Value of the node
#   Next Link: The Linked List node that points to the next node
class Node:

    # Initializing the Node object (constructor)
    def __init__(self, data):
        self.data = data
        self.next = None


class StackLL:

    # Initializing the StackLL object
    def __init__(self):
        # Initializing a head node to traverse in the Linked List of the Stack
        self.head = None
        self.size = 0

    # Defining the len(<StackLL-Obj-Name>) function for the Stack object
    def __len__(self):
        return self.size

    # Returns True if the Stack is empty, else returns False
    def isEmpty(self):
        return self.size == 0

    # Prints the elements of the Stack from top to bottom
    def display(self):
        # Cannot print anything if Stack is empty.
        if self.isEmpty():
            print("Stack is empty.")
            return
        x = self.head
        print("Stack:")
        while x != None:
            print(x.data)
            x = x.next

    # Returns the top element of the Stack
    def top(self):
        # There is no top of Stack if it is empty.
        if self.isEmpty():
            print("Stack is empty.")
            return
        return self.head.data

    # Pushes an element to the top of the Stack
    def push(self, val):
        x = Node(val)
        # If Stack is empty, we can point the head to the pushed node.
        if self.isEmpty():
            self.head = x
        else:
            x.next = self.head
            self.head = x
        self.size += 1  # Increasing the size of the Stack by 1 after pushing a node.

    # Removes the top elements of the Stack and returns the value
    def pop(self):
        # Cannot pop any element from the Stack if it is empty.
        if self.isEmpty():
            print("Stack is empty. Cannot perform operation.")
            return
        x = self.head
        self.head = self.head.next
        v = x.data
        del x  # Deleting the node object we wish to pop.
        self.size -= 1  # Decreasing the size of the Stack by 1 after popping a node.

        # Returning the popped value
        return v

    # Checks if the given value exists in the Stack
    def exists(self, val):
        # If the Stack is empty, there won't be any value in it to check with.
        # So the given value does not exist in such a case.
        if self.isEmpty():
            return False

        x = self.head
        # Traverse through the Stack until we find the value given or reach the bottom element.
        while x.next != None and x.data != val:
            x = x.next
        if val == x.data:
            return True
        if x.next is None:
            return False


if __name__ == "__main__":
    st = StackLL()
    st.push(1)
    st.push(2)
    st.push(3)
    st.push(4)
    st.push(5)
    st.display()
    st.pop()
    st.display()
    print("Is Empty:",st.isEmpty())
    print("3 in Stack?",st.exists(3))
    print("Size of Stack:",len(st))
    print("Top of Stack:",st.top())
