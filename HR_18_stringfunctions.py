''' 
 Python Programs in Hacker Rank 
 BY: Jagdeep Singh Brar 
 Program Description: 
 Python has built-in string validation methods for basic data.
   It can check if a string is composed of alphabetical characters, alphanumeric characters, digits, etc.
'''
#
if __name__ == '__main__':
    s = input()
    alnum = digit = alpha = lower = upper = False
    for char in s:
        if char.isalnum(): 
            alnum = True 
        if char.isalpha(): 
            alpha = True
        if char.isdigit(): 
            digit = True
        if char.islower(): 
            lower = True
        if char.isupper(): 
            upper = True
    print(alnum)
    print(alpha)
    print(digit)
    print(lower)
    print(upper)
    