import os

def list_files():
    folders = input("Enter the folder names").split()

    for folder in folders:
        try:
            files = os.listdir(folder)
        except FileNotFoundError:
            print("Enter a valid folder names" + folder)
            continue
        for file in files:
            print(file)

list_files()


#Steps:
#-	Taking the user input using input()
#-	Listing the files & folders using the for loop
#-	Using OS module
#-	Print the output
#-	Handling the known errors using try & except 