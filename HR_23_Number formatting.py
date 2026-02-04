''' 
 Python Programs in Hacker Rank 
 BY: Jagdeep Singh Brar 
 Program Description: 
 Given an integer, n, print the following values for each i integer 1 from N to :
    1. Decimal
    2. Octal
    3. Hexadecimal (capitalized)
    4. Binary
'''
#

def print_formatted(number):
    width = len(bin(number))-2
    for i in range(1,number+1):
        print(f'{i:{width}d} {i:{width}o} {i:{width}X} {i:{width}b}')

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)