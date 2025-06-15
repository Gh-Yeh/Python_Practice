x = 1000

option = 0
transaction_count = 0
Failed_withdraws = 0
pwd = "1234"
if input("Enter your password: ") == pwd:
    while option != 4:
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        option = int(input("Select an option: "))
        if option == 1:
            print(f"Your current balance is: ${x}")
        elif option == 2:
            deposit = int(input("Enter the amount to deposit: "))
            x += deposit
            transaction_count += 1
            print(f"You have deposited ${deposit}. Your new balance is: ${x}")
        elif option == 3:
            withdraw = int(input("Enter the amount to withdraw: "))
            if 0 < withdraw <= x:
                x -= withdraw
                transaction_count += 1
                print(f"You have withdrawn ${withdraw}. Your new balance is: ${x}")
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
