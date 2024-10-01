'''Extract Names

Jack was a little boy, who was playing the game word puzzle. The jack brother gave him a task to find the nouns in a given set of lines. Try to help jack to finish his task.


Problem Constraints:
Use the re  module for Regular Expression
Use the findAll method

Extract all names from the given text. Use metacharacter
Rules:
1) only alphabets
2) starts with upper-case
3) may contain surnames
4) may contain initials

Input format:
A single line input string consists of capitalized words in it.

Output format:
The output will be the words which are obeying the mentioned rules


Sample Input 1:
S.Vinoth Kumar and John Watson are friends with James
Sample output 1:
S.Vinoth Kumar 
John Watson 
James

Sample Input 2:
there were two friends named Sam and Jason
Sample output 2:
Sam
Jason'''
import re

def extract_names(text):
    # Regular expression pattern to match names
    pattern = r'\b[A-Z][a-z]*(?:\.[A-Z][a-z]*)*(?: [A-Z][a-z]*)*\b'
    # Find all matches in the input text
    matches = re.findall(pattern, text)
    return matches

# Sample Test
if __name__ == "__main__":
    input_text = input()
    names = extract_names(input_text)
    for name in names:
        print(name)
   