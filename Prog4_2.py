''' 
  Python Crash Course by ERIC MATTHES 
 Program written by: Jagdeep Singh Brar 
 Program Name: 4-2. Animals: Think of at least three different animals that have a common characteristic.
                    Store the names of these animals in a list, and then use a for loop to
                    print out the name of each animal.
                • Modify your program to print a statement about each animal, such as
                    A dog would make a great pet.
                • Add a line at the end of your program stating what these animals have in
                    common. You could print a sentence such as Any of these animals would
                    make a great pet!
'''
animal = ['Dog', 'Cat','Cow']

for ani in animal:
    print(ani)

for ani in animal:
    print('A '+ ani + ' would make a great pet.')
print('Care and love them !')