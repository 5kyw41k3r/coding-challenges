x = input("Enter something: ")
# Ask for user input
try:
    if type(eval(x)) == float: # If statement for float identification
        print(x, " is floating point number") # Print data type
    elif type(eval(x)) == int: # elif statement for integer identification
        print(x, " is interger number") # Print data type    
    elif type(eval(x)) == bool: # elif statement for bool identification
        print(x, " is a boolean") # Print data type  
except:
    print("That is a string") # Print data type
