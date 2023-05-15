from cc13.node import Node
class Stack:

    def __init__(self):
        self.top = None
    
    def push(self,value):
        """
        Pushes a new element onto the top of the stack.

        Args:
            value: The value of the new element.

        Returns:
            The value of the new element that was pushed onto the stack.
        """

        node =Node(value)
        if self.top == None:
             self.top = node
        else:
             node.next = self.top
             self.top = node

        return self.top.value
    
    def pop(self):
        """
        Removes and returns the top element from the stack.

        Returns:
            The value of the top element that was removed.

        Raises:
            Exception: If the stack is empty and pop is called.
        """
        
        if self.top == None:
            raise Exception("Empty stack")
        else:
            temp = self.top
            self.top = self.top.next
            temp.next = None
        return temp.value
              
              


    def Validate_brackets(self,string):
            """
            Validates the brackets in the given string.

            Args:
                string: The string containing brackets to be validated.

            Returns:
                True if each open bracket has a close bracket.
            """

            for i in string:
                # print(i, end="")
                if i == "(" or i == "[" or i == "{":
                    self.push(i)
                
                if i == ")":
                    if self.top and self.top.value == "(":
                        self.pop()
                    else:
                        return False

                if i == "]":
                    if self.top and self.top.value == "[":
                        self.pop()
                    else:
                        return False
                
                if i == "}":
                    if self.top and self.top.value == "{":
                        self.pop()
                    else:
                        return False

            # print(self.top.value)
            if self.top == None:
                return True
            else:
                return False
                    
            
  

if __name__ =="__main__":
    stack = Stack()
    print(stack.Validate_brackets("{}"))
    print(stack.Validate_brackets("{}(){}"))
    print(stack.Validate_brackets("()[[Extra Characters]]"))
    print(stack.Validate_brackets("(){}[[]]"))
    print(stack.Validate_brackets("{}{Code}[Fellows](())"))
    print(stack.Validate_brackets("[({}]"))
    print(stack.Validate_brackets("(]("))
    print(stack.Validate_brackets("[({}]"))

