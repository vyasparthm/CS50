'''
In a file called extensions.py, implement a program that prompts the user for the name of a file and then outputs that file’s media type if the file’s name ends, case-insensitively, in any of these suffixes:

    .gif
    .jpg
    .jpeg
    .png
    .pdf
    .txt
    .zip
If the file’s name ends with some other suffix or has no suffix at all, output application/octet-stream instead, which is a common default.
'''

def main():
    filename = str(input('Enter File Name: ').lower())
    extnfinder(filename)

def extnfinder(file):
    if file.endswith('.gif'):
        print('This is a "gif" file')
    elif file.endswith('jpg') or file.endswith('jpeg'):
        print('This is a "jpg/jpeg" file')
    elif file.endswith('.png'):
        print('This is a "png" file')
    elif file.endswith('.pdf'):
        print('This is a "pdf" file')
    elif file.endswith('.txt'):
        print('This is a "txt" file')
    elif file.endswith('.zip'):
        print('This is a "zip" file')
    else:
        print('This seems to be: application/octet-stream')

if __name__ == '__main__':
    main()