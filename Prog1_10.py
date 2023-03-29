''' 
 Python Programs
 BY: Jagdeep Singh Brar 
 
 Program Name: write a program to input two numbers and swap them ( Using third variable)
''' 
# Ask user to input two integer number
num1 = int(input('Enter First number : '))
num2 = int(input('Enter Second number : '))

# Display number enterd by user
print('***** Number before swap are ******')
print('First Number enter by user is : ',num1)
print('Second Number enter by user is : ',num2)

# Swap values using third variable

num3 = num1   # Store first number in third variable
num1 = num2   # Assign second number to first variable
num2 = num3   # Assign first number to second variable

# Display Swap number
print('***** Number after swap are ******')
print('First Number after swap  is : ',num1)
print('Second Number after swap is : ',num2)

