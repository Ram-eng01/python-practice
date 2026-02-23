import sys

#sys.argv contains the list of command line arguments

print("Script Name:", sys.argv[0])
if len(sys.argv) > 1 :
    print("ARGUMENT PASSED:", sys.argv[1:]) 
else:
    print("No arguments passed.")