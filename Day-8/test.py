import os

folder = input("please enter the  folders ith some space").split()

for i in folder:
    try:
        files = os.listdir(i)
    except FileNotFoundError:
        print("please provide a valid fodler name" + " " + i)
        continue

    for file in files:
        print(file)
    