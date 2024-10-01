'''create new file "practise.txt" using python 
Add following datain it:
Hi everyone
We are learning file i/o
using java
i like programing java 
1. WAF that replace all occurence of python with java 
2.search if "learning" found in file or not 
3.WAF to find in which line of the file does the word "Learning" occur first print -1 if word not foud
'''
with open("Practise.txt","w")as f:
    f.write("Hi everyone\nWe are learning file i/o\nusing java\ni like programing java ")

#1. WAF that replace all occurence of python with java 

    
def Word_repalce():
    with open("Practise.txt","r")as f:
        data=f.read()
        new_data=data.replace("java","Python")
        print(new_data)

    with open("Practise.txt","w")as f:
        f.write(new_data)


Word_repalce()

#2.search if "learning" found in file or not 

def check_word():
    word="learning"
    with open ("Practise.txt","r")as f:
        data=f.read()
        if(data.find(word) != -1):
            print("Found")
        else:
            print("Not Found")

check_word()


#3.WAF to find in which line of the file does the word "Learning" occur first print -1 if word not foud
def check_line_of_word():
        word="learning"
        data=True
        line_no=1
        with open("Practise.txt","r")as f:
            while data:
                data=f.readline()
                if(word in data):
                    print(line_no)
                    
                    line_no += 1

        return -1
print(check_line_of_word())

    

        
        
