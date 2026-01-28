''' 
 Python Programs
 BY: Jagdeep Singh Brar 
 
 Program Name: Program to calculate BMI of a person.
To calculate BMI Weight/Height*Height
''' 
# Ask your to enter Weight and height
weight_in_kg = float(input("Enter weight in kg :"))
height_in_meter = float(input("Enter height in meter : "))

#Calculate BMI of person
bmi = round(weight_in_kg/(height_in_meter**2),2)

# Display weight and height of person in formmated text
print(f'Weight enterd by person is :{weight_in_kg}kg and height  :{height_in_meter}m ')

# \u00b to write superscript 
print(f'BMI of person is : {bmi} kg/m\u00b2')
