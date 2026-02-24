'''
In a file called extensions.py, implement a program that prompts the user for the name of a file and then outputs that file's media type if the file's name ends, case-insensitively, in any of these suffixes:

    .gif
    .jpg
    .jpeg
    .png
    .pdf
    .txt
    .zip
If the file's name ends with some other suffix or has no suffix at all, output application/octet-stream instead, which is a common default.
'''

def check_file_type(extn:str)->str:
    extn_clean = extn.lower().strip()
    if extn_clean.endswith('.gif'):
        return 'image/gif'
    elif extn_clean.endswith('.jpg'):
        return 'image/jpg'
    elif extn_clean.endswith('.jpeg'):
        return 'image/jpeg'
    elif extn_clean.endswith('.jpeg'):
        return 'image/jpeg'
    elif extn_clean.endswith('png'):
        return 'image/png'
    elif extn_clean.endswith('.pdf'):
        return 'document/pdf'
    elif extn_clean.endswith('.txt'):
        return 'text file'
    elif extn_clean.endswith('.zip'):
        return 'compressed object'
    else:
        return 'application/octet-stream'
    
def main():
    user_input = input('Enter the file name: ')
    print(f"The file:{user_input} is: {check_file_type(user_input)}")

if __name__ == '__main__':
    main()