from node import Node

class LinkedList():
    def __init__(self):
        self.head = None

    def insert(self,value):
        node = Node(value)

        if self.head is None:
              self.head = node
        
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node

    def includes(self,key):
        current = self.head

        if current is None:
            return False
        else:

            while current is not None:
                if current.value is key :
                   return True
                current = current.next
        return False
    
    def __str__(self):
        output = ""

        if self.head is None:
            output = "LL is Empty"

        else :
            current = self.head
            while (current):
                output = f'{current.value} --> '+ output
                current = current.next
            output += 'Null'
        
        return output
    
    def __repr__(self):
        output = ""

        if self.head is None:
            output = "LL is Empty"

        else :
            current = self.head
            while (current):
                output = f'{current.value} --> '+ output
                current = current.next
            output += 'Null'
        
        return output