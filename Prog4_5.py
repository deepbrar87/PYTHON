''' 
  Python Crash Course by ERIC MATTHES 
 Program written by: Jagdeep Singh Brar 
 Program Name: 4.5 : Summing a Million: Make a list of the numbers from one to one million,
                    and then use min() and max() to make sure your list actually starts at one and
                    ends at one million. Also, use the sum() function to see how quickly Python can
                    add a million numbers.
'''
sum = 0
lst = [num for num in range(1,1000001)]
print(min(lst))
print(max(lst))
for val in lst:
    sum = sum + int(val)

print(sum)