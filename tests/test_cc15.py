from cc15.binary_tree import Node
from cc15.binary_tree import Binary_Tree
from cc15.binary_tree import Binary_Search_Tree
def test_1():

    tree = Binary_Tree()

    actual = tree.pre_order(tree.root)
    expected = None
  
    assert actual == expected

def test_2():

    tree = Binary_Tree()

    actual = tree.In_order(tree.root)
    expected = None
  
    assert actual == expected

def test_3():

    tree = Binary_Tree()

    actual = tree.post_order(tree.root)
    expected = None
  
    assert actual == expected

def test_4():

    tree = Binary_Tree()
    node1 = Node("A")

    
    tree.root = node1


    actual = tree.pre_order(tree.root)
    expected = ['A']
  
    assert actual == expected

def test_5():

    B = Binary_Search_Tree()
    B.Add(5)
    B.Add(9)
    B.Add(3)


    actual =  B.pre_order(B.root)
    expected = [5,3,9]
  
    assert actual == expected

def test_6():

    tree = Binary_Tree()
    node1 = Node("A")
    node2 = Node("B")
    node3 = Node("C")
    node4 = Node("D")
    node5 = Node("E")
    node6 = Node("F")
    
    tree.root = node1
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6


    actual = tree.pre_order(tree.root)
    expected = ['A', 'B', 'D', 'E', 'C', 'F']
  
    assert actual == expected

def test_7():

    tree = Binary_Tree()
    node1 = Node("A")
    node2 = Node("B")
    node3 = Node("C")
    node4 = Node("D")
    node5 = Node("E")
    node6 = Node("F")
    
    tree.root = node1
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6


    actual = tree.In_order(tree.root)
    expected = ['D', 'B', 'E', 'A', 'F', 'C']
  
    assert actual == expected

def test_8():

    tree = Binary_Tree()
    node1 = Node("A")
    node2 = Node("B")
    node3 = Node("C")
    node4 = Node("D")
    node5 = Node("E")
    node6 = Node("F")
    
    tree.root = node1
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6


    actual = tree.post_order(tree.root)
    expected = ['D', 'E', 'B', 'F', 'C', 'A']
  
    assert actual == expected

def test_9():

    B = Binary_Search_Tree()
    B.Add(5)
    B.Add(9)
    B.Add(3)
    B.Add(6)
    B.Add(7)
    B.Add(1)


    actual =  B.Contains(9)
    expected = True
  
    assert actual == expected

def test_10():

    B = Binary_Search_Tree()
    B.Add(5)
    B.Add(9)
    B.Add(3)
    B.Add(6)
    B.Add(7)
    B.Add(1)


    actual =  B.Contains(10)
    expected = False
  
    assert actual == expected