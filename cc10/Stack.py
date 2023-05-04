from cc10.node import Node

class stack:

    def __init__(self):
        self.top = None
    
    def push(self,value):
        node = Node(value)    # Create a new node
       

        if self.top is None:   # Check if the stack is empty
            self.top = node
            return
        else:
            current = self.top
            self.top = node
            self.top.next = current

    def pop(self):
    

        if self.top is None:   # Check if the stack is empty
            
            raise Exception("Empty stack")
        else:
            current = self.top
            self.top = self.top.next
            current.next = None

    def peek(self):
        if self.is_empty():
            raise Exception("Empty stack")
        return self.front.value
   
    def is_empty(self):
        if self.top is None:   # Check if the stack is empty
            
            return True
        return False