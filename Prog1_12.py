''' 
 Python Programs
 BY: Jagdeep Singh Brar 
 
 Program Name: Write a program to input three numbers and swap them 
                as this first number becomes the 2nd number, 
                2nd number become as the 3rd number and 
                3rd number become the first number.
''' 
# Ask user to input three integer number
num1 = int(input('Enter First number : '))
num2 = int(input('Enter Second number : '))
num3 = int(input('Enter Third number : '))

# Display number enterd by user
print('***** Number before swap are ******')
print('First Number enter by user is : ',num1)
print('Second Number enter by user is : ',num2)
print('Third Number enter by user is : ',num3)

# Swap values using third variable
num2,num3,num1 = num1,num2,num3

# Display Swap number
print('***** Number after swap are ******')
print('First Number after swap  is : ',num1)
print('Second Number after swap is : ',num2)
print('Third Number after swap is : ',num3)