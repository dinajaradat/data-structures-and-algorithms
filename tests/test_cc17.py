from cc17.breadth_search import Binary_Tree
from cc17.breadth_search import Node
def test_1():

    tree = Binary_Tree()

    actual = tree.breadth()
    expected = []
  
    assert actual == expected


def test_2():

    tree = Binary_Tree()

    node1 = Node(2)
    
    tree.root = node1


    actual = tree.breadth()
    expected = [2]
  
    assert actual == expected

def test_3():

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


    actual = tree.breadth()
    expected = [2, 7, 5, 2, 6, 9, 5, 11, 4]
  
    assert actual == expected

def test_4():

    tree = Binary_Tree()

    node1 = Node(10)
    node2 = Node(5)
    node3 = Node(15)
    node4 = Node(3)
    node5 = Node(7)
    node6 = Node(12)
    node7 = Node(20)
    
    tree.root = node1
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node3.right = node7


    actual = tree.breadth()
    expected = [10, 5, 15, 3, 7, 12, 20]
  
    assert actual == expected