''' 
 Python Programs
 BY: Jagdeep Singh Brar 
 
 Program Name: Write a program to input a number and print its cube.
''' 
# Take a number from user as integer
num1 = int(input("Enter a number to find cube :"))

# Calculate cube of given number
cube = num1*num1*num1 # Method 1 
cube = num1**3        # Method 2

#Display cube of given number
print(f'Cube of {num1} is : {cube}')