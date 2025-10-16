import random

### accout clss


class Account:
    
    
    def __init__(self, name, email, address,account_type):
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.balance = 0
        self.transaction = []
        self.loan = 0
    def get_name(self):
        return self.name
    
    def account_number_generator(self):
        return random.randint(1000, 10000)
    def deposit(self, value):
        self.balance += value
        admin.total_balance_in_bank+=value
        print(f"{value} Deposit successful")
        print("\n\n")
        self.transaction.append(f'{value} deposit')

    def withdraw(self, value):
        if value > self.balance:
            print("Withdrawal amount exceeded")
            print("\n\n")
        elif value>admin.total_balance_in_bank:
            print("Bank is bankrupt")
            print("\n\n")
        else:
            self.balance -= value
            admin.total_balance_in_bank-=value
            print(f"{value} Withdraw successful")
            print("\n\n")
            self.transaction.append(f'{value} Withdraw')

    def check_available_balance(self):
        print(f"Your account balance is: {self.balance}")
        print("\n\n")

    def take_loan(self, amount, is_loan):
        if amount>admin.total_balance_in_bank:
            print("The loan cannot possible")
        else:
            if is_loan:
                if self.loan < 2:
                    self.loan += 1
                    self.balance += amount
                    admin.total_balance_in_bank-=amount
                    print("Loan take successful")
                    self.transaction.append(f'Loan taken {amount}')
                else:
                    print("You have exceeded your loan limit")
                    print("\n\n")
            else:
                print("The loan feature is turned off")
                print("\n\n")

    def transaction_history(self):
        for trans in self.transaction:
            print(trans)
            print("\n\n")

    def transfer_money(self, amount, receiver):
        if receiver is None:
            print("Account does not exist")
            print("\n\n")
        elif self.balance < amount:
            print("Not enough money")
            print("\n\n")
        else:
            self.balance -= amount
            receiver.balance += amount
            self.transaction.append(f'Transfer {amount} money to {receiver.name}')
            receiver.transaction.append(f"Receive {amount} money from {self.name}")
            print(f"Money transfer Successull to: {receiver.name}")
            print("\n\n\n")
 
        
            
            
    
##user class
          
class User:
    def __init__(self, account):
        self.account=account
    def get_name(self):
        return self.account.get_name()
    def balance(self):
        self.account.check_available_balance()
    def deposit(self, value):
       self.account.deposit(value)
    def withdraw(self, value):
       self.account.withdraw(value)
    def check_available_balance(self):
       self.account.check_available_balance()
    def take_loan(self, amount, is_loan):
       self.account.take_loan(amount, is_loan)
    def loan_balance(self):
        print(f'Your loan balance is: {self.account.loan}')
    def transaction_history(self):
       self.account.transaction_history()
    def transfer_money(self, amount, receiver):
       self.account.transfer_money(amount, receiver)
    
    
    
#bank class
class Bank:
    def __init__(self):
        self.loan_status=True
        self.account_list={}
        self.admin_pass=1234
        self.total_balance_in_bank=0
    def create_a_account(self, name, email, address, account_type):
        account_number=Account.account_number_generator(self)
        user = Account(name, email, address, account_type)
        self.account_list[account_number]=user
        print("Account create successful")
        print(f"Please print this Account Number: {account_number} and give to the {name}")
        print("\n\n")
        
    def delete_account(self, account_number):
        if account_number in self.account_list:
            del self.account_list[account_number]
            print("Account deleted successfully")
            print("\n\n")
        else:
            print("Account not found")
            print("\n\n")
          
    def total_av_balance_in_bank(self):
        print(f"Total balance in bank is: {self.total_balance_in_bank}")
    

    def total_loan_balance_in_bank(self):
        total_loan = 0
        for account in self.account_list.values():
            for transaction in account.transaction:
                if 'Loan taken' in transaction:
                    loan_amount = int(transaction.split()[2])
                    total_loan += loan_amount
        print(f"Total loan balance in bank: {total_loan}")
        print("\n\n")

    def loan_on_off(self):
        self.loan_status = not self.loan_status
        if self.loan_status:
            
            print("The loan feature turned on")
            return True
        else:
            
            print("The loan feature is off")
            return False

    def get_account(self, account_number):
        return self.account_list.get(account_number)
    def all_account_list(self):
        for account_number, account in self.account_list.items():
            print(f'account_number: {account_number} ')
            print(f'Account_details: Name: {account.name}, Email: {account.email}, Address: {account.address}, Account_type: {account.account_type} ')
            print("\n\n")


