''' 
 Python Programs
 BY: Jagdeep Singh Brar 
 
 Program Name: Write a program that accept marks in 5 subject 
                and output average marks.
''' 
# Input marks of 5 subject
engMarks = float(input('Enter marks of English subject : '))
mathMarks = float(input('Enter marks of Mathematics subject : '))
sciencemarks = float(input('Enter marks of Science subject : '))
hindiMarks = float(input('Enter marks of Hindi subject : '))
computerMarks = float(input('Enter marks of Computer subject : '))
#Calcuate Average of subject
average = round(((engMarks+mathMarks+sciencemarks+hindiMarks+computerMarks)/5),2)
# Display Marks and Average of five subjects
print(f'''Marks of English : {engMarks} \nMarks of Mathematics : {mathMarks} \nMarks of Science : {sciencemarks}
      Marks of Hindi : {hindiMarks} \nMarks of Computer : {computerMarks} \nAverage marks of subject : {average}''')