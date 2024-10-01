class birthyear():
    def input(self):
        self.a=int(input("Enter the birth date:-"))
        self.b=int(input("Enter the birth year:-"))

    def calculate(self):
        self.age=2023-self.b
        print(f"Your age is:-{self.age}")

obj=birthyear()
obj.input()
obj.calculate()
