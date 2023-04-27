from cc7.node import Node
# from node import Node

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self,value):
        node = Node(value)    # Create a new node
       

        if self.head is None:   # Check if the list is empty
            self.head = node
            return
        else:
            current = self.head   # Traverse the list to find the last node 
            while current.next is not None:
                current = current.next
            current.next = node   # append the new node at the  end of list 
            return 


    def insert_before(self,value, new_value):
        new_node = Node(new_value)    # Create a new node with the new value

        if self.head is None:         # Check if the list is empty
            self.head = new_node
            return

        if self.head.value == value:   # If the value to insert before = the head node
            new_node.next = self.head
            self.head = new_node
            return

        else:
            current = self.head         
            while current.next is not None:   # Traverse the list to find the node with the value
                if current.next.value == value:
                    new_node.next = current.next
                    current.next = new_node
                    return
                current = current.next
                
            current.next = new_node       # If the value is not found in the list --> append the new node at the  end of list 


    def insert_after(self,value, new_value):
        new_node = Node(new_value)    # Create a new node with the new value


        if self.head is None:         # Check if the list is empty
            self.head = new_node
            return
        
        else:
            current = self.head
            while current is not None:    # Traverse the list to find the node with the value
                if current.value == value:
                    new_node = Node(new_value)
                    new_node.next = current.next
                    current.next = new_node
                    return
            
                current = current.next

    
    def kthFromEnd(self,k):
        
        if k < 0:
            return None
        if self.head is None:         # Check if the list is empty
            return None
        
        if self.head.next is None:
            if k == 0:
                return self.head.value

        
        else:
            pointer1 = self.head
            pointer2 = self.head

            while pointer2.next is not None:
                 pointer2 = pointer2.next
            # print (pointer2.value)
            for i in range (k):
                   pointer1 = pointer1.next
                   current = self.head
     
                   while current.next != pointer2 :
                        if current.next is None:
                           return 
                        current = current.next
                   pointer2 = current    
                       

            return pointer2.value
        

    def __str__(self):
        output = "" 

        if self.head is None:
            output = "LL is Empty"

        else:
            current = self.head
            
            while (current):
                output =  output + f'{current.value} --> '
                current = current.next
            output += 'X'

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
            output += 'X'
        
        return output