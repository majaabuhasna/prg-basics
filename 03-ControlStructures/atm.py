###
# ATM (cash machine) simulator
#
balance = 1000  # Initial balance
pin = '1111' # initial 4-digit PIN code
pin_tries = 0
access_granted = False

while pin_tries < 3:
    entered_pin = input('Please enter your 4-digit PIN: ')
    if entered_pin == pin:
        access_granted = True
        print('Access granted.')
        print ()
        break
    else:
        pin_tries += 1
        if pin_tries < 3:
            print(f'Incorrect PIN. {3 - pin_tries} attempt/s remaining.')

if access_granted:
    while True:
        print()
        print("ATM Menu:")
        print("1. Check balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Change PIN")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")
        print()

        if choice == '1':
            print(f"Your current balance is: €{balance}")
        elif choice == '2':
            amount = float(input("Enter the amount to deposit: "))
            balance += amount
            print(f"€{amount} has been deposited. New balance: €{balance}")
        elif choice == '3':
            amount = float(input("Enter the amount to withdraw: "))
            if amount <= balance:
                balance -= amount
                print(f"€{amount} has been withdrawn. New balance: €{balance}")
            else:
                print("Insufficient balance.")
        elif choice == '4':
            current_pin_check = input('To change PIN, please enter your CURRENT PIN: ')
            if current_pin_check != pin:
                print('Incorrect current PIN. Action cancelled.')
            else:
                new_pin = input('Enter your NEW 4-digit PIN: ')
                if len(new_pin) == 4 and new_pin.isdigit():
                    new_pin_confirm = input('Re-enter your NEW PIN to comfirm: ')
                    if new_pin_confirm == new_pin:
                        pin = new_pin
                        print('PIN changed successfully.')
                    else:
                        print('New PINs do not match. Action cancelled.') 
                else:
                    print('Invalid PIN format. PIN must be exactly 4 digits.')
        elif choice == '5':
            print("Exiting... Thank you for using the ATM!")
            break  # Exit the loop
        else:
            print("Invalid option. Please try again.")
