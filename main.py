x = 1000

option = 0

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
        print(f"You have deposited ${deposit}. Your new balance is: ${x}")
