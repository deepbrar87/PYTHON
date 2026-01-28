''' 
 Python Programs
 BY: Jagdeep Singh Brar 
 
 Program Name: Write a program to input a value in kilometers and 
               convert it into miles(1 km = 0.621371 miles)
''' 
# Input a value of kilometers as float. 
kiloMeter = float(input('Input a value in kilometers :'))

# Convert kilometers to miles and use round() function to convert output into 02 decimal points.
miles = round((0.621371 * kiloMeter),2)

# Display result after conversion
print(f'{kiloMeter} km = {miles} miles')
