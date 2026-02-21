x = 20  # Global variable

def another_function():
    print(x)  # This will access the global variable 'y'

another_function()
print(x)  # This will print 20