def display_menu_logged_out():
    print("\nOptions:")
    print("1. Create Account")
    print("2. Login Account")
    print("0. Exit")
    return input("Enter your choice: ")


def display_menu_logged_in():
    print("\nOptions:")
    print("1. Update Password")
    print("2. View Balance")
    print("3. Send Money to other account")
    print("4. Logout")
    print("5. Deposit Money")
    print("6. Withdraw Money")
    print("0. Exit")
    return input("Enter your choice: ")
