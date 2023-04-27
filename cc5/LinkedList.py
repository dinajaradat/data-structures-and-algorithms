from cc5.node import Node
# from node import Node

class LinkedList():
    def __init__(self):
        self.head = None

    def insert(self,value):
        # inserts a new node with the given value at the beginning of the linked list.
        node = Node(value)
        node.next = self.head
        self.head = node


    def includes(self,key): # key: A value to search for in the linked list.
        # Check whether a node with the given key value exists in the linked list.
        current = self.head
        while current:
          if current.value == key: # whether a node with the given key value exists in the linked list.
             return True
          current = current.next
        return False

    
    def __str__(self):
        
        output = ""

        if self.head is None:
           output = "LL is Empty"
        else:
            current = self.head
            while current:
                output += f"{current.value} --> "
                current = current.next
            output += "Null"
        return output
    
    
    def __repr__(self):
        output = ""

        if self.head is None:
           output = "LL is Empty"
        else:
            current = self.head
            while current:
                output += f"{current.value} --> "
                current = current.next
            output += "Null"
        return output
    