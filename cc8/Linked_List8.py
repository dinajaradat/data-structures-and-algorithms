class Node:
    def __init__(self,value):
        
        """
        Initializes a new Node object with the given value.

        Args:
            value: The value to be stored in the node.
        """
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        """
        Initializes an empty linked list.
        """
        self.head = None
    
    def append(self,value):

        """
        Appends a new node with the given value to the end of the linked list.

        Args:
            value: The value to be stored in the new node.
        """
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
    
    def __str__(self):
        """
        Returns a string representation of the linked list.

        Returns:
            A string representing the linked list, with the node values separated by "-->" and ending with "X".
        """
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
        

    def zip_List(self,list1,list2):
         """
        Zips together two linked lists and returns a new linked list.

        Args:
            list1: The first linked list to be zipped.
            list2: The second linked list to be zipped.

        Returns:
            A new linked list containing the nodes from list1 and list2, alternately.

        """


         pointer1 = list1.head
         pointer2 = list2.head

         while pointer1 is not None and pointer2 is not None:
             self.append(pointer1.value)
             self.append(pointer2.value)

             pointer1 = pointer1.next
             pointer2 = pointer2.next

         while pointer1 is not None:
               self.append(pointer1.value)
               pointer1 = pointer1.next

         while pointer2 is not None:
               self.append(pointer2.value)
               pointer2 = pointer2.next


         return self


if __name__ =="__main__":
    LL1= LinkedList()
    LL2= LinkedList()
    LL = LinkedList()

    LL1.append(1)
    LL1.append(3)
    LL1.append(2)

    LL2.append(5)
    LL2.append(9)
    LL2.append(4)

    print (LL1)
    print (LL2)
    
    print(LL.zip_List(LL1,LL2))
