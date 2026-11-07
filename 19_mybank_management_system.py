import random

all_accounts = [
    {
        "account_title": "Talha",
        "account_number": 12345,
        "account_pin": 4567,
        "account_balance": 50000,
    },
    {
        "account_title": "Haseeb",
        "account_number": 67890,
        "account_pin": 9876,
        "account_balance": 30000,
    },
]


def open_account():
    account_title = input("Enter Your Account Title: ")
    account_number = random.randint(10000, 99999)
    while any(account["account_number"] == account_number for account in all_accounts):
        account_number = random.randint(10000, 99999)
    account_pin = random.randint(1000, 9999)
    initial_balance = 0
    account = {
        "account_title": account_title,
        "account_number": account_number,
        "account_pin": account_pin,
        "account_balance": initial_balance,
    }
    all_accounts.append(account)
    return account


def check_balance(user_account, user_pin):
    for account in all_accounts:
        if account["account_number"] == user_account:
            if user_pin == account["account_pin"]:
                return account["account_balance"]
            return "Invalid PIN"
    return "Invalid Account"


def cash_withdrawal(user_account, user_pin, amount):
    if amount <= 0:
        return "Amount must be greater than zero"
    for account in all_accounts:
        if account["account_number"] == user_account:
            if user_pin == account["account_pin"]:
                if amount <= account["account_balance"]:
                    account["account_balance"] -= amount
                    return "Withdrawal Successful"
                return "Insufficient Balance"
            return "Invalid PIN"
    return "Invalid Account"


def cash_deposit(user_account, user_pin, amount):
    if amount <= 0:
        return "Amount must be greater than zero"
    for account in all_accounts:
        if account["account_number"] == user_account:
            if user_pin == account["account_pin"]:
                account["account_balance"] += amount
                return "Deposit Successful"
            return "Invalid PIN"
    return "Invalid Account"


def transfer_amount(user_account, user_pin, amount, beneficiary_account):
    if amount <= 0:
        return "Amount must be greater than zero"
    for account in all_accounts:
        if account["account_number"] == user_account:
            if user_pin == account["account_pin"]:
                if amount <= account["account_balance"]:
                    if user_account == beneficiary_account:
                        return "Cannot transfer to the same account"
                    for beneficiary in all_accounts:
                        if beneficiary["account_number"] == beneficiary_account:
                            account["account_balance"] -= amount
                            beneficiary["account_balance"] += amount
                            return "Transfer Successful"
                    return "Invalid Beneficiary Account"
                return "Insufficient Balance"
            return "Invalid PIN"
    return "Invalid Sender Account"


def close_account(user_account, user_pin):
    for index, account in enumerate(all_accounts):
        if account["account_number"] == user_account:
            if user_pin == account["account_pin"]:
                del all_accounts[index]
                return "Account Closed Successfully"
            return "Invalid PIN"
    return "Invalid Account"


def get_number(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Invalid input! Please enter numbers only.")


def banking_menu():
    while True:
        print("\n========== MYBANK ==========")
        print("1. Open Account")
        print("2. Check Balance")
        print("3. Cash Withdrawal")
        print("4. Cash Deposit")
        print("5. Transfer Money")
        print("6. Close Account")
        print("7. Exit")
        print("============================")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            new_account = open_account()
            print("\nAccount Created Successfully!")
            print("Account Details:", new_account)

        elif choice == "2":
            user_account = get_number("Enter Account Number: ")
            user_pin = get_number("Enter PIN: ")
            result = check_balance(user_account, user_pin)
            print("Balance:", result)

        elif choice == "3":
            user_account = get_number("Enter Account Number: ")
            user_pin = get_number("Enter PIN: ")
            amount = get_number("Enter Withdrawal Amount: ")
            result = cash_withdrawal(user_account, user_pin, amount)
            print(result)

        elif choice == "4":
            user_account = get_number("Enter Account Number: ")
            user_pin = get_number("Enter PIN: ")
            amount = get_number("Enter Deposit Amount: ")
            result = cash_deposit(user_account, user_pin, amount)
            print(result)

        elif choice == "5":
            user_account = get_number("Enter Sender Account Number: ")
            user_pin = get_number("Enter PIN: ")
            amount = get_number("Enter Transfer Amount: ")
            beneficiary_account = get_number("Enter Beneficiary Account: ")
            result = transfer_amount(
                user_account, user_pin, amount, beneficiary_account
            )
            print(result)

        elif choice == "6":
            user_account = get_number("Enter Account Number: ")
            user_pin = get_number("Enter PIN: ")
            result = close_account(user_account, user_pin)
            print(result)

        elif choice == "7":
            print("Thank you for using MYBANK!")
            break

        else:
            print("Invalid choice. Please try again.")


banking_menu()
