from madlib_cli.madlib import getKeys
from madlib_cli.madlib import user_input
from madlib_cli.madlib import returnKeys


def test_getKeys():
    actual = getKeys('{Adjective}')
    expected = 'Adjective'
    assert actual == expected

def test_userinput():
    actual = user_input('Adjective')
    expected = 'Adjective'
    assert actual == expected

def test_returnKeys():
    actual = returnKeys('Dinosaur')
    expected = 'Dinosaur'
    assert actual == expected