''' 
 Python Programs
 BY: Jagdeep Singh Brar 
 
 Program Name: Write a program to input a value in tonnes and 
               convert it into quintals and kilograms.
               (1 tonne - 10 quintal     1 tonne = 1000 kilograms, 1 quintal = 100 kilograms)
''' 
# Input a value in tonne by user
tonne = float(input('Enter a value in tonne :'))

# Convert value into quintal
quintal = round((tonne*10),3)

# Convert value into kilograms
kiloGram = round((tonne*1000),3)

# Display converted value
print(f'{tonne} tonne = {quintal} quintal')
print(f'{tonne} tonne = {kiloGram} kilograms')
