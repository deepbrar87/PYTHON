''' 
 Python Programs 
 BY: Jagdeep Singh Brar 
 
 Program Name: Write a program with maximum three lines of code and 
        assign first 5 multiples of a number to five variable and then print them.
''' 
# Ask user to enter a number
num = int(input('Enter a number : '))

# Calculate first five multiple of given number
num1 ,num2,num3,num4,num5 = num*1 ,num*2, num*3, num*4, num*5

# Display result 
print(f'Number enterd by user : {num} \nFirst five multiple are : {num1}, {num2}, {num3}, {num4}, {num5}')