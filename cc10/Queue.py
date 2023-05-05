from cc10.node import Node

class Queue :

    def __init__(self):
        self.front = None
        self.rear = None
    
    def enqueue(self,value):
        node = Node(value)    # Create a new node
       
            
        if self.front is None:   # Check if the queue is empty
            self.front = node
            self.rear = node
            return
        else:
            current = self.rear
            self.rear = node
            current.next = self.rear 

    def dequeue(self):
    

        if self.rear is None:   # Check if the queue is empty
            
            raise Exception("Empty Queue")
        else:
            current = self.rear
            self.rear = self.rear.next
            current.next = None

    def peek(self):
        if self.is_empty():
            raise Exception("Empty Queue")
        return self.front.value
   
    def is_empty(self):
        if self.front is None:   # Check if the queue is empty
            
            return True
        return False