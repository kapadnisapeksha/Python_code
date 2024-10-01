class library:
      def input(self):
            self.name=input("Enter the name of book:_")
            self.price=int(input("Enter the price:-"))
            self.days=int(input("How much day you delaied:-"))
      def call(self):
            if(self.days>1 or self.days<=7):
                  self.calculation=self.days*0.25
            elif(self.days==8 or self.days<=15):
                  self.calculation=self.days*0.40
            elif(self.days==16 or self.days<=30):
                  self.calculation=self.days*0.60
            elif(self.days>30):
                 self.calculation=self.days*0.80
      def displays(self):
            print("You have to pay the amount",self.calculation)
            print(self.name)
            print(self.price)

lib=library()
lib.input()
lib.call()
lib.displays()
                
                  