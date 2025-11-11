import plates as p

def test_check_len():
    assert p.check_len('Halo10') == True
    assert p.check_len('EBP162') == True

def test_starts_with():
    assert p.starts_with('EBp162') == True   
    assert p.starts_with('HiHelo') == True

def test_numbers_middle():
    assert p.numbers_middle('AAA333') == True   
    assert p.numbers_middle('AAA325') == True   
    assert p.numbers_middle('AAA33a') == False   
    assert p.numbers_middle('1AA33a') == False   

def test_non_alpha_numeric():
    assert p.non_alpha_numeric('123456') == True
    assert p.non_alpha_numeric('AA3456') == True
    assert p.non_alpha_numeric('Hello World') == False
    

