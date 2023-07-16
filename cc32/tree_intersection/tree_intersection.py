class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def tree_intersection(tree1, tree2):
    hashmap = {}
    intersection_set = set()

    def traverse(node):
        if node is None:
            return None
        hashmap[node.value] = True
        traverse(node.left)
        traverse(node.right)

    traverse(tree1.root)

    def find_intersection(node):
        if node is None:
            return None
        if node.value in hashmap:
            intersection_set.add(node.value)
        find_intersection(node.left)
        find_intersection(node.right)

    find_intersection(tree2.root)
    
    return intersection_set



class BinaryTree:
    def __init__(self):
        self.root = None

        


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


print(values)

