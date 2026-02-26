import sys

type = sys.argv[1]

if type == "t2.micro":
    print("ok we will create a instance for you of type:", type)
elif type == "t3.medium":
    print("ok we will create a instance for you of type:", type)
else:
    print("Sorry we can not create this type select t2.micro,t3,medium:", type)