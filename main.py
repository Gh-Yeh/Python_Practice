balance_amount = 1000

option = 0
transaction_count = 0
Failed_withdraws = 0
pwd = "1234"

# Validating password
if input("Enter your password: ") == pwd:
    # Main loop for the ATM program
    while option != 4:
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        # Prompt user for an option
        option = int(input("Select an option: "))
        # Validate option input
        if option == 1:
            print(f"Your current balance is: ${balance_amount}")
        elif option == 2:
            deposit = int(input("Enter the amount to deposit: "))
            if deposit <= 0:
                print("Deposit amount must be greater than zero.")
                continue
            balance_amount += deposit
            transaction_count += 1
            print(
                f"You have deposited ${deposit}. Your new balance is: ${balance_amount}"
            )
        elif option == 3:
            withdraw = int(input("Enter the amount to withdraw: "))
            if 0 < withdraw <= balance_amount:
                balance_amount -= withdraw
                transaction_count += 1
                print(
                    f"You have withdrawn ${withdraw}. Your new balance is: ${balance_amount}"
                )
            else:
                print("Insufficient funds or invalid amount entered.")
                Failed_withdraws += 1
            if Failed_withdraws > 3:
                print("Too many failed withdrawal attempts !!")
        elif option == 4:
            print("Exiting the program. Thank you!")
            print(f"Total transactions made: {transaction_count}")
        else:
            print("Invalid option selected. Please try again.")
else:
    print("Incorrect password. Exiting...")
