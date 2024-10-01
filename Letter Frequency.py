'''Letter Frequency
Prakash is the English school teacher at Aksh public school. He wants to teach the English characters to the 1st class students. After taking the class he wanted to know whether his students recognize the letters of English alphabet. So he gave his students a English sentence, and asked them to write down the count of each character in alphabatical order.
 
Help the students to find the count by writing a program that builds a frequency listing of the characters contained in the file, and prints a sorted and formatted character frequency table to the screen.
 
Note:
Read the input from the file and print the output in the console.  
Input File should be named as frequencyFile.txt.
 
Input File Content:
Set of words (or sentences).  
 
Output Format:  
Print a sorted and formatted character frequency table. 

Sample Input and Output: 
b: 1
i: 1
n: 2
o: 2
r: 1
t: 1
w: 1'''


def count_character_frequency(input_filename):
    try:
        # Initialize an empty dictionary to store character frequencies
        char_frequency = {}

        # Read the input file
        with open(input_filename, "r") as infile:
            content = infile.read()

        # Count frequencies of each character (convert to lowercase first)
        for char in content:
            if char.isalpha():  # Consider only alphabetic characters
                char_lower = char.lower()  # Convert character to lowercase
                if char_lower in char_frequency:
                    char_frequency[char_lower] += 1
                else:
                    char_frequency[char_lower] = 1

        # Sort characters alphabetically
        sorted_chars = sorted(char_frequency.items())

        # Print the sorted and formatted character frequency table
        for char, count in sorted_chars:
            print(f"{char}: {count}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    input_filename = "frequencyFile.txt"
    count_character_frequency(input_filename)
