
# from cc10.node import Node
from cc10.node import Node

class Stack:

    def __init__(self):
        """
        Initializes an empty stack with a top pointer set to None.
        """
        self.top = None
    
    def push(self,value):
        """
        Add a new node with the given value to the top of the stack.
        """
        node = Node(value)
        node.next = self.top
        self.top = node
        return self.top

    def pop(self):
        """
        Removes and returns the node at the top of the stack. Raises an exception if the stack is empty.
        """

    

        if self.top is None:   # Check if the stack is empty
            
            raise Exception("Empty stack")
        
        current = self.top
        self.top = self.top.next
        current.next = None
        return current.value

    def peek(self):
        """
        Returns the value of the node at the top of the stack without removing it. Raises an exception if the stack is empty.
        """
        if self.is_empty():
            raise Exception("Empty stack")
        return  self.top.value
   
    def is_empty(self):
        """
        Returns True if the stack is empty, False otherwise.
        """
        if self.top is None:   # Check if the stack is empty
            
            return True
        return False
    
    def __str__(self):
        """
        Returns a string representation of the stack.

        """
        output = "" 

        if self.top is None:
            raise Exception("Empty stack")

        else:
            current = self.top
            
            while (current):
                output =  output + f'{current.value} --> '
                current = current.next
            output += "None"

        return output
    

if __name__ =="__main__":
 
    S = Stack()

    S.push(1)
    S.push(2)
    S.push(3)
    S.push(4)

    # print (S)

    print(str(S))
    print(S.pop())

    print(S.is_empty())
    print(S.peek())