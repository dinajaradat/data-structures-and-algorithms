import pytest
from cc30.hashtable import HashTable

def test_set():
    hashtable1 = HashTable(1)
    actual = hashtable1.set("A", 70)
    expected = None

    assert expected == actual

def test_hash():
    hashtable1 = HashTable(1)
    hashtable1.set("A", 70)
    actual = hashtable1.hash("A")
    expected = 0

    assert expected == actual 
     

def test_get():
    hashtable1 = HashTable(1)
    hashtable1.set("A", 70)
    actual = hashtable1.get("A")
    expected = 70

    assert expected == actual 

def test_key():
    hashtable1 = HashTable(1)
    hashtable1.set("A", 70)
    actual = hashtable1.get("W")
    expected = None

    assert expected == actual 


def test_all_keys():
    hashtable1 = HashTable(1)
    hashtable1.set("A", 70)
    hashtable1.set("B", 90)
    hashtable1.set("C", 80)
    hashtable1.set("D", 95)
    hashtable1.set("E", 60)

    actual = hashtable1.keys()
    expected = ['A', 'B', 'C', 'D', 'E']

    assert expected == actual 

def test_collision():
    
    hashtable1 = HashTable(1)
    hashtable1.set("A", 70)
    hashtable1.set("B", 90)
    hashtable1.set("C", 80)
    hashtable1.set("D", 95)
    hashtable1.set("E", 60)

     
    actual = hashtable1.keys()
    expected = ['A', 'B', 'C', 'D', 'E']

    assert expected == actual



