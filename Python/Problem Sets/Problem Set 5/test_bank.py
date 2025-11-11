'''
In a file called test_bank.py, implement three or more functions that collectively test your implementation of value thoroughly, each of whose names should begin with test_ so that you can execute your tests with:

pytest test_bank.py
'''

from bank import verifyGreeting

def test_First_Letter():
    assert verifyGreeting("Hi there") == '$20 for you'
    assert verifyGreeting("Hi Bro") == '$20 for you'
    assert verifyGreeting("Hey How's it going?") == '$20 for you'

def test_for_Hello():
    assert verifyGreeting("Hello there") == '$0 for you'
    assert verifyGreeting("Hello friend") == '$0 for you'
    assert verifyGreeting("Hello amigo") == '$0 for you'

def test_no_Hello_or_H():
    assert verifyGreeting("Que paso Amigo") == '$100 for you'
    assert verifyGreeting("Good day so far?") == '$100 for you'