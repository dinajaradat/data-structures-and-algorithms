class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class delete_Node_BST(object):
    def deleteNode(self, root, key):
        if root is None:
            return None

        if key < root.value:
            root.left = self.deleteNode(root.left, key)
        elif key > root.value:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            suc = self.findMinimum(root.right)
            root.value = suc.value

            root.right = self.deleteNode(root.right, suc.value)

        return root.value

    def findMinimum(self, node):
        while node.left:
            node = node.left
        return node


root1 = Node(1)
root1.left = Node(3)
root1.right = Node(6)
root1.left.right = Node(4)
root1.right.right = Node(7)

d1 = delete_Node_BST()
print(d1.deleteNode(root1,3))