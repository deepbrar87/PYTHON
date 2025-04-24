''' 
  Python Crash Course by ERIC MATTHES 
 Program written by: Jagdeep Singh Brar 
 Program Name: 4-9. Cube Comprehension: Use a list comprehension to generate a list of the
first 10 cubes.
'''
lst = [val**3 for val in range(1,11)]
for num in lst:
    print(num)