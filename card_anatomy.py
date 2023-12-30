import random


class BankingSystem:
    def __init__(self):
        self.accounts = {}

    def generate_card_number(self):
        # Generate 9 random digits
        card_number = "400000" + \
            ''.join([str(random.randint(0, 9)) for _ in range(9)])
        # Calculate and append the checksum
        card_number += str(self.calculate_checksum(card_number))
        return card_number

    def generate_pin(self):
        # Generate a random 4-digit PIN
        return '{:04}'.format(random.randint(0, 9999))

    def calculate_checksum(self, card_number):
        # Implement the Luhn algorithm to calculate the checksum
        digits = [int(digit) for digit in card_number]
        checksum = (sum(digits[:15]) * 9) % 10
        return checksum

    def create_account(self):
        card_number = self.generate_card_number()
        pin = self.generate_pin()
        balance = 0
        self.accounts[card_number] = {'pin': pin, 'balance': balance}
        print("Your card has been created")
        print(f"Your card number:\n{card_number}")
        print(f"Your card PIN:\n{pin}")

    def log_into_account(self):
        card_number = input("Enter your card number:\n>")
        pin = input("Enter your PIN:\n>")
        if card_number in self.accounts and self.accounts[card_number]['pin'] == pin:
            print("You have successfully logged in!")
            self.account_menu(card_number)
        else:
            print("Wrong card number or PIN!")

    def account_menu(self, card_number):
        while True:
            print("\n1. Balance\n2. Log out\n0. Exit")
            choice = input(">")
            if choice == '1':
                print(f"Balance: {self.accounts[card_number]['balance']}")
            elif choice == '2':
                print("You have successfully logged out!")
                break
            elif choice == '0':
                print("Bye!")
                exit()
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    banking_system = BankingSystem()

    while True:
        print("\n1. Create an account\n2. Log into account\n0. Exit")
        option = input(">")

        if option == '1':
            banking_system.create_account()
        elif option == '2':
            banking_system.log_into_account()
        elif option == '0':
            print("Bye!")
            break
        else:
            print("Invalid choice. Please try again.")
