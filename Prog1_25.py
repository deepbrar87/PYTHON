''' 
 Python Programs for Class XI 
 BY: Jagdeep Singh Brar 
 
 Program Name: Write a program to read details like name, class and age of student
             and then print its details firstly in same line and then in separate lines. 
            Make sure you have used two black line in these two different types of prints.
''' 
# Ask user to enter Name, Class and Age
name = input('Enter your name : ')
classs = int(input('Enter your class : '))
age =  int(input('Enter your age : '))

print(f'Name : {name} Class : {classs} Age : {age} \n\n\nName : {name} \nClass : {classs} \nAge : {age} ')
