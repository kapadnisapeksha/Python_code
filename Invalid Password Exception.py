'''CustomException: Invalid Password Exception
Vicky's father wants to create the whatsApp account. But again and again Invalid Password error comes. So Vicky helps his father to create a account. During account creation he has enter the username and password, in which the password should be contain atleast one lowercase letter, one upper case letter and a number, otherwise exception occured.
So write a program to check the password is valid or invalid.

Note:
Conditions for a valid password: 
Password should contain atleast one lowercase letter, one upper case letter and a number. 
Use exception handling mechanisms to handle these exceptions 
 
Input and Output Format: 
Refer sample input and output for formatting specifications. 
All text in bold corresponds to input and the rest corresponds to output. 

Sample Input and Output 1 : 
Enter the username
Vikram
Enter the password 
1samudrA
Employee Username: Vikram
Password: 1samudrA

Sample Input and Output 2 : 
Enter the username 
Rashmi
Enter the password 
hawai
CustomException: Invalid Password Exception
'''
class InvalidPasswordException(Exception):
    pass

def check_password(password):
    if (not any(c.islower() for c in password) or
        not any(c.isupper() for c in password) or
        not any(c.isdigit() for c in password)):
        raise InvalidPasswordException("CustomException: Invalid Password Exception")

def create_account():
    try:
        username = input("Enter the username\n")
        password = input("Enter the password\n")
        check_password(password)
        print(f"Employee Username: {username}")
        print(f"Password: {password}")
    except InvalidPasswordException as e:
        # Count occurrences of 'CustomError' in the exception message
        count_custom_error = e.args[0].count('CustomException')
        if count_custom_error >= 1 and count_custom_error <= 3:
            print(e)
        else:
            raise  # Reraise the exception if the count is outside the expected range

# Call the function to create the account
create_account()
