import streamlit as st
import random

# SESSION STATE
if "all_accounts" not in st.session_state:
    st.session_state.all_accounts = []

if "created_account" not in st.session_state:
    st.session_state.created_account = None


# BANKING FUNCTIONS
def open_account(account_title):
    account_number = random.randint(10000, 99999)
    while any(
        account["account_number"] == account_number
        for account in st.session_state.all_accounts
    ):
        account_number = random.randint(10000, 99999)
    account_pin = random.randint(1000, 9999)
    account = {
        "account_title": account_title,
        "account_number": account_number,
        "account_pin": account_pin,
        "account_balance": 0,
    }
    st.session_state.all_accounts.append(account)
    return account


def check_balance(user_account, user_pin):
    for account in st.session_state.all_accounts:
        if account["account_number"] == user_account:
            if user_pin == account["account_pin"]:
                return account["account_balance"]
            return "Invalid PIN"
    return "Invalid Account"


def cash_withdrawal(user_account, user_pin, amount):
    if amount <= 0:
        return "Amount must be greater than zero"
    for account in st.session_state.all_accounts:
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
    for account in st.session_state.all_accounts:
        if account["account_number"] == user_account:
            if user_pin == account["account_pin"]:
                account["account_balance"] += amount
                return "Deposit Successful"
            return "Invalid PIN"
    return "Invalid Account"


def transfer_amount(user_account, user_pin, amount, beneficiary_account):
    if amount <= 0:
        return "Amount must be greater than zero"
    for account in st.session_state.all_accounts:
        if account["account_number"] == user_account:
            if user_pin == account["account_pin"]:
                if user_account == beneficiary_account:
                    return "Cannot transfer to the same account"
                if amount > account["account_balance"]:
                    return "Insufficient Balance"
                for beneficiary in st.session_state.all_accounts:
                    if beneficiary["account_number"] == beneficiary_account:
                        account["account_balance"] -= amount
                        beneficiary["account_balance"] += amount
                        return "Transfer Successful"
                return "Invalid Beneficiary Account"
            return "Invalid PIN"
    return "Invalid Sender Account"


def close_account(user_account, user_pin):
    for index, account in enumerate(st.session_state.all_accounts):
        if account["account_number"] == user_account:
            if user_pin == account["account_pin"]:
                del st.session_state.all_accounts[index]
                return "Account Closed Successfully"
            return "Invalid PIN"
    return "Invalid Account"


# STREAMLIT INTERFACE
st.title("🏦 MYBANK - Banking Management System")


menu = st.sidebar.selectbox(
    "Select Banking Service",
    [
        "Open Account",
        "Check Balance",
        "Cash Withdrawal",
        "Cash Deposit",
        "Transfer Money",
        "Close Account",
        "Show All Accounts",
    ],
)


if menu == "Open Account":
    st.header("➕ Open a New Account")

    account_title = st.text_input("Enter Your Account Title")

    if st.button("Create Account"):
        if account_title.strip():
            new_account = open_account(account_title.strip())
            st.session_state.created_account = new_account
            st.success("Account Created Successfully!")
        else:
            st.error("Please enter an account title.")

    if st.session_state.created_account is not None:
        account = st.session_state.created_account

        st.write("Account Title:", account["account_title"])
        st.write("Account Number:", account["account_number"])
        st.write("Account PIN:", account["account_pin"])
        st.write("Initial Balance:", account["account_balance"])


elif menu == "Check Balance":
    st.header("💰 Check Account Balance")

    user_account = st.number_input(
        "Enter Account Number", min_value=10000, max_value=99999
    )
    user_pin = st.number_input("Enter PIN", min_value=1000, max_value=9999)

    if st.button("Check Balance"):
        result = check_balance(user_account, user_pin)

        if isinstance(result, int):
            st.success(f"Your Current Balance: Rs {result}")
        else:
            st.error(result)


elif menu == "Cash Deposit":
    st.header("📥 Deposit Money")

    user_account = st.number_input(
        "Enter Account Number", min_value=10000, max_value=99999
    )
    user_pin = st.number_input("Enter PIN", min_value=1000, max_value=9999)
    amount = st.number_input("Enter Deposit Amount", min_value=1)

    if st.button("Deposit Money"):
        result = cash_deposit(user_account, user_pin, amount)

        if result == "Deposit Successful":
            st.success(result)
        else:
            st.error(result)


elif menu == "Cash Withdrawal":
    st.header("📤 Withdraw Money")

    user_account = st.number_input(
        "Enter Account Number", min_value=10000, max_value=99999
    )
    user_pin = st.number_input("Enter PIN", min_value=1000, max_value=9999)
    amount = st.number_input("Enter Withdrawal Amount", min_value=1)

    if st.button("Withdraw Money"):
        result = cash_withdrawal(user_account, user_pin, amount)

        if result == "Withdrawal Successful":
            st.success(result)
        else:
            st.error(result)


elif menu == "Transfer Money":
    st.header("💸 Transfer Money")

    user_account = st.number_input(
        "Your Account Number", min_value=10000, max_value=99999
    )
    user_pin = st.number_input("Your PIN", min_value=1000, max_value=9999)
    amount = st.number_input("Transfer Amount", min_value=1)
    beneficiary_account = st.number_input(
        "Beneficiary Account Number", min_value=10000, max_value=99999
    )

    if st.button("Transfer Money"):
        result = transfer_amount(user_account, user_pin, amount, beneficiary_account)

        if result == "Transfer Successful":
            st.success(result)
        else:
            st.error(result)


elif menu == "Close Account":
    st.header("❌ Close Bank Account")

    user_account = st.number_input(
        "Enter Account Number", min_value=10000, max_value=99999
    )
    user_pin = st.number_input("Enter PIN", min_value=1000, max_value=9999)

    if st.button("Close Account"):
        result = close_account(user_account, user_pin)

        if result == "Account Closed Successfully":
            st.success(result)
        else:
            st.error(result)


elif menu == "Show All Accounts":
    st.header("📋 All Bank Accounts")

    if st.session_state.all_accounts:
        st.dataframe(st.session_state.all_accounts, use_container_width=True)
    else:
        st.info("No accounts have been created yet.")
