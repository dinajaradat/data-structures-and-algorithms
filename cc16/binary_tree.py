class Node:
    def __init__(self,value):
        """
        Initializes a new Node object with the given value.

        Args:
            value: The value to be stored in the node.
        """
        self.value = value
        self.left = None
        self.right = None

class Binary_Tree:
    """
        Initializes a new Binary_Tree object.
    """

    def __init__(self):
        self.root = None
        self.max =0

    def traverse(self,node):
        """
        Recursively traverses the binary tree to find the maximum value.

        Args:
            node (Node): The current node being visited.

        Returns:
            None
        """
        # print(node.value)
        if node is None:
            return None
        if node is not None:
            if node.value > self.max:
                self.max = node.value
        if node.left is not None:
            self.traverse(node.left)
        if node.right is not None:
            self.traverse(node.right)
 
        
    
    def tree_max(self):
        """
        Finds the maximum value stored in the binary tree.

        Returns:
            number: The maximum value in the tree.
        """
        # print(self.root.value)
        self.traverse(self.root) 
        return self.max

    def pre_order(self, node):
        """
        Performs a pre-order traversal of the binary tree rooted at the given node.

        Args:
            node (Node): The root node of the binary tree.

        Returns:
            list: A list containing the values of the nodes visited in pre-order traversal.
        """
        output = []
        # print(node.value)
        # if node == None:
        #     return output
        if node is None:
            return None
        if node is not None:
            # print(node.value)
            output.append(node.value)
        if node.left is not None:
            # print(node.value)
            output += self.pre_order(node.left)
        if node.right is not None:
            # print(node.value)
            output += self.pre_order(node.right)
        # print(node.value)
        return output
    
    def In_order(self, node):
        """
        Performs an in-order traversal of the binary tree rooted at the given node.

        Args:
            node (Node): The root node of the binary tree.

        Returns:
            list: A list containing the values of the nodes visited in in-order traversal.
        """

        output = []
        if node is None:
            return None
        
        if node.left is not None:
            # print(node.value)
            output += self.In_order(node.left)
        
        if node is not None:
            # print(node.value)
            output.append(node.value)
        
        if node.right is not None:
            # print(node.value)
            output += self.In_order(node.right)
        # print(node.value)
        return output
    
    def post_order(self, node):
        """
        Performs a post-order traversal of the binary tree rooted at the given node.

        Args:
            node (Node): The root node of the binary tree.

        Returns:
            list: A list containing the values of the nodes visited in post-order traversal.
        """

        output = []
        if node is None:
            return None
        
        if node.left is not None:
            # print(node.value)
            output += self.post_order(node.left)

        if node.right is not None:
            # print(node.value)
            output += self.post_order(node.right)
        # print(node.value)

        if node is not None:
            # print(node.value)
            output.append(node.value)

        return output
    

    
class Binary_Search_Tree(Binary_Tree):
    
    def Add(self , value):
        """
        Adds a new node with the given value to the binary search tree.

        Args:
            value (any): The value to be added to the tree.
        """
        node = Node(value)
        if self.root is None:
            self.root = node
            # print(self.root.value)
            return 
        else:
            temp = self.root
            while temp:
                if value < temp.value:
                    if temp.left is None:
                        temp.left = node
                        # print( temp.left.value)
                        return
                    else:
                        temp = temp.left

                else:
                    if temp.right is None:
                        temp.right = node
                        # print(temp.right.value)
                        return 
                    else:
                        temp = temp.right

    
    def Contains(self,value):
        """
        Checks if the binary search tree contains a node with the given value.

        Args:
            value (any): The value to be searched in the tree.

        Returns:
            bool: True if the value is found in the tree, False otherwise.
        """
        temp = self.root
        while temp:
            if value == temp.value:
                return True
            else:
                if value < temp.value:
                    temp = temp.left
                else:
                    temp = temp.right
        
        return False



        
   



if __name__ == "__main__":
    tree = Binary_Tree()

    node1 = Node(2)
    node2 = Node(7)
    node3 = Node(5)
    node4 = Node(8)
    node5 = Node(11)
    node6 = Node(6)
    
    tree.root = node1
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6

    print(tree.tree_max())


