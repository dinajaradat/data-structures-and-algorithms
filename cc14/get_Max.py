from node import Node
from stack import Stack
class Max_Stack:
    def __init__(self):
        self.top = None
        self.maxStack = Stack()

    def push(self,value):
        node = Node(value)

        if self.top == None:
            self.top = node
            self.maxStack.top = node
        else:
            if node > self.maxStack.top.value:
                self.maxStack.top = node
            node.next = self.top
            self.top = node
            

        return self.top.value
    
    def pop(self):
        if self.top == None:
            raise Exception ("Empty Stack")
        else:
            temp = self.top
            if self.maxStack.top.value == self.top.value:
                self.maxStack.top = None
            self.top = self.top.next
            temp.next = None

        return temp.value
    

    
    def getMax(self,value):
        
        if self.top == None:
            self.push(value)
            self.maxStack.push(value)
            # print(self.maxStack.top.value)
        else:
            if value >= self.maxStack.top.value:
                self.push(value)
                self.maxStack.pop()
                self.maxStack.push(value)
                # print(self.maxStack.top.value)
            else:
                self.push(value)
                # print(self.maxStack.top.value)
            
        # print(self.maxStack.top.value)


            

       

    

if __name__ == "__main__":
    stack1 = Max_Stack()
    stack1.getMax(5)
    stack1.getMax(4)
    stack1.getMax(9)
    stack1.getMax(3)
    stack1.getMax(7)
    print(stack1.maxStack.top.value)



#  Max_Stack.push(self.top.value)
#         current = self.top
#         while current is not None:
#             current = current.next
#             if current.value >= Max_Stack.top.value:
#                 Max_Stack.pop()
#                 Max_Stack.push(current.value)
            
#         return Max_Stack.top.value