''' 
 Python Programs
 BY: Jagdeep Singh Brar 
 
 Program Name: Write a program to read 3 numbers in 3 variable 
                and swap first two variable with sum of first 
                and second, second and third number respectively.
''' 
# Ask user to input three integer number
num1 = int(input('Enter First number : '))
num2 = int(input('Enter Second number : '))
num3 = int(input('Enter Third number : '))

# Display number enterd by user
print('***** Number are ******')
print('First Number enter by user is : ',num1)
print('Second Number enter by user is : ',num2)
print('Third Number enter by user is : ',num3)

# Swap values using third variable
num1,num2 = num1+num2,num2+num3

# Display Swap number
print('***** Number after swap are ******')
print('First Number after swap  is : ',num1)
print('Second Number after swap is : ',num2)
print('Third Number after swap is : ',num3)