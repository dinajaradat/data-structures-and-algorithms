
from cc13.validate_brackets import Stack

def test_1():

    stack = Stack()

    actual = stack.Validate_brackets("")
    expected = True
  
    assert actual == expected

def test_2():

    stack = Stack()

    actual = stack.Validate_brackets("{}")
    expected = True
  
    assert actual == expected

def test_3():

    stack = Stack()

    actual = stack.Validate_brackets("{}(){}")
    expected = True
  
    assert actual == expected

def test_4():

    stack = Stack()

    actual = stack.Validate_brackets("()[[Extra Characters]]")
    expected = True
  
    assert actual == expected

def test_5():

    stack = Stack()

    actual = stack.Validate_brackets("(){}[[]]")
    expected = True
  
    assert actual == expected

def test_6():

    stack = Stack()

    actual = stack.Validate_brackets("{}{Code}[Fellows](())")
    expected = True
  
    assert actual == expected



def test_7():

    stack = Stack()

    actual = stack.Validate_brackets("[({}]")
    expected = False
  
    assert actual == expected

def test_8():

    stack = Stack()

    actual = stack.Validate_brackets("[({}]")
    expected = False
  
    assert actual == expected

def test_9():

    stack = Stack()

    actual = stack.Validate_brackets("(](")
    expected = False
  
    assert actual == expected

def test_10():

    stack = Stack()

    actual = stack.Validate_brackets("[({}]")
    expected = False
  
    assert actual == expected