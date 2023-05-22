from cc16.binary_tree import Node
from cc16.binary_tree import Binary_Tree
def test_1():

    tree = Binary_Tree()


    actual = tree.tree_max()
    expected = 0
  
    assert actual == expected

def test_2():

    tree = Binary_Tree()
    node1 = Node(2)

    
    tree.root = node1
 
    actual = tree.tree_max()
    expected = 2
  
    assert actual == expected


def test_3():

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

    actual = tree.tree_max()
    expected = 11
  
    assert actual == expected


def test_4():

    tree = Binary_Tree()
    node1 = Node(8)
    node2 = Node(7)
    node3 = Node(2)
    node4 = Node(14)
    node5 = Node(11)
    node6 = Node(1)
    
    tree.root = node1
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6

    actual = tree.tree_max()
    expected = 14
  
    assert actual == expected