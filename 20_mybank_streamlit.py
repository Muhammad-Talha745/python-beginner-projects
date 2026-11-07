import pandas as pd
import sqlite3
import streamlit as st
import random


def create_table():
    with sqlite3.connect("mybank.db") as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS accounts (
                account_number INTEGER PRIMARY KEY,
                account_title TEXT NOT NULL,
                account_pin INTEGER NOT NULL,
                account_balance INTEGER DEFAULT 0
            )
        """)


create_table()


# BANKING FUNCTIONS
def open_account(account_title):
    account_number = random.randint(10000, 99999)
    with sqlite3.connect("mybank.db") as conn:
        while conn.execute(
            "SELECT account_number FROM accounts WHERE account_number = ?",
            (account_number,),
        ).fetchone():
            account_number = random.randint(10000, 99999)
        account_pin = random.randint(1000, 9999)
        initial_balance = 0
        conn.execute(
            """
            INSERT INTO accounts
            (account_number, account_title, account_pin, account_balance)
            VALUES (?, ?, ?, ?)
            """,
            (account_number, account_title, account_pin, initial_balance),
        )
    return {
        "account_title": account_title,
        "account_number": account_number,
        "account_pin": account_pin,
        "account_balance": initial_balance,
    }


def check_balance(user_account, user_pin):
    with sqlite3.connect("mybank.db") as conn:
        account = conn.execute(
            """
            SELECT account_balance
            FROM accounts
            WHERE account_number = ? AND account_pin = ?
            """,
            (user_account, user_pin),
        ).fetchone()
    if account:
        return account[0]
    return "Invalid Account or PIN"


def cash_withdrawal(user_account, user_pin, amount):
    if amount <= 0:
        return "Amount must be greater than zero"
    with sqlite3.connect("mybank.db") as conn:
        account = conn.execute(
            """
            SELECT account_balance
            FROM accounts
            WHERE account_number = ? AND account_pin = ?
            """,
            (user_account, user_pin),
        ).fetchone()
        if account:
            current_balance = account[0]
            if amount <= current_balance:
                conn.execute(
                    """
                    UPDATE accounts
                    SET account_balance = account_balance - ?
                    WHERE account_number = ?
                    """,
                    (amount, user_account),
                )
                return "Withdrawal Successful"
            return "Insufficient Balance"
    return "Invalid Account or PIN"


def cash_deposit(user_account, user_pin, amount):
    if amount <= 0:
        return "Amount must be greater than zero"
    with sqlite3.connect("mybank.db") as conn:
        account = conn.execute(
            """
            SELECT account_balance
            FROM accounts
            WHERE account_number = ? AND account_pin = ?
            """,
            (user_account, user_pin),
        ).fetchone()
        if account:
            conn.execute(
                """
                UPDATE accounts
                SET account_balance = account_balance + ?
                WHERE account_number = ?
                """,
                (amount, user_account),
            )
            return "Deposit Successful"
    return "Invalid Account or PIN"


def transfer_amount(user_account, user_pin, amount, beneficiary_account):
    if amount <= 0:
        return "Amount must be greater than zero"
    if user_account == beneficiary_account:
        return "Cannot transfer to the same account"
    with sqlite3.connect("mybank.db") as conn:
        sender = conn.execute(
            """
            SELECT account_balance
            FROM accounts
            WHERE account_number = ? AND account_pin = ?
            """,
            (user_account, user_pin),
        ).fetchone()
        if not sender:
            return "Invalid Sender Account or PIN"
        beneficiary = conn.execute(
            """
            SELECT account_number
            FROM accounts
            WHERE account_number = ?
            """,
            (beneficiary_account,),
        ).fetchone()
        if not beneficiary:
            return "Invalid Beneficiary Account"

        if amount > sender[0]:
            return "Insufficient Balance"
        conn.execute(
            """
            UPDATE accounts
            SET account_balance = account_balance - ?
            WHERE account_number = ?
            """,
            (amount, user_account),
        )
        conn.execute(
            """
            UPDATE accounts
            SET account_balance = account_balance + ?
            WHERE account_number = ?
            """,
            (amount, beneficiary_account),
        )
    return "Transfer Successful"


def close_account(user_account, user_pin):
    with sqlite3.connect("mybank.db") as conn:
        account = conn.execute(
            """
            SELECT account_number
            FROM accounts
            WHERE account_number = ? AND account_pin = ?
            """,
            (user_account, user_pin),
        ).fetchone()
        if account:
            conn.execute(
                """
                DELETE FROM accounts
                WHERE account_number = ?
                """,
                (user_account,),
            )
            return "Account Closed Successfully"
    return "Invalid Account or PIN"


def show_all_accounts():
    with sqlite3.connect("mybank.db") as conn:
        accounts = conn.execute("""
            SELECT account_number, account_title, account_balance
            FROM accounts
            """).fetchall()

    return accounts


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

            st.success("Account Created Successfully!")

            st.write("Account Title:", new_account["account_title"])
            st.write("Account Number:", new_account["account_number"])
            st.write("Account PIN:", new_account["account_pin"])
            st.write("Initial Balance:", new_account["account_balance"])

        else:
            st.error("Please enter an account title.")


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

    accounts = show_all_accounts()

    if accounts:
        df = pd.DataFrame(
            accounts,
            columns=[
                "Account Number",
                "Account Title",
                "Balance (Rs)",
            ],
        )

        st.dataframe(df, use_container_width=True)

    else:
        st.info("No accounts have been created yet.")
