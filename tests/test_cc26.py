from cc26.InsertionSort import InsertionSort
def test_1():

    input = []
    actual = InsertionSort(input)
    expected = []
  
    assert actual == expected


def test_2():
    input = [2]
    actual = InsertionSort(input)
    expected = [2]
  
    assert actual == expected

def test_3():

    input = [58,18,-1,8,5,-2,-10]
    actual = InsertionSort(input)
    expected = [-10, -2, -1, 5, 8, 18, 58]
  
    assert actual == expected

def test_4():
    
    input = [58,-10]
    actual = InsertionSort(input)
    expected = [-10,58]
  
    assert actual == expected