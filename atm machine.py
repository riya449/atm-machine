# Custom Exceptions
class InsufficientBalanceError(Exception):
    pass

class InvalidPINError(Exception):
    pass


def atm_machine():
    correct_pin = "1234"
    balance = 5000
    attempts = 0

    #  PIN Authentication (3 attempts only)
    while attempts < 3:
        try:
            pin = input("Enter your PIN: ")

            if pin != correct_pin:
                attempts += 1
                raise InvalidPINError("Incorrect PIN!")

            print("\nLogin Successful!")
            break

        except InvalidPINError as e:
            print(e)
            print("Attempts left:", 3 - attempts)

        except KeyboardInterrupt:
            print("\nOperation cancelled by user.")
            return

        except Exception as e:
            print("Unexpected Error:", e)
            return

    else:
        print("Too many wrong attempts. Card blocked!")
        return

    #  ATM Menu
    while True:
        try:
            print("\n===== ATM MENU =====")
            print("1. Check Balance")
            print("2. Withdraw Money")
            print("3. Deposit Money")
            print("4. Exit")

            choice = int(input("Enter choice: "))

            if choice == 1:
                print("Current Balance:", balance)

            elif choice == 2:
                amount = float(input("Enter withdrawal amount: "))
                if amount > balance:
                    raise InsufficientBalanceError("Insufficient Balance!")
                if amount <= 0:
                    raise ValueError("Invalid withdrawal amount!")
                balance -= amount
                print("Withdrawal Successful!")
                print("Remaining Balance:", balance)

            elif choice == 3:
                amount = float(input("Enter deposit amount: "))
                if amount <= 0:
                    raise ValueError("Invalid deposit amount!")
                balance += amount
                print("Deposit Successful!")
                print("Updated Balance:", balance)

            elif choice == 4:
                print("Thank you for using ATM!")
                break

            else:
                raise ValueError("Invalid menu choice!")

        except ValueError as ve:
            print("Value Error:", ve)

        except InsufficientBalanceError as ibe:
            print("Balance Error:", ibe)

        except ZeroDivisionError:
            print("Math Error occurred!")

        except KeyboardInterrupt:
            print("\nTransaction cancelled by user.")
            break

        except Exception as e:
            print("Unexpected Error:", e)


# Run ATM
atm_machine()