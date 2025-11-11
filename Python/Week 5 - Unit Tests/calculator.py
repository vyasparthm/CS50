def main():
    
    while True:    
        try: 

                x = int(input('What is X: '))
                print('X squared is:', square(x))
                break
        except ValueError:
            print('Only integers are allowed!!')
            continue


def square(n):
    return n * n




if __name__ == '__main__':
    main()