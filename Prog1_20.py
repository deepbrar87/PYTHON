''' 
 Python Programs
 BY: Jagdeep Singh Brar 
 
 Program Name: Write a program that asks for your height in centimetres 
                and then converts your height to feet and inches. 
                (1 feet = 12 inches, 1 inch to 2.54 cm).
''' 
# Input height in centimeters
height_CM = int(input("Enter your height in centimeters : "))
# Convert height into feet and inch
height_Inch = height_CM / 2.54
height_Feet  =int(height_Inch//12)
height_Inch = int(height_Inch%12)
# Display height in feet and inch
print(f'Your Height is : {height_Feet}\' {height_Inch}\"')