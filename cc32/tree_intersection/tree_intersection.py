class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def tree_intersection(tree1, tree2):
    set1 = set()
    set2 = set()

    def traverse(node, set):
        if node is None:
            return
        set.add(node.value)
        traverse(node.left, set)
        traverse(node.right, set)

    traverse(tree1.root, set1)
    traverse(tree2.root, set2)

    # print(set1)
    # print(set2)

    return set1.intersection(set2)



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

