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
def check_file_type(filename:str) -> str:
    filename = filename.lower().strip()

    #Simple dictionary to hold the different extension types
    media_types = {  ".gif'":"image/gif'"
                    ,".jpg":"image/jpg"
                    ,".jpeg":"image/jpeg"
                    ,".png":"image/png"
                    ,".pdf":"document/pdf"
                    ,".txt":"text file"
                    ,".zip":"compressed object"
                  }
    
    # Iterate through the loop to check if there is a match in media_types
    for ext,media_type in media_types.items():
        if filename.endswith(ext):
            return media_type
    #Default if not found in the Dictionary        
    return "application/octet-stream"
        
def main():
    user_input = input("What is your filename? ")
    print(f"The file you inserted is: {check_file_type(user_input)}")

if __name__ == "__main__":
    main()
