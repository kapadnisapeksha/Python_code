'''Admin Roles - Lambda Expression 1
 

A Lab manager wants to know the respective roles of the person in an ABC degree college. When he enters the person designation, then all their roles should be printed. So help him by writing a program using lambda function.
Write a program to enter the designation of a person as "Admin", "Teacher", or "Student", and print their respective roles.

Note: Use only the lambda function.

Below are the respective roles for the designation:
1) Admin roles:
     - Login
     - Logout
     - resetPassword
     - createUser
2) Teacher roles:
     -  Login

     - Logout

    - postResults

    - attendanceReport

3) Student roles:
     - Login

     - Logout

    - takeTest


Input Format:
Input consists of an integer value for menu choice as described in Sample Output.

Print ''Wrong Choice" when the user enters the invalid choice.

Output Format:
The output consists of strings as roles for respective designation.
[All the bold letters correspond to Input and rest corresponds to output]

Sample Input and Output 1:

1. Admin

2. Teacher

3. Student

Enter your choice:

1
Login

Logout

resetPassword

createUser

Sample Input and Output 2:

1. Admin

2. Teacher

3. Student

Enter your choice:
4
Wrong Choice'''
def display_roles():
    # Define roles using a dictionary
    roles = {
        1: ["Login", "Logout", "resetPassword", "createUser"],
        2: ["Login", "Logout", "postResults", "attendanceReport"],
        3: ["Login", "Logout", "takeTest"]
    }

    # Lambda function to print roles
    print_roles = lambda role_list: list(map(lambda role: print(role), role_list))
    
    # Lambda function to get roles
    get_roles = lambda choice: roles.get(choice, "Wrong Choice")
    
    # Lambda function to validate input
    validate_input = lambda input: int(input) if input.isdigit() else "Wrong Choice"
    
    # Display menu
    print("1. Admin")
    print("2. Teacher")
    print("3. Student")
    
    # Get user input
    choice_input = input("Enter your choice:\n")
    choice = validate_input(choice_input)
    
    if choice == "Wrong Choice":
        print(choice)
    else:
        result = get_roles(choice)
        if result == "Wrong Choice":
            print(result)
        else:
            print_roles(result)

# Run the function
display_roles()