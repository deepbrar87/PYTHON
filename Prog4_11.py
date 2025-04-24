''' 
  Python Crash Course by ERIC MATTHES 
 Program written by: Jagdeep Singh Brar 
 Program Name: 4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1
                    (page 60). Make a copy of the list of pizzas, and call it friend_pizzas.
                    Then, do the following:
                • Add a new pizza to the original list.
                • Add a different pizza to the list friend_pizzas.
                • Prove that you have two separate lists. Print the message, My favorite
                pizzas are:, and then use a for loop to print the first list. Print the message,
                My friend’s favorite pizzas are:, and then use a for loop to print the second
                list. Make sure each new pizza is stored in the appropriate list.
'''
pizzas = ['Cheese Pizza', 'Pepproni Pizza', 'Spicy Chilly Pizza', 'Farm house Pizza']
friend_pizzas = pizzas[:]
pizzas.append('Sweet Pizza')
friend_pizzas.append('Corn Pizza')
print('My favorite pizzas are:, ')
print(pizzas)


print('My friend’s favorite pizzas are:,')
print(friend_pizzas)