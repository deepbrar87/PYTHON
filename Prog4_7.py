''' 
  Python Crash Course by ERIC MATTHES 
 Program written by: Jagdeep Singh Brar 
 Program Name: 4-7. Threes: Make a list of the multiples of 3 from 3 to 30. Use a for loop to
                    print the numbers in your list.
'''
lst = [val for val in range(3,31,3)]
for num in lst:
    print(num)