''' 
 Python Programs
 BY: Jagdeep Singh Brar 
 
 Program Name: write a program to input two numbers and swap them ( Without using third variable)
''' 
# Ask user to input two integer number
num1 = int(input('Enter First number : '))
num2 = int(input('Enter Second number : '))

# Display number enterd by user
print('***** Number before swap are ******')
print('First Number enter by user is : ',num1)
print('Second Number enter by user is : ',num2)

# Swap values using third variable
num1, num2 = num2,num1

# Display Swap number
print('***** Number after swap are ******')
print('First Number after swap  is : ',num1)
print('Second Number after swap is : ',num2)