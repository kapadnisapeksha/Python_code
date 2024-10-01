"""One-to-One Relationship – 1 (Unidirectional)

Create a class named Address with the following private_attributes

__street

__city

__state

 

Include a constructor

__init__(self, street, city, state)

 

Include a method

__str__(self)

This method returns a string corresponding to Address details in the format specified

in the sample output.

 

Create a class named Person with the following private_attributes

__name

__age

__address (of type Address)

 

Include a constructor

__init__(self, name, age, address)

 

Include a method

__str__(self)

This method returns a string corresponding to Person details in the format specified

in the sample output.

 

Create objects of the above classes and test them.

 

Input and Output Format:

Refer Sample Input and Output for formatting specifications.

 

Sample Input and Output 1:

[All text in bold corresponds to input and the rest corresponds to output]

 

Enter name

Mahirl

Enter age

10

Enter address

Enter street

LMC Street

Enter city

Salem

Enter state

Tamilnadu

Person Details

Mahirl is a person who is 10 years old and lives in the following address : LMC Street , Salem , Tamilnadu

 """

class Address:
    def __init__(self,city,street,state):
        self.__city=city
        self.__street=street
        self.__state=state

    def __str__(self):
        return f"{self.__city},{self.__street},{self.__state}"
    
class Person(Address):
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
    def __str__(self):
        return f"{self.__name} is a person who is {self.__age} years old and lives in thr following address:"
    

city=input("Enter the name of city:")
street=input("Enter the street:")
state=input("Enter the state")

name=input("Enter the name:")
age=int(input("Enter the age:"))
p=Person(name,age)
p

