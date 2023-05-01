from cc8.Linked_List8 import LinkedList

def test_normal_with_same_length():

    LL1= LinkedList()
    LL2= LinkedList()
    LL = LinkedList()

    LL1.append(1)
    LL1.append(3)
    LL1.append(2)

    LL2.append(5)
    LL2.append(9)
    LL2.append(4)

    LL.zip_List(LL1,LL2)

    actual = str(LL)
    expected = "1 --> 5 --> 3 --> 9 --> 2 --> 4 --> X"
  
    assert actual == expected



def test_with_different_length():

    LL1= LinkedList()
    LL2= LinkedList()
    LL = LinkedList()

    LL1.append(1)
    LL1.append(3)

    LL2.append(5)
    LL2.append(9)
    LL2.append(4)

    LL.zip_List(LL1,LL2)

    actual = str(LL)
    expected = "1 --> 5 --> 3 --> 9 --> 4 --> X"
  
    assert actual == expected



def test_one_empty():

    LL1= LinkedList()
    LL2= LinkedList()
    LL = LinkedList()

    LL2.append(5)
    LL2.append(9)
    LL2.append(4)

    LL.zip_List(LL1,LL2)

    actual = str(LL)
    expected = "5 --> 9 --> 4 --> X"
  
    assert actual == expected



def test_2_empty():
    LL1= LinkedList()
    LL2= LinkedList()
    LL = LinkedList()


    LL.zip_List(LL1,LL2)

    actual = str(LL)
    expected = "LL is Empty"
  
    assert actual == expected


