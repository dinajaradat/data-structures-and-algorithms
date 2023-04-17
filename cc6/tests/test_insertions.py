from linked_list import linked_list

def test_empty_LL():
    LL = linked_list()

    actual = str(LL)
    expected = "LL is Empty"
    assert actual == expected

def test_append_to_end():
    
    LL= linked_list()

    LL.append(1)
    LL.append(2)
    LL.append(3)

    actual = str(LL)
    expected = "1 --> 2 --> 3 --> X"
  
    assert actual == expected