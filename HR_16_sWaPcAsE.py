''' 
 Python Programs in Hacker Rank 
 BY: Jagdeep Singh Brar 
 Program Description: 
 You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

For Example:

Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2  
'''
#

def swap_case(s):
    line = ''
    for char in s:
        if char.islower():
            line += char.upper()
        elif char.isupper():
            line += char.lower()
        else:
            line += char
    return line

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)