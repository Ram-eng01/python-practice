import sys


def addition(num1, num2):
    add = num1 + num2
    return add


def sub(num1, num2):
    s = num1 - num2
    return s

def multiplication(num1, num2):
    mul = num1 * num2
    return mul

num1 = float(sys.argv[1])
operation = sys.argv[2]
num2 = float(sys.argv[3])

if operation == "add":
    output = addition(num1,num2)
    print(output)