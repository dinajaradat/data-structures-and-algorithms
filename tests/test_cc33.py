from cc33.left_join import left_join


def test_1():
   
    hashmap1 = {}
    hashmap2 = {}

    expected = []
    actual = left_join(hashmap1, hashmap2)

    assert expected == actual 

def test_2():
    
    hashmap1 = {}
    hashmap2 = {'diligent':'idle', 'fond':'averse', 'guide':'follow', 'flow':'jam', 'wrath':'delight'}
   
    expected = []
    actual = left_join(hashmap1, hashmap2)

    assert expected == actual 



def test_3():
   
    hashmap1 = {'diligent':'idle'}
    hashmap2 = {'fond':'averse', 'guide':'follow', 'flow':'jam', 'wrath':'delight'}

    expected = [['diligent','idle',None]]
    actual = left_join(hashmap1, hashmap2)

    assert expected == actual 



def test_4():

    hashmap1 = {'diligent':'employed', 'fond':'enamored', 'guide':'usher', 'outfit':'garb', 'wrath':'anger'}
    hashmap2 = {'diligent':'idle', 'fond':'averse', 'guide':'follow', 'flow':'jam', 'wrath':'delight'}


    expected = [['diligent', 'employed', 'idle'], ['fond', 'enamored', 'averse'], ['guide', 'usher', 'follow'], ['outfit', 'garb', None], ['wrath','anger', 'delight']]
    actual = left_join(hashmap1, hashmap2)

    assert expected == actual 