class Bank():
    owner = ''
    balance = 0

    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
    
    def __str__(self):
        return(f"The owner of the bank is {self.owner} and balance is {self.balance}")
    
    def deposit(self):
        amt = float(input("Enter the amount you want to deposit:"))
        self.balance = self.balance+amt
    
    def display_balance(self):
        print(f"Yor current balance is :{self.balance}")

    def withdraw(self):
        amt = float(input("ENter the amount you want to withdraw:"))
        if amt > self.balance:
            print(f"Balance is not sufficient. You current balance is{self.balance}")
        else:
            self.balance = self.balance - amt


mybank = Bank("Billy",100)
choice = ''
while choice != '5':
    print("\nEnter 1 for knowing the information of the bank")
    print("Enter 2 for Deposit")
    print("Enter 3 for Withdraw")
    print("Enter 4 for Checking the Balance")
    print("Enter 5 to Exit")

    choice = input("Enter your choice: ")

    match choice:
        case '1':
            print(mybank)
        case '2':
            mybank.deposit()
        case '3':
            mybank.withdraw()
        case '4':
            mybank.display_balance()
        case '5':
            print("Thank you for your services")
        case _:
            print("Invalid choice. Please try again.")