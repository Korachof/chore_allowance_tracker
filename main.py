import user
import sys


def main():
    """main script for Chore Allowance Tracker"""
    start_menu()
    menu_select()


def start_menu():
    """start menu for main script"""
    print("Welcome to the Chore Allowance Tracker!\n")
    print("Please Select from the Options Below\n")
    print("1) New User")
    print("2) Load User")
    print("3) Exit Program\n")


def menu_select():
    """menu select functionality for main script"""
    user_input = None
    while user_input != "1" and user_input != "2" and user_input != "3":
        user_input = input("Type the Associated Number and Press ENTER: ")
    
    if user_input == "1":
        create_user()

    elif user_input == "2":
        load_user()

    elif user_input == "3":
        exit_program()


def create_user():
    pass

def load_user():
    pass

def exit_program():
    print("Are you sure you want to EXIT?\n")
    exit_check = input("Type 1 for YES. Type Any Other Key For NO: ")
    if exit_check == "1":
        sys.exit()
    else:
        print("")       # an empty print to skip a line visually
        main()

def show_user_list():
    pass

if __name__ == "__main__":
    main()