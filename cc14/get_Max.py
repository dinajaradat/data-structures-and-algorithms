from node import Node

class Max_Stack:
    def __init__(self):
        self.top = None
        self.max = 0

    def push(self,value):

        if value > self.max :
                self.max = value

        node = Node(value)

        if self.top == None:
            self.top = node
            
        else:
            node.next = self.top
            self.top = node
            

        return self.top.value
    
    def pop(self):
       
        if self.top == None:
            raise Exception ("Empty Stack")
        else:
            temp = self.top
            self.top = self.top.next
            temp.next = None
            if temp.value == self.max:
               self.max = 0 
               current = self.top
               while current.next is not None:
                    if current.value > self.max:
                       self.max = current.value
                    current = current.next
                   
        return temp.value

    
    def getMax(self):
        return self.max


        

    

if __name__ == "__main__":
    S = Max_Stack()

    S.push(3)
    S.push(2)
    S.push(3)
    S.push(4)
    S.push(9)

    print(S.getMax())

    print(S.pop())

    print(S.getMax())


