from bank_app import BankApp
from console_ui import display_menu_logged_out, display_menu_logged_in

def main():
    app = BankApp("accounts.xlsx")

    while True:
        if app.current_account:
            choice = display_menu_logged_in()
            if choice == "1":
                old_password = input("Enter old password: ")
                new_password = input("Enter new password: ")
                app.update_password(old_password, new_password)
            elif choice == "2":
                app.view_balance()
            elif choice == "3":
                to_username = input("Enter recipient's username: ")
                amount = float(input("Enter the amount to send: "))
                app.send_money(to_username, amount)
            elif choice == "4":
                app.logout()
            elif choice == "0":
                break
            else:
                print("Invalid choice.")
        else:
            choice = display_menu_logged_out()
            if choice == "1":
                username = input("Enter username: ")
                password = input("Enter password: ")
                app.create_account(username, password)
            elif choice == "2":
                username = input("Enter username: ")
                password = input("Enter password: ")
                app.login_account(username, password)
            elif choice == "0":
                break
            else:
                print("Invalid choice.")

if __name__ == "__main__":
    main()
