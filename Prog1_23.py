''' 
 Python Programs
 BY: Jagdeep Singh Brar 
 
 Program Name: Write a program to compute simple intrest and compound intrest.
''' 
# Ask user to input Principal amount, rate and time 
principal = float(input('Enter principal amount : '))
rate = float(input('Enter rate of intrest : '))
time = int(input('Enter time in month : '))
# Calculate Simple intrest and Compound intrest
SI = round(((principal*rate*(time/12))/100),2)
timeYear = time/12
CI = round((principal*((1+(rate/100))**timeYear)),2)
# Display Simple intrest and Comound intrest
print(f'Simple Intrest : {SI} \nCompound Intrest : {CI}')
