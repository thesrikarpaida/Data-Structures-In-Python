"""
A Stack is a linear data structure that follows the Last-In First-Out (LIFO) order in performing operations.
It is implemented using list (array) in this program.
"""


class Stack:

    # Initializing the Stack object
    def __init__(self):
        self.data = list()

    # Defining the len(<Stack-Obj-Name>) function for the Stack object
    def __len__(self):
        return len(self.data)

    # Returns True if the Stack is empty, else returns False
    def isEmpty(self):
        return len(self.data) == 0

    # Prints the elements of the Stack from top to bottom
    def display(self):
        # Cannot print anything if Stack is empty.
        if self.isEmpty():
            print("Stack is empty.")
            return
        print("Stack:")
        for i in reversed(self.data):
            print(i)

    # Returns the top element of the Stack
    def top(self):
        # There is no top of Stack if it is empty.
        if self.isEmpty():
            print("Stack is empty.")
            return
        return self.data[-1]

    # Pushes an element to the top of the Stack
    def push(self, n):
        self.data.append(n)

    # Removes the top elements of the Stack and returns the value
    def pop(self):
        # Cannot pop any element from the Stack if it is empty.
        if self.isEmpty():
            print("Stack is empty. Cannot perform operation.")
            return
        return self.data.pop()

    # Checks if the given value exists in the Stack
    def exists(self, val):
        return val in self.data


if __name__ == "__main__":
    st = Stack()
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
