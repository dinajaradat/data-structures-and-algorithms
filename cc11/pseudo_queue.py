from node import Node
from stack import Stack


class Pseudo_queue:
    def __init__(self):
        self.top = None
        self.stack2 = Stack()
       
    
    def push(self, value):
        """
        Pushes a node with the given value to the first stack.
        """
        node = Node(value)
        node.next = self.top
        self.top = node
        print(self.top.value)
        return node.value  # return the value of the pushed node instead of the node object

    def pop(self):
        """
        Removes and returns the first node of the first stack.
        """
        
        print(self)
        if self.top is None:
            raise Exception("Empty stack")
        
        current = self.top
        temp =self.top
        
        while current.next is not None:
            current = current.next
        while temp.next != current:
            temp = temp.next
        
        temp.next = None
        # print(temp.value)
        
        
        return current.value
    
    def is_empty(self):
        """
        Returns True if the stack is empty, False otherwise.
        """
        if self.top is None:   # Check if the stack is empty
            return True
        elif self.stack2.top is None:
            return True
        return False
    

    def peek(self):
        """
        Returns the value of the top node of the first stack without removing it.
        """
        if self.is_empty():
            raise Exception("Empty stack")
        return self.top.value


    def enqueue(self, value):
        """
        Enqueues a node with the given value to the end of the stack.
        """

        if self.is_empty():
           self.push(value)
        else:
            while not self.is_empty():
                 self.stack2.push(self.pop())
            self.push(value)
            while not self.stack2.is_empty():
                 self.push(self.stack2.pop())
        
        return self
       
    

    def dequeue(self):
        """
        Dequeues the node at the front of the stack and returns its value.
        """
  
        # print (self)
        

        return self.pop()
    

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
                output =  output + f'<-- {current.value}  '
                current = current.next
            output = "None" + output

        return output
    

    

if __name__ == "__main__":


    S1 = Pseudo_queue()

    S1.enqueue(20)
    S1.enqueue(15)
    S1.enqueue(10)
   
    S1.enqueue(5)
    S1.dequeue()

    print(str(S1))

    
 


