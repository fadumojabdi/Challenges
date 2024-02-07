from lib.most_often import MostOften

def test_empty_list_most_often():
    mostoften = MostOften([])
    mostoften.add_new("apple")
    mostoften.add_new("banana")
    mostoften.add_new("apple")
    mostoften.add_new("banana")
    mostoften.add_new("banana")
    result = mostoften.starting_list
    assert result == ["apple","banana", "apple", "banana", "banana"]

def test_mostoften_banana():
    mostoften = MostOften([])
    mostoften.add_new("apple")
    mostoften.add_new("banana")
    mostoften.add_new("apple")
    mostoften.add_new("banana")
    mostoften.add_new("banana")
    result = mostoften.get_most_often()
    assert result == "banana"

def test_mostoften_integer():
    mostoften = MostOften([])
    mostoften.add_new(1)
    mostoften.add_new(2)
    mostoften.add_new(1)
    mostoften.add_new(2)
    
    result = mostoften.get_most_often()
    assert result == "no clear winner"

def test_mostoften_mixed_with_integer_string():
    mostoften = MostOften([])
    mostoften.add_new(1)
    mostoften.add_new("banana")
    mostoften.add_new(2)
    mostoften.add_new(1)
    mostoften.add_new("banana")
    mostoften.add_new(1)
    result = mostoften.get_most_often()
    assert result == 1


def test_empty_list_most_often():
    mostoften = MostOften([])
    mostoften.add_new("apple")
    
    result = mostoften.get_most_often()
    assert result == "apple" 