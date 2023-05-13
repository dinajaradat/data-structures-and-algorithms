from cc12.node import Node
class animal:

    def __init__(self,species ,name ):
        self.name = name
        self.species = species
        

class AnimalShelter:
    def __init__(self):
        """
        Initializes an empty queue with front and rear pointers set to None.
        """
        
        self.front = None
        self.rear = None


    def enqueue(self,Animal):
        node = Node(Animal.species)
        if self.front == None:
            self.front = node
            self.rear = node
        else :
            current = self.rear
            self.rear = node
            current.next = self.rear 

        return self.rear

    
    def dequeue(self , pref):
       """
       Removes and returns the node at the front of the queue. Raises an exception if the queue is empty.
       """

    #    print(self.front.value)
    #    print(self.rear.value)
    #    print(pref)
       if self.front is None:   # Check if the queue is empty
        
           raise Exception("Empty Queue")
       else:
            if pref != "dog" and pref != "cat":
               return  "Null"
        
            else:
                # print(self.front.value)
                if self.front.value == pref:
                    current = self.front 
                    self.front = self.front.next
                    current.next = None
                    return current.value
                else:
                    current = self.front 
                    temp = self.front
                    while pref != current.value:
                        current = current.next
                    # print(current.value)

                    while temp.next != current:
                        temp = temp.next
                    temp.next = current.next
                    current.next = None
                    # print(current.value)
                    return current.value
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
            # print (self.front.value)
            current = self.front
            
            while (current):
                output =   f' <-- {current.value}' + output 
                current = current.next
            output = "None"+ output

        return output


if __name__=="__main__":
    animal1 = animal("cat","lila1")
    animal2 = animal("cat","lila2")
    animal3 = animal("dog","dody1")
    animal4 = animal("dog","dody2")
    animal5 = animal("dog","dody3")

    A1 = AnimalShelter()
    A1.enqueue(animal1)
    A1.enqueue(animal2)
    A1.enqueue(animal3)
    A1.enqueue(animal4)
    print(A1)

    A1.dequeue("cat")
    print(A1)

    A1.enqueue(animal5)
    print(A1)

    A1.dequeue("dog")
    print(A1)

