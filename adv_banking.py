import random
import sqlite3


class BankingSystem:
    def __init__(self):
        self.conn = sqlite3.connect('card.s3db')
        self.cur = self.conn.cursor()
        self.create_table()

    def create_table(self):
        # Create the 'card' table if it doesn't exist
        self.cur.execute('''
            CREATE TABLE IF NOT EXISTS card (
                id INTEGER PRIMARY KEY,
                number TEXT,
                pin TEXT,
                balance INTEGER DEFAULT 0
            )
        ''')
        self.conn.commit()

    def generate_card_number(self):
        # Generate 9 random digits
        card_number = "400000" + \
                      ''.join([str(random.randint(0, 9)) for _ in range(9)])
        # Calculate and append the checksum
        card_number += str(self.calculate_checksum(card_number))
        return card_number

    def calculate_checksum(self, card_number):
        # Implement the Luhn algorithm to calculate the checksum
        digits = [int(digit) for digit in card_number]
        checksum = 0
        for index, digit in enumerate(digits):
            if index % 2 == 0:
                digit *= 2
                if digit > 9:
                    digit -= 9
            checksum += digit
        return (10 - (checksum % 10)) % 10

    def generate_pin(self):
        # Generate a random 4-digit PIN
        return str(random.randint(1000, 9999))

    def create_account(self):
        card_number = self.generate_card_number()
        pin = self.generate_pin()
        balance = 0

        # Insert account data into the 'card' table
        self.cur.execute('''
            INSERT INTO card (number, pin, balance)
            VALUES (?, ?, ?)
        ''', (card_number, pin, balance))
        self.conn.commit()

        print("Your card has been created")
        print(f"Your card number:\n{card_number}")
        print(f"Your card PIN:\n{pin}")

    def log_into_account(self):
        card_number = input("Enter your card number:\n>")
        pin = input("Enter your PIN:\n>")

        # Retrieve account data from the 'card' table
        self.cur.execute('''
            SELECT * FROM card
            WHERE number = ? AND pin = ?
        ''', (card_number, pin))
        account_data = self.cur.fetchone()

        if account_data:
            print("You have successfully logged in!")
            self.account_menu(card_number)
        else:
            print("Wrong card number or PIN!")

    def account_menu(self, card_number):
        while True:
            print(
                "\n1. Balance\n2. Add income\n3. Do transfer\n4. Close account\n5. Log out\n0. Exit")
            choice = input(">")
            if choice == '1':
                # Retrieve and print the balance from the 'card' table
                self.cur.execute('''
                    SELECT balance FROM card
                    WHERE number = ?
                ''', (card_number,))
                balance = self.cur.fetchone()[0]
                print(f"Balance: {balance}")
            elif choice == '2':
                self.add_income(card_number)
            elif choice == '3':
                self.do_transfer(card_number)
            elif choice == '4':
                self.close_account(card_number)
            elif choice == '5':
                print("You have successfully logged out!")
                break
            elif choice == '0':
                print("Bye!")
                self.conn.close()
                exit()
            else:
                print("Invalid choice. Please try again.")

    def add_income(self, card_number):
        income = int(input("Enter income:\n>"))

        # Update the balance in the 'card' table
        self.cur.execute('''
            UPDATE card
            SET balance = balance + ?
            WHERE number = ?
        ''', (income, card_number))
        self.conn.commit()

        print("Income was added successfully!")

    def do_transfer(self, sender_card_number):
        receiver_card_number = input("Enter receiver's card number:\n>")

        if receiver_card_number == sender_card_number:
            print("You can't transfer money to the same account!")
            return

        if not self.luhn_algorithm_valid(receiver_card_number):
            print("Probably you made a mistake in the card number. Please try again!")
            return

        # Check if the receiver's card number exists
        self.cur.execute('''
            SELECT * FROM card
            WHERE number = ?
        ''', (receiver_card_number,))
        receiver_data = self.cur.fetchone()

        if not receiver_data:
            print("Such a card does not exist.")
            return

        transfer_amount = int(
            input("Enter how much money you want to transfer:\n>"))

        # Check if the sender has enough money
        self.cur.execute('''
            SELECT balance FROM card
            WHERE number = ?
        ''', (sender_card_number,))
        sender_balance = self.cur.fetchone()[0]

        if transfer_amount > sender_balance:
            print("Not enough money!")
            return

        # Perform the transaction: deduct from sender, add to receiver
        self.cur.execute('''
            UPDATE card
            SET balance = balance - ?
            WHERE number = ?
        ''', (transfer_amount, sender_card_number))

        self.cur.execute('''
            UPDATE card
            SET balance = balance + ?
            WHERE number = ?
        ''', (transfer_amount, receiver_card_number))

        self.conn.commit()

        print("Success! Money has been transferred.")

    def close_account(self, card_number):
        # Delete the account from the 'card' table
        self.cur.execute('''
            DELETE FROM card
            WHERE number = ?
        ''', (card_number,))
        self.conn.commit()

        print("Account has been closed.")

    def luhn_algorithm_valid(self, card_number):
        # Implement the Luhn algorithm to check the card number validity
        digits = [int(digit) for digit in card_number[:-1]]
        checksum = 0
        for index, digit in enumerate(digits):
            if index % 2 == 0:
                digit *= 2
                if digit > 9:
                    digit -= 9
            checksum += digit
        return (checksum + int(card_number[-1])) % 10 == 0


if __name__ == "__main__":
    banking_system = BankingSystem()

    while True:
        print("\n1. Create an account\n2. Log into account\n0. Exit")
        option = input("Enter your choice:\n>")
        if option == '1':
            banking_system.create_account()
        elif option == '2':
            banking_system.log_into_account()
        elif option == '0':
            print("Bye!")
            break
        else:
            print("Invalid choice. Please try again.")
