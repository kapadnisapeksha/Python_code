'''Regex- Password validation


ABX company asking for applying for the jobs from 2017 batch students. So company people released the Online application form for application. So Interested students can go for that link and can provide all the details. So Each student has to create an account through that link.
So for creating the Account they have to provide their valid mail Id and password.

So They have provided some rules for creating a valid password.
That is, the password should contain at least 8 characters including special characters[ _@$#%!&], uppercase and lowercase letters.

Problem Constraints:
Use regex methods for validating.
Use re module.

Input and Output Format:
Input is a string that indicates a password.
The output contains a string indicates whether the password is valid or not. ( Refer to sample output format).

Note: All text in bold corresponds to the input and the rest corresponds to output.

Sample Input and Output 1:
Abc123$
Not a Valid Password

Sample Input and Output 2:
sand$hhAAA
Valid Password'''
import re

def validate_password(password):
    # Regular expression to match the password criteria
    pattern = re.compile(
        r'^(?=.*[a-z])'        # At least one lowercase letter
        r'(?=.*[A-Z])'         # At least one uppercase letter
        r'(?=.*[_@$#%!&])'     # At least one special character
        r'.{8,}$'              # At least 8 characters long
    )
    
    if re.fullmatch(pattern, password):
        return "Valid Password"
    else:
        return "Not a Valid Password"

# Sample Test
if __name__ == "__main__":
    password = input()
    result = validate_password(password)
    print(result)
   