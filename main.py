import user
import sys


def main():
    """main script for Chore Allowance Tracker"""
    print("Welcome to the Chore Allowance Tracker!\n")
    print("Please Select from the Options Below\n")
    print("1) New User")
    print("2) Load User")
    print("3) Exit Program\n")
    user_input = None
    while user_input != "1" and user_input != "2" and user_input != "3":
        user_input = input("Type the Associated Number and Press ENTER: ")
    
    if user_input == "1":
        create_user()

    elif user_input == "2":
        load_user()

    elif user_input == "3":
        print("Are you sure you want to EXIT?\n")
        exit_check = input("Type 1 for YES. Type Any Other Key For NO: ")
        if exit_check == "1":
            sys.exit()

        else:
            main()


def create_user():
    pass

def show_user_list():
    pass

def load_user():
    pass


if __name__ == "__main__":
    main()