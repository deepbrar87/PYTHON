''' 
  Python Crash Course by ERIC MATTHES 
 Program written by: Jagdeep Singh Brar  
 Program Name: 4-13. Buffet: A buffet-style restaurant offers only five basic foods. Think of five
                    simple foods, and store them in a tuple.
                    • Use a for loop to print each food the restaurant offers.
                    • Try to modify one of the items, and make sure that Python rejects the change.
                    • The restaurant changes its menu, replacing two of the items with different
                    foods. Add a block of code that rewrites the tuple, and then use a for
                    loop to print each of the items on the revised menu.
'''
menu = ('Shahi Panner','Chiken Masala','Daal','Butter roti')
print(menu)

#menu[2] = 'Butter Daal'
#print(menu)

menu = ('Shahi Panner','Chiken Masala','Butter Daal','Butter roti', 'Butter Naan')
for item in menu:
    print(item)