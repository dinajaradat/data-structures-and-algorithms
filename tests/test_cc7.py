
from cc7.linked_list import LinkedList

def test_greater_than_length():

    LL= LinkedList()

    LL.append(1)
    LL.append(2)
    LL.append(3)
    LL.append(4)


    actual = (LL.kthFromEnd(7))
    expected = None
  
    assert actual == expected

def test_k_equal_to_list_length():

    LL= LinkedList()

    LL.append(1)
    LL.append(2)
    LL.append(3)
    LL.append(4)


    actual = (LL.kthFromEnd(4))
    expected = None
  
    assert actual == expected

def test_nonpositive_k():

    LL= LinkedList()

    LL.append(1)
    LL.append(2)
    LL.append(3)
    LL.append(4)


    actual = (LL.kthFromEnd(-1))
    expected = None
  
    assert actual == expected

def test_linked_list_size_one():
    LL= LinkedList()

    LL.append(1)

    actual = (LL.kthFromEnd(0))
    expected = 1
  
    assert actual == expected

def test_k_in_the_middle():
    
    LL= LinkedList()

    LL.append(1)
    LL.append(2)
    LL.append(3)
    LL.append(4)
    LL.append(5)


    actual = (LL.kthFromEnd(1))
    expected = 4
  
    assert actual == expected

