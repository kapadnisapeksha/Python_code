'''Student Details - Lambda Expression 5
 

Write a program to enter the 'N' number of student's detail. All the details are in one line, separated by a comma. Print all the details in sorted order by student's name, by using the Lambda function.
 

Input Format:

The first line of input is an integer, which corresponds to the number of students 'n'.

The next 'n' lines of inputs are string, which corresponds to the student's details separated by comma[, ]  (Name, Roll Number, CGPA).


Output Format:

The output consists of item type details sorted by the student's name, lambda function.

Refer to sample output for formatting specifications.

[All text in bold corresponds to input and rest corresponds to output] 
 

Sample Input and Output: 

Enter the number of students:

3

Vikram,101,8.5

Peter,401,8.9

Amit,701,7.6

Name,Roll Number,CGPA

Amit,701,7.6
Peter,401,8.9
Vikram,101,8.5

Problem Requirements:
Python3'''
def student_details():
    # Read number of students
    n = int(input("Enter the number of Students\n"))
    
    # Read student details
    students = []
    for _ in range(n):
        details = input().strip()
        students.append(details.split(','))

    # Sort the students by name using lambda
    students_sorted = sorted(students, key=lambda student: student[0].strip())

    # Print header
    print("Name,Roll Number,CGPA")
    
    # Print sorted student details
    for student in students_sorted:
        print(",".join(student))

# Run the function
student_details()