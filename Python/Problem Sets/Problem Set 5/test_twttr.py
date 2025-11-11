'''
In a file called twttr.py, reimplement Setting up my twttr from Problem Set 2, restructuring your code per the below, wherein shorten expects a str as input and returns that same str but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.
'''

from twttr import shorten_string

def test_shorten_string_Manual():
    assert shorten_string("Hello Parth") == 'hll prth'
    assert shorten_string("I am Twitter") == ' m twttr'
    assert shorten_string("I am test of a,e,i,o,u") == ' m tst f ,,,,'
    

