import pytest
from binary import Binary_Search

def test_0():
    actual=Binary_Search([],5)
    expected=-1
    assert actual == expected


def test_1():
    actual=Binary_Search([4, 8, 15, 16, 23, 42],15)
    expected=2
    assert actual == expected

def test_2():
    actual=Binary_Search([-131, -82, 0, 27, 42, 68, 179],42)
    expected=4
    assert actual == expected

def test_3():
    actual=Binary_Search([11, 22, 33, 44, 55, 66, 77],99)
    expected=-1
    assert actual == expected