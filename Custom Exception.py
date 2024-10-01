'''Custom Exception

Create a class named Student with a single attribute – marks.

Include a method named check_marks in the Student Class.

This method checks whether the marks is greater than  or equal to 90 and if it is greater than or equal to 90, the method returns True.

If the marks is less than 90, a custom Exception named NotEligibleException is raised and an appropriate message as shown in the sample output is displayed.

 

Create a custom Exception class named NotEligibleException.

 

Create an object of the student class and test the above methods.

 

Input and Output Format:

Refer Sample Input and Output for formatting specifications.

All text in bold corresponds to input and the rest corresponds to output.

 

Sample Input and Output 1:

Enter marks of student

98

Eligible

 

Sample Input and Output 2:

Enter marks of student

56

Inside Except Block : Not Eligible

 '''
class NotEligibleException(Exception):
    pass
class Student:
    std_marks=None 
    def check_marks(self):
        try:
            self.marks=int(input("Enter marks of student"))
            if self.marks>=90:
                print("Eligible")
            else:
                raise NotEligibleException
        except NotEligibleException:
            print("Inside Except Block : Not Eligible")

student=Student()
student.check_marks()