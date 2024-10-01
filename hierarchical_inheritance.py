#1 base class multiple derived class
class Calculator:
    def read(self):
        self.a=30
        self.b=20
class Addition(Calculator):
    def add(self):
        self.c=0
        self.c=self.a+self.b
        print(f"Addition is:-{self.c}")
class sub(Calculator):
    def sub(self):
       self.c=self.a-self.b
       print(f"Substraction is:-{self.c}")


obj=sub()
obj.read()

obj.sub()

obj2=Addition()
obj2.read()
obj2.add()
