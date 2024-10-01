class saving_account:
    def __init__(self):
        self.balance = 0
        self.accountno = 0

    def deposit(self):
        dep = int(input("Enter the amount you want to deposit: "))
        self.balance += dep
        print(f"Deposited amount: {dep}")
        print(f"Your available bank balance is: {self.balance}")

    def withdraw(self):
        withdraw = int(input("Enter the amount you want to withdraw: "))
        if withdraw <= self.balance:
            self.balance -= withdraw
            print(f"Withdrawn amount: {withdraw}")
            print(f"Your available bank balance is: {self.balance}")
        else:
            print("Insufficient balance for withdrawal.")

    def show(self):
        print(f"Your available bank balance is: {self.balance}")


s1 = saving_account()
while True:
    print("\n1. Check bank balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        s1.show()
    elif choice == 2:
        s1.deposit()
    elif choice == 3:
        s1.withdraw()
    elif choice == 4:
        break
    else:
        print("Invalid choice. Please try again.")
