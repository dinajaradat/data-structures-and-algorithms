import pytest
from cc12.animal_Shelter import AnimalShelter
from cc12.animal_Shelter import animal

def test_enqueue_into_a_queue():

    animal1 = animal("cat","lila1")

    A1 = AnimalShelter()
    A1.enqueue(animal1)

    actual = str(A1)
    expected = "None <-- cat"
  
    assert actual == expected


def test_enqueue_multiple_values_into_queue():

    animal1 = animal("cat","lila1")
    animal2 = animal("cat","lila2")
    animal3 = animal("dog","dody1")
    animal4 = animal("dog","dody2")
    animal5 = animal("dog","dody3")

    A1 = AnimalShelter()
    A1.enqueue(animal1)
    A1.enqueue(animal2)
    A1.enqueue(animal3)
    A1.enqueue(animal4)

    actual = str(A1)
    expected = "None <-- dog <-- dog <-- cat <-- cat"
  
    assert actual == expected


def test_dequeue_out_first_value():

    animal1 = animal("cat","lila1")
    animal2 = animal("cat","lila2")
    animal3 = animal("dog","dody1")
    animal4 = animal("dog","dody2")
    animal5 = animal("dog","dody3")

    A1 = AnimalShelter()
    A1.enqueue(animal1)
    A1.enqueue(animal2)
    A1.enqueue(animal3)
    A1.enqueue(animal4)



    actual = A1.dequeue("cat")
    expected = "cat"
  
    assert actual == expected


def test_dequeue_out_one_value():

    animal1 = animal("cat","lila1")
    animal2 = animal("cat","lila2")
    animal3 = animal("dog","dody1")
    animal4 = animal("dog","dody2")
    animal5 = animal("dog","dody3")

    A1 = AnimalShelter()
    A1.enqueue(animal1)
    A1.enqueue(animal2)
    A1.enqueue(animal3)
    A1.enqueue(animal4)


    actual = A1.dequeue("dog")
    expected = "dog"
  
    assert actual == expected





def test_instantiate_an_empty_queue():

    A1 = AnimalShelter()

    actual = A1.is_empty()
    expected = True
  
    assert actual == expected


def test_dequeue_peek_on_empty_queue_raises_exception():

    A1 = AnimalShelter()

    with pytest.raises(Exception) as E:
        A1.dequeue("cat")
    assert str(E.value) == "Empty Queue"