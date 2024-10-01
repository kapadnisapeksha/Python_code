#multiple inheritance 2 base class 1 child class
class Calculator:
    def read(self):
        self.a=30
        self.b=20
class Addition():
    def add(self):
        self.c=0
        self.c=self.a+self.b
        print(f"Addition is:-{self.c}")
class sub(Addition,Calculator):
    def sub(self):
       self.c=self.a-self.b
       print(f"Substraction is:-{self.c}")


obj=sub()
obj.read()
obj.add()
obj.sub()
