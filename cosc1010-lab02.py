# Jared Tolman
# UWYO COSC 1010
# 9/18/24
# Lab 02 
# Lab Section: 15
# Sources, people worked with, help given to: Lab TA

# Helpful personal notes
# In terminal window in the codespace (codespace clones the repository)
# git status
# git add "file name"
# git commit -m "commit message"
# git push
# To run file, type "python file name" in terminal window

your_variable_here = "when you see this, replace it with your code"

## Section ONE

# Complete the following print statement to print out "Hello, COSC1010"
print(f"Hello, COSC1010")

# Assign the string above to a variable named hello_message and print that variable
hello_message = f"Hello, COSC1010"
print(hello_message)

# Assign the string "cowboy joe" to a variable, and print that variable with title casing
CJ="cowboy joe"
print(CJ.title())

# Complete the following f-string print message 
    # You will need to create your own variables and insert them  
    # the final message should read `The University of Wyoming was founded in 1886`
a=f"University of Wyoming"
b=f"1886"
print(f"The {a} was founded in {b}")

# Now let's do some math with variables 
    # Create two variables x and y and assign them the values 5 and 10 respectively 
    # Complete the following print statements using your variables
    #All math must be done within the braces in the f-strings
x=5
y=10

print(f"x + y = {x+y}")
print(f"x - y = {x-y}")
print(f"x * y = {x*y}")
print(f"x / y = {x/y}")

# String concatenation 
    # Finally we will take a look at string concatenation
    # String concatenation combines two strings together
    # It is done using the + operator
    # Create three variables:
        # first_name, which is your first name 
        # last_name, which is your last name
        # space, which is a space character 
    # Use string concatenation to print out your full name 
first_name="Jared"
last_name="Tolman"
space=" "
print(f"{first_name}{space}{last_name}")