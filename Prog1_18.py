''' 
 Python Programs 
 BY: Jagdeep Singh Brar 
 
 Program Name: Write a Python program that accepts radius of a circle
             and print its area.
''' 
# Ask user to enter radius of circle
radius = float(input('Enter a radius of circle :'))

# Calculate area of circle
area = round(3.14*(radius**2),2)

# Display area of circle
print('Area of circle : ', area)