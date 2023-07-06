from cc32.tree_intersection.tree_intersection import tree_intersection
from cc32.tree_intersection.tree_intersection import BinaryTree
from cc32.tree_intersection.tree_intersection import Node


def test_1():
   
    tree1 = BinaryTree()
    tree2 = BinaryTree()

    expected = set()
    actual = tree_intersection(tree1, tree2)

    assert expected == actual 

def test_2():
    
    tree1 = BinaryTree()

    tree1.root = Node(500)
    tree1.root.left = Node(0)
    tree1.root.right = Node(150)

    tree2 = BinaryTree()


    expected = set()
    actual = tree_intersection(tree1, tree2)

    assert expected == actual 

def test_3():
   
    tree1 = BinaryTree()

    tree1.root = Node(500)
    tree1.root.left = Node(100)
    tree1.root.right = Node(150)

    tree2 = BinaryTree()

    tree2.root = Node(150)
    tree2.root.left = Node(100)
    tree2.root.right = Node(200)

  

    expected = {100,150}
    actual = tree_intersection(tree1, tree2)

    assert expected == actual 

def test_4():

    tree1 = BinaryTree()

    tree1.root = Node(500)
    tree1.root.left = Node(100)
    tree1.root.right = Node(150)

    tree2 = BinaryTree()

    tree2.root = Node(15)
    tree2.root.left = Node(101)
   
    expected = set()
    actual = tree_intersection(tree1, tree2)
    assert expected == actual 
