from cc6.linked_list import LinkedList

def test_empty_LL():
    LL = LinkedList()

    actual = str(LL)
    expected = "LL is Empty"
    assert actual == expected

def test_append_to_end():
    
    LL= LinkedList()

    LL.append(1)
    LL.append(2)
    LL.append(3)

    actual = str(LL)
    expected = "1 --> 2 --> 3 --> X"
  
    assert actual == expected

def test_insert_before_middle():
    LL= LinkedList()

    LL.append(1)
    LL.append(2)
    LL.append(3)
    LL.append(4)

    LL.insert_before(3, 6)

    actual = str(LL)
    expected = "1 --> 2 --> 6 --> 3 --> 4 --> X"
  
    assert actual == expected

def test_insert_before_first_node():
    LL= LinkedList()

    LL.append(1)
    LL.append(2)
    LL.append(3)
    LL.append(4)

    LL.insert_before(LL.head.value, 6)

    actual = str(LL)
    expected = "6 --> 1 --> 2 --> 3 --> 4 --> X"
  
    assert actual == expected

def test_insert_after_middle():
    LL= LinkedList()

    LL.append(1)
    LL.append(2)
    LL.append(3)
    LL.append(4)

    LL.insert_after(2, 6)

    actual = str(LL)
    expected = "1 --> 2 --> 6 --> 3 --> 4 --> X"
  
    assert actual == expected


def test_insert_after_last_node():
    LL= LinkedList()

    LL.append(1)
    LL.append(2)
    LL.append(3)
    LL.append(4)

    LL.insert_after(4, 6)

    actual = str(LL)
    expected = "1 --> 2 --> 3 --> 4 --> 6 --> X"
  
    assert actual == expected
