''' 
  Python Crash Course by ERIC MATTHES 
 Program written by: Jagdeep Singh Brar 
 Program Name:  4-12. More Loops: All versions of foods.py in this section have avoided using
                for loops when printing to save space. Choose a version of foods.py, and
                write two for loops to print each list of foods.
'''
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are:")
for my_piz in my_foods:
    print(my_piz)
print("\nMy friend's favorite foods are:")
for fri_piz in friend_foods:
    print(fri_piz)