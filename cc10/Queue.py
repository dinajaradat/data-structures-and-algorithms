from cc10.node import Node
# from node import Node

class Queue :

    def __init__(self):
        """
        Initializes an empty queue with front and rear pointers set to None.
        """
        self.front = None
        self.rear = None
    
    def enqueue(self,value):
        """
        Adds a new node with the given value to the rear of the queue.
        """
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
        """
        Removes and returns the node at the front of the queue. Raises an exception if the queue is empty.
        """
    

        if self.rear is None:   # Check if the queue is empty
            
            raise Exception("Empty Queue")
        else:
            current = self.front 
            self.front = self.front.next
            current.next = None
            return current.value

    def peek(self):
        """
        Returns the value of the node at the front of the queue without removing it. Raises an exception if the queue is empty.
        """
        if self.is_empty():
            raise Exception("Empty Queue")
        return self.front.value
   
    def is_empty(self):
        """
        Returns True if the queue is empty, False otherwise.
        """
        if self.front is None:   # Check if the queue is empty
            
            return True
        return False
    
    def __str__(self):
        """
        Returns a string representation of the queue.

        """
        output = "" 

        if self.front is None:
            raise Exception("Empty Queue")

        else:
            current = self.front
            
            while (current):
                output =   f' <-- {current.value}' + output 
                current = current.next
            output = "None"+ output

        return output
    

if __name__ =="__main__":
 
    Q = Queue()

    Q.enqueue(1)
    Q.enqueue(2)
    Q.enqueue(3)
    Q.enqueue(4)

    # print (S)

    print(str(Q))
    print(Q.dequeue())
    print(str(Q))

    print(Q.is_empty())
    print(Q.peek())