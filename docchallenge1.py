import sys

print("Welcome to this program")
print("Enter any value any I will determine the data type")
print("Use exit to exit the program at any point of time")



def main():
  x = input("Enter something: ")
  if x == "exit":
    sys.exit()
  try:
    if type(eval(x)) == float: # If statement for float identification
        print(x, " is floating point number") # Print data type
    elif type(eval(x)) == int: # elif statement for integer identification
        print(x, " is interger number") # Print data type    
    elif type(eval(x)) == bool: # elif statement for bool identification
        print(x, " is a boolean") # Print data type  
  except:
    print("That is a string") # Print data type

while main:
  main()
