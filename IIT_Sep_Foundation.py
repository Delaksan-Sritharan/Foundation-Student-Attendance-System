import random

def find_floating_point(input_str):
    if input_str.replace('.','').isdigit():
        return True
    else:
        return False

def isNIC(nic_str):
    if(len(nic_str) == 10 and nic_str[:9].isdigit() and nic_str[9].isalnum() and nic_str[-1].isalpha()):
        return True
    else:
        return  False




customers = []
balance = 00.00
choice1 = 0

# Displaying the heading
# Printing the options to let the user choose one
while True:
    if choice1 == 0:
        print("IIT Campus".center(50))
        print("Main Menu".center(50))
        print("")
        print("1) Enroll a new student")
        print("2) View details of a student")
        print("3) View details of all the students according to the branch")
        print("4) Update student details")
        print("5) Mark attendance")
        print("6) View attendance")
        print("7) Exit")
        try:
            choice1 = int(input("Your choice: "))
        except ValueError:
            print("Input a correct choice From 1 to 7")
            continue

    if choice1 == 1:

        if len(customers) >= 5:
            print("Customers limit reached")
            choice1 = 0
        else:
            print("IIT Campus".center(50))
            print("Enroll a new student".center(50))
            print("")
            # Generate a 10-digit random bank account number
            Bank_Account_Number = str(random.randint(1000000000, 9999999999))
            print(f"Bank Account Number: {Bank_Account_Number}")
            NIC = str(input("NIC: "))
            while not isNIC(NIC):
                print("Invalid NIC. Please enter a 10 character NIC with the first 9 characters as digits and the last character as either a digit or a letter.")
                NIC = str(input("NIC: "))
            First_Name = str(input("First Name: ")).capitalize()
            while not ((0 < len(First_Name) <= 10) and First_Name.isalpha()):
                print("Oops! Max 10 characters for First Name. Please try again.")
                First_Name = str(input("First Name: "))
            Last_Name = str(input("Last Name: ")).capitalize()
            while not ((0 < len(Last_Name) <= 15)and Last_Name.isalpha()):
                print("Oops! Max 10 characters for Last Name. Please try again.")
                Last_Name = str(input("Last Name: "))
            Birth_Date = input("Enter Birth Date (YYYY-MM-DD): ")
            while True:
                if not (len(Birth_Date) == 10 and Birth_Date[4] == '-' and Birth_Date[7] == '-'):
                    print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
                    Birth_Date = input("Enter Birth Date (YYYY-MM-DD): ")
                    continue  # Go back to the beginning of the loop

                try:
                    Birth_Year, Birth_Month, Birth_Day = Birth_Date.split('-')
                    Birth_Year = int(Birth_Year)  # Convert to integers for validation
                    Birth_Month = int(Birth_Month)
                    Birth_Day = int(Birth_Day)

                    # Validate month range (1-12)
                    if not (1 <= Birth_Month <= 12):
                        print("Invalid month. Please enter a value between 1 and 12.")
                        Birth_Date = input("Enter Birth Date (YYYY-MM-DD): ")
                        continue

                    # Validate day range based on month (considering leap years is optional)
                    if Birth_Month in (4, 6, 9, 11):  # Months with 30 days
                        if not (1 <= Birth_Day <= 30):
                            print(f"Invalid day for month {Birth_Month}. Please enter a value between 1 and 30.")
                            Birth_Date = input("Enter Birth Date (YYYY-MM-DD): ")
                            continue
                    elif Birth_Month == 2:  # February (28 days in non-leap years)
                        # Implement leap year check here for more accurate validation
                        if not (1 <= Birth_Day <= 28):
                            print(f"Invalid day for month {Birth_Month}. Please enter a value between 1 and 28.")
                            Birth_Date = input("Enter Birth Date (YYYY-MM-DD): ")
                            continue
                    else:  # Months with 31 days
                        if not (1 <= Birth_Day <= 31):
                            print(f"Invalid day for month {Birth_Month}. Please enter a value between 1 and 31.")
                            Birth_Date = input("Enter Birth Date (YYYY-MM-DD): ")
                            continue

                    break  # Exit loop if all validations pass
                except ValueError:
                    print("Invalid date components. Please enter numeric values for year, month, and day.")
                    Birth_Date = input("Enter Birth Date (YYYY-MM-DD): ")

            Permanent_Address = str(input("Permanent Address: "))
            while not (0 < len(Permanent_Address) <= 15):
                print("Invalid Address. Please enter a 15 character address.")
                Permanent_Address = str(input("Permanent Address: "))

            Phone_Number = str(input("Phone Number: "))
            while not (len(Phone_Number) == 10 and Phone_Number.isdigit()):
                print("Invalid phone number. Please enter a 10-digit number.")
                Phone_Number = str(input("Phone Number: "))

            while True:
                save_choice = input("Do you want to save the account (Yes/No)? ").lower()
                if save_choice == "yes" or save_choice == "Yes" or save_choice == "YES":
                    customer = [Bank_Account_Number, NIC, First_Name, Last_Name, Birth_Date, Permanent_Address,
                                Phone_Number, balance]
                    customers.append(customer)
                    print("Customer added successfully")
                    break
                elif save_choice == "no" or save_choice == "No" or save_choice == "NO":
                    if customers:
                        customers.pop()  # remove the last added customer
                    print("Customer not saved")
                    break
                else:
                    print("Invalid input. Please enter 'Yes' or 'No'")
            choice1 = 0


    elif choice1 == 2:

        while True:

            print("ABC Bank".center(50))
            print("View details of a customer".center(50))
            print("")
            Bank_Account_Number = input("Bank Account Number: ")
            if not Bank_Account_Number:
                print("Please enter a bank account number.")
                continue  # Go back to the beginning of the loop


            # Check if the account exists
            account_found = False
            for customer in customers:
                if customer[0] == Bank_Account_Number:
                    account_found = True
                    print(f"NIC: {customer[1]}")
                    print(f"Phone Number: {customer[6]}")
                    print(f"First Name: {customer[2]}")
                    print(f"Last Name: {customer[3]}")
                    print(f"Bank Balance: {customer[7]:.2f}")

                    another_view = input("Do you want to view another account details (Yes/No)? ").lower()

                    if another_view == "yes":
                        continue  # Break out of the outer loop for new account number

                    # **Fixed indentation here**
                    elif another_view == "no":
                        # Go back to the main menu
                        break  # Break out of the inner loop, returning to main menu
                    else:
                        print("Invalid choice. Please select a valid option.")

            if not account_found:
                print("Account not found. Please re-enter the account number.")
            if another_view == "no":
                break

        choice1 = 0


    elif choice1 == 3:

        while True:

            print("ABC Bank".center(50))

            print("View details of all the customers".center(50))

            print("NIC\t\tAccount NO\tFirst Name\tLast Name\t\tBank Balance")

            for customer in customers:
                first_name_indent = 10-len(customer[2])
                last_name_indent = 15-len(customer[3])
                print(f"{customer[1]} \t{customer[0]}\t{customer[2]}"+" "*first_name_indent+f"\t{customer[3]}"+" "*last_name_indent+f"\t{customer[7]}")

            update_choice = input("Do you want to update the account details (Yes/No)? ").lower()

            if update_choice == "yes":
                choice1 = 6
                break
            elif update_choice == "no":
                choice1 = 0
                break
            else:
                print("Invalid choice. Please select a valid option")
                break
        # Switch to option 6 for updating details

    elif choice1 == 4:
        print("ABC Bank".center(50))
        print("Deposit Money to a given account")
        print("")
        Bank_Account_Number = input("Bank Account Number: ")
        if not Bank_Account_Number:
            print("Please enter a bank account number.")
            continue  # Go back to the beginning of the loop
        Deposit_Amount = input("Deposit Amount: ")

        while not find_floating_point(Deposit_Amount):
            Deposit_Amount = input("Deposit Amount: ")

              # Go back to the beginning of the loop
        Deposit_Amount = float(Deposit_Amount)
        save_choice = input("Do you want to save (Yes/No)? ").lower()

        if save_choice == "yes":
            print("Details saved.")
            account_found = False
            for customer in customers:
                if customer[0] == Bank_Account_Number:
                    account_found = True
                    customer[7] += Deposit_Amount
            print(f"Deposited {Deposit_Amount:.2f} to account {Bank_Account_Number}. New balance: {customer[7]:.2f}")
            choice1 = 0


        elif save_choice == "no":
            print("Account not found. Please re-enter the account number.")
            choice1 = 0


    elif choice1 == 5:
        print("ABC Bank".center(50))
        print("Withdraw money from a given account")
        Bank_Account_Number = input("Bank Account Number: ")
        account_found = False
        for customer in customers:
            if customer[0] == Bank_Account_Number:
                account_found = True
                Withdraw_Amount = float(input("Withdraw Amount: "))
                save_choice = input("Do you want to save (Yes/No)? ").lower()
                if save_choice == "yes":
                    print("Details saved.")
                    if customer[7] >= Withdraw_Amount:
                        customer[7] -= Withdraw_Amount

                        print(
                            f"Withdrew {Withdraw_Amount:.2f} from account {Bank_Account_Number}. New balance: {customer[7]:.2f}")
                    choice1 = 0
                elif save_choice == "no":
                    print("Details not saved.")

                else:
                    print("Invalid input")

                choice1 = 0
                break

        if not account_found:
            print("Account not found. Please re-enter the account number.")
        choice1 = 0

    elif choice1 == 6:
        print("ABC Bank".center(50))
        print("Update Customer Details")
        print("")
        Bank_Account_Number = input("Bank Account Number: ")
        account_found = False
        for customer in customers:
            if customer[0] == Bank_Account_Number:
                account_found = True
                print("Current Details:")
                print(f"NIC: {customer[1]}")
                print(f"Phone Number: {customer[6]}")
                print(f"First Name: {customer[2]}")
                print(f"Last Name: {customer[3]}")
                print(f"Birth Date: {customer[4]}")
                print(f"Permanent Address: {customer[5]}")
                NIC = input("New NIC: ")
                while not isNIC(NIC):
                    print("Invalid NIC. Please enter a 10 character NIC with the first 9 characters as digits and the last character as either a digit or a letter.")
                    NIC = input("New NIC: ")
                new_first_name = input("New First Name: ").capitalize()
                while not ((0 < len(new_first_name) <= 10) and new_first_name.isalpha()):
                    print("Oops! Max 10 characters for First Name. Please try again.")
                    new_first_name = input("New First Name: ").capitalize()
                new_last_name = input("New Last Name: ").capitalize()
                while not ((0 < len(new_last_name) <= 15) and new_last_name.isalpha()):
                    print("Oops! Max 15 characters for Last Name. Please try again.")
                    new_last_name = input("New Last Name: ").capitalize()
                new_phone_number = input("New Phone Number: ")
                while not (len(new_phone_number) == 10 and new_phone_number.isdigit()):
                    print("Invalid phone number. Please enter a 10-digit number.")
                    new_phone_number = input("New Phone Number: ")
                new_permanent_address = input("New Permanent Address: ")
                while not (0 < len(new_permanent_address) <= 15):
                    print("Invalid Address. Please enter a 15 character address.")
                    new_permanent_address = input("New Permanent Address: ")
                save_choice = input("Do you want to save (Yes/No)? ").lower()
                if save_choice == "yes":
                    customer[2] = new_first_name if new_first_name else customer[2]
                    customer[3] = new_last_name if new_last_name else customer[3]
                    customer[6] = new_phone_number if new_phone_number else customer[6]
                    customer[5] = new_permanent_address if new_permanent_address else customer[5]
                    print("Customer details updated successfully.")
                    choice1 = 0
                if save_choice == "no":
                    print("customer is not saved.")
                    choice1 = 0
                break
        if not account_found:
            print("Account not found. Please re-enter the account number.")
        choice = 0

    elif choice1 == 7:
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please select a valid option.")
