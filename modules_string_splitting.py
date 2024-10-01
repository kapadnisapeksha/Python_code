'''Module: String Splitting
Akash wants to send a message to his colleague about his official team work. But he wants to maintain his message privacy, so he will encrypt his message and send that to his friend. Now his colleague wants to decode that message. Akash gave a hint to his colleague, like he has to decode his message by splitting his message with a particular character sent by him. Help Akash's colleague to decode the message by writing a program.

Input Format:
The first line of input consists of a string.
The next line of input consists of a character.

Output Format:
The output is a list of strings after splitting.
Every first letter of splitted word should be in capital.

Note: All text in bold corresponds to input and the rest corresponds to output.

Sample Input and Output 1:
aaahggghbbb
h
Strings after splitting
Aaa
Ggg
Bbb

Sample Input and Output 2:
ahhg&hcg&fhgf90
&
Strings after splitting
Ahhg
Hcg
Fhgf90'''
# Function to split the string and capitalize the first letter of each word
def split_and_capitalize(message, split_char):
    # Split the message by the specified character
    split_strings = message.split(split_char)
    # Capitalize the first letter of each substring
    capitalized_strings = [s.capitalize() for s in split_strings]
    return capitalized_strings

# Taking input for the message and the split character
message = input()
split_char = input()

# Get the split and capitalized strings
result = split_and_capitalize(message, split_char)

# Output the result
print("Strings after splitting")
for string in result:
    print(string)
   
