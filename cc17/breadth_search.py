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
    A class representing a binary tree.

    Attributes:
        root: The root node of the binary tree.
    """

    def __init__(self):
        self.root = None
        self.max =0

    def breadth(self):
        """
        Performs breadth-first traversal of the binary tree and returns the values in a list.
        
        Returns:
            A list of values representing the breadth-first traversal of the binary tree.
        """
        output = [] 
        if self.root is None:
            return output
        
        # print(self.root.value)
        

        def breadth_recursive(queue):
            if not queue:
                return

            current = queue.pop(0)
            output.append(current.value)

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

            breadth_recursive(queue)
        
        queue = [self.root]
        breadth_recursive(queue)
        return output


                 


    



if __name__ == "__main__":
    tree = Binary_Tree()

    node1 = Node(2)
    node2 = Node(7)
    node3 = Node(5)
    node4 = Node(2)
    node5 = Node(6)
    node6 = Node(9)
    node7 = Node(5)
    node8 = Node(11)
    node9 = Node(4)
    
    tree.root = node1
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node5.left = node7
    node5.right = node8
    node6.left = node9

    # print(tree.tree_max())
    print(tree.breadth())


