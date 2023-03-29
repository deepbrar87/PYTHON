''' 
 Python Programs for Class XI 
 BY: Jagdeep Singh Brar 
 
 Program Name: Write a program to input a single digit and 
                print a 3-digit number create as <n(n-1) (n-2)> 
             e.g. if your input is 7 then it should be 
                print 789 assume that the input  is in range one to 7.
''' 
num = int(input('Enter a number ( From 1 to 7) :'))
print(f'{num}{num+1}{num+2}')