admin=Bank()  
while True:
    print("Welcome to our Bank Management System")
    print("Option 1: Admin")
    print("Option 2: User")
    print("Option 3: Exit")
    print("\n\n\n")
    op = int(input("Enter your option: "))
    if op == 1:
        pas = int(input("Enter your admin password: "))
        if pas==admin.admin_pass:
        
            
            
            while True:
                print("\n\n\n")
                print("Welcome to Admin Interface")
                print("Choice 1: Create an account ")
                print("Choice 2: Delete user account")
                print("Choice 3: View all user accounts list ")
                print("Choice 4: Total available balance of the bank")
                print("Choice 5: The total loan amount")
                print("Choice 6: On or off the loan feature of the bank")
                print("Choice 7: Exit")
                print("\n\n\n")
                ch = int(input("Enter your Choice: "))
                if ch == 1:
                    name = input("Enter user's name: ")
                    email = input("Enter user's email: ")
                    address = input("Enter user's address: ")
                    account_type = input("Enter user's account type (savings/current): ")
                    admin.create_a_account(name, email, address, account_type)
                    print("\n\n")
                elif ch == 2:
                    a_c=int(input("Enter account number to delete account: "))
                    admin.delete_account(a_c)
                    
                elif ch == 3:
                    admin.all_account_list()
                elif ch == 4:
                    admin.total_av_balance_in_bank()
                elif ch == 5:
                    admin.total_loan_balance_in_bank()
                elif ch == 6:
                    admin.loan_on_off()
                elif ch==7:
                    print("Exit From admin pannel")
                    print("\n\n\n")
                    break
                else:
                    print("invalid choice")
        else:
            print("Wrong passowrd")
            print("please try again")
            print("\n\n\n")
            
                    
            
        
    elif op == 2:
        while True:
            
            print("Welcome to User Interface")
            print("Choice 1: Log in to account")
            print("Choice 2: Exit ")
            print("\n\n\n")
            ch = int(input("Enter your choice: "))
            if ch==1:
                
                account_number=int(input("Enter your account number: "))
                user_object=admin.get_account(account_number)
                if user_object:
                    user= User(user_object)
                    print(f"WELCOME TO YOUR ACCOUNT: {user.get_name()}")
                    print("\n\n\n")
                    while True:
                        print("Option 1: Deposit")
                        print("Option 2: Withdraw")
                        print("Option 3: Check Balance")
                        print("Option 4: Transfer Money")
                        print("Option 5: Take Loan")
                        print("Option 6: View Transaction History")
                        print("Option 7: Exit")
                        print("\n\n\n")
                        user_choice = int(input("Enter your option: "))
                        if user_choice==1:
                            amount = int(input("Enter amount to deposit: "))
                            user.deposit(amount)
                        elif user_choice == 2:
                            amount = int(input("Enter amount to withdraw: "))
                            user.withdraw(amount)
                        elif user_choice == 3:
                            user.balance()       
                        elif user_choice == 4:
                            ac=int(input("Enter account number of reciver: "))
                            receiver=admin.get_account(ac)
                            u=admin.get_account(account_number)
                            if receiver==u:
                                print("you enter your account number")
                                print("\n\n\n")
                            else:
                                    
                                if receiver:
                                    amount=int(input("Enter your amount for transfer: "))
                                    user.transfer_money(amount,receiver)
                                else:
                                    print("Account does not exist")
                        elif user_choice == 5:
                            amount = int(input("Enter loan amount: "))
                            is_loan = admin.loan_status
                            user.take_loan(amount, is_loan)
                        
                        elif user_choice == 6:
                            user.transaction_history()
                            
                                
                        elif user_choice == 7:
                            print("You leave from account")
                            break
                        else:
                            print("Ivalid choice")
                            print("\n\n\n")
                else:
                    print("You enterd wrong account number")
                            
            elif ch==2:
                print("Exiting from user menu")
                print("\n\n\n")
                break
            else:
                print("Invalid choice")
                
                

    elif op==3:
        print("THANKS FOR VISITING OUR BANK")
        print("\n\n\n")
        break
    else:
        
        print("Invalid option. Please choose again.")
        print("\n\n\n")

                        

    