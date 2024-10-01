

'''5. Write a program that will reverse a four digit number.Also it checks whether the reverse is true'''
def reverfun():
    four_digi=int(input("Enter the four digit number:-"))
    rever_digi=int(str(four_digi)[::-1])
    return rever_digi



obj=reverfun()
print(obj)
