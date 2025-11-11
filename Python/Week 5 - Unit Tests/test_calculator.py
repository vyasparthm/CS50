from calculator import square

def main():
    test_square()


def test_square():
    ## If Else till the end of time?
    # if square(2) != 4:
    #     print('Error! test failed for 2, squared value was not 4')
    # elif square(2) == 4:
    #     print(f'It works, Passed for 2, {square(2)}')

    ## Assert
    try:
        assert square(2) == 4, "square(2) should equal 4"
    except AssertionError as e:
           print(f'AssertionError Error occured: {e}')        
    try:
        assert square(3) == 9, "square(3) should equal 9"
    except AssertionError as e:
       print(f'AssertionError Error occured: {e}')        
    try:       
        assert square(4) == 16, "square(4) should equal 16"
    except AssertionError as e:
       print(f'AssertionError Error occured: {e}')        
    try:
        assert square(-2) == 4, "square(-2) should equal 4"
    except AssertionError as e:
           print(f'AssertionError Error occured: {e}')                
   



if __name__ == '__main__':
    main()