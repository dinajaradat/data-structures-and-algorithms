from cc31.repeated_word import repeated_word

def test_1():
    str = " "
    actual = repeated_word(str)
    expected = None

    assert expected == actual 

def test_2():
    str = "Once upon a time, there was a brave princess who..."
    actual = repeated_word(str)
    expected = "a"

    assert expected == actual 

def test_3():
    str = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."
    actual = repeated_word(str)
    expected = "it"

    assert expected == actual 

def test_4():
    str = "It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."
    actual = repeated_word(str)
    expected = "summer"

    assert expected == actual 