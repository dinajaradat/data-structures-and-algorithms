import pytest
from cc10.Stack import Stack
from cc10.Queue import Queue

def test_push_onto_a_stack():

    S = Stack()

    S.push(1)

    actual = str(S)
    expected = "1 --> None"
  
    assert actual == expected

def test_push_multiple_values_stack():

    S = Stack()

    S.push(1)
    S.push(2)
    S.push(3)
    S.push(4)


    actual = str(S)
    expected = "4 --> 3 --> 2 --> 1 --> None"
  
    assert actual == expected

def test_pop_off_the_stack():

    S = Stack()

    S.push(1)
    S.push(2)
    S.push(3)
    S.push(4)

    actual = S.pop()
    expected = 4
  
    assert actual == expected

def test_empty_stack_after_multiple_pops():

    S = Stack()

    S.push(1)
    S.push(2)
    S.push(3)
    S.push(4)
    S.pop()
    S.pop()
    S.pop()
    S.pop()

    actual = S.is_empty()
    expected = True
  
    assert actual == expected


def test_peek_the_next_item_on_the_stack():

    S = Stack()

    S.push(1)
    S.push(2)
    S.push(3)
    S.push(4)
    S.pop()


    actual = S.peek()
    expected = 3
  
    assert actual == expected


def test_instantiate_an_empty_stack():

    S = Stack()

    actual = S.is_empty()
    expected = True
  
    assert actual == expected


def test_pop_peek_on_empty_stack_raises_exception():

    S = Stack()

    with pytest.raises(Exception) as E:
        S.pop()
    assert str(E.value) == "Empty stack"

    with pytest.raises(Exception) as E:
        S.peek()
    assert str(E.value) == "Empty stack"


def test_enqueue_into_a_queue():

    Q = Queue()

    Q.enqueue(1)

    actual = str(Q)
    expected = "None <-- 1"
  
    assert actual == expected


def test_enqueue_multiple_values_into_queue():

    Q = Queue()

    Q.enqueue(1)
    Q.enqueue(2)
    Q.enqueue(3)
    Q.enqueue(4)

    actual = str(Q)
    expected = "None <-- 4 <-- 3 <-- 2 <-- 1"
  
    assert actual == expected


def test_dequeue_out_expected_value():

    Q = Queue()

    Q.enqueue(1)
    Q.enqueue(2)
    Q.enqueue(3)
    Q.enqueue(4)

    actual = Q.dequeue()
    expected = 1
  
    assert actual == expected


def test_peek_into_a_queue():

    Q = Queue()

    Q.enqueue(1)
    Q.enqueue(2)
    Q.enqueue(3)
    Q.enqueue(4)

    actual = Q.peek()
    expected = 1
  
    assert actual == expected


def test_empty_queue_after_multiple_dequeues():

    Q = Queue()

    Q.enqueue(1)
    Q.enqueue(2)
    Q.enqueue(3)
    Q.enqueue(4)

    Q.dequeue()
    Q.dequeue()
    Q.dequeue()
    Q.dequeue()

    actual = Q.is_empty()
    expected = True
  
    assert actual == expected


def test_instantiate_an_empty_queue():

    Q = Queue()

    actual = Q.is_empty()
    expected = True
  
    assert actual == expected


def test_dequeue_peek_on_empty_queue_raises_exception():

    Q = Queue()

    with pytest.raises(Exception) as E:
        Q.dequeue()
    assert str(E.value) == "Empty Queue"

    with pytest.raises(Exception) as E:
        Q.peek()
    assert str(E.value) == "Empty Queue"