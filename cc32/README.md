# tree-intersection


# Whiteboard Process

![img](./cc_32.png)
![tests](../tests/test_cc32.py)


# Approach & Efficiency
### Initialize an empty hashmap and an empty set.
### Create a recursive function traverse to traverse the nodes of tree1 and populate the hashmap with the values encountered.
    If the current node is None, return None.
    else, add the current node's value as a key to the hashmap with a value of True.
    Recursively call traverse for the left and right child nodes.
### traverse(tree1.root) to populate the hashmap with values from tree1.
### Define another recursive function find_intersection(node) to traverse the nodes of tree2 and find the intersection of values.
    If the current node is None, return None.
   If the current node's value exists in the hashmap, add it to the intersection set.
   Recursively call find_intersection for the left and right child nodes.
### find_intersection(tree2.root) to find the intersection of values in tree2 using the hashmap.
### Return the intersection_set.

## time --> O(n + m), where n is the number of nodes in tree1 and m is the number of nodes in tree2
## Space -->  O(n + m)




# Solution

            tree1 = BinaryTree()

            tree1.root = Node(100)
            tree1.root.left = Node(200)
            tree1.root.right = Node(300)
            tree1.root.left.left = Node(700)
            tree1.root.left.right = Node(125)

            tree2 = BinaryTree()

            tree2.root = Node(150)
            tree2.root.left = Node(100)
            tree2.root.right = Node(200)
            tree2.root.left.left = Node(700)
            tree2.root.left.right = Node(125)
            tree2.root.right.left = Node(75)



            values = tree_intersection(tree1, tree2)

## output = 
            {200, 700, 100, 125}
           