'''Mails Per Hour


Write a program to read through the input.txt and find out the no.of mails by hour of the day for each of the messages.

Rule:
The file name should be input.txt.

Input format:
Give the input as a file .

Output format:
The output will be the hour (ascending order) and the number of mails received. Display the output in the console.

Sample Input file (input.txt):
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

From louis@media.berkeley.edu Fri Jan  4 18:10:48 2008

From zqian@umich.edu Fri Jan  4 16:10:39 2008

From rjlowe@iupui.edu Fri Jan  4 15:46:24 2008

From zqian@umich.edu Fri Jan  4 15:03:18 2008

Sample Output:
09 1
15 2
16 1
18 1

'''
#create input.txt to run below code
#copy the path and change all (\ ===> /)e.g C:\Users\DELL\OneDrive\Desktop\sample.txt to C:/Users/DELL/OneDrive/Desktop/sample.txt
#ready to run
def count_emails_per_hour(input_filename):
    try:
        hour_count = {}
        
        with open(input_filename, "r") as infile:
            for line in infile:
                if line.startswith("From "):
                    words = line.split()
                    time_str = words[5]  # Extract the time part (HH:MM:SS)
                    hour = time_str[:2]  # Extract the hour (HH)
                    
                    if hour in hour_count:
                        hour_count[hour] += 1
                    else:
                        hour_count[hour] = 1
        
        # Sort hours in ascending order
        sorted_hours = sorted(hour_count.items())
        
        # Print the result
        for hour, count in sorted_hours:
            print(f"{hour} {count}")
            
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    input_filename = "C:/Users/DELL/OneDrive/Desktop/persistent on bording course notes/OS UNIX COURSE/unix i design/input.txt"
    count_emails_per_hour(input_filename)
   