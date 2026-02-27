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