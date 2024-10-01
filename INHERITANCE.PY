class animals:
    def pets(self):
        print("Cat and Dog are pets")
class birds(animals):#without (animals) it is not possible to access the fun of animal class
    def fly(self):
        print("Birds can fly!")

obj=birds()
obj.pets()#because of inheritance we can accesss function of other class
obj.fly()