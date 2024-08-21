import user
import chores
import sys


def main():
    """main script for Chore Allowance Tracker"""
    ui = UI()

class UI:       # considering refactoring the UI menu options into a class. 
    def __init__(self):
        self._user_object = self.start_menu()
        self._user_menu = self.user_profile()

    def start_menu(self):
        """start menu for main script"""
        print("")       # an empty print to skip a line visually
        print("Welcome to the Chore Allowance Tracker!\n")
        print("Please Select from the Options Below\n")
        print("1) New User")
        print("2) Load User")
        print("3) Exit Program\n")
        return self.menu_select()

    def menu_select(self):
        """menu select functionality for main script"""
        user_input = None
        while user_input != "1" and user_input != "2" and user_input != "3":
            user_input = input("Type the Associated Number and Press ENTER: ")
        
        if user_input == "1":
            return self.create_user()
        elif user_input == "2":
            return self.load_user()
        elif user_input == "3":
            return self.exit_program(0)


    def create_user(self):
        """Creates a new user. Asks for input for user name.
        returns: user_profile (user.User object)"""
        print("CREATE NEW PROFILE\n")
        print("*If you want to go back to the previous step, type 2 instead of your name\n*")
        print("What is your Name?")
        check = 0
        while check != "1":
            user_name = input("Type your name and press ENTER: ")
            print("")       # an empty print to skip a line visually

            if user_name == "2":
                return self.start_menu()

            print(f"Is {user_name} correct?")
            check = input("Type 1 for YES. Type Any other key for NO: ")
            print("")       # an empty print to skip a line visually
        return user.User(user_name, 0, [], [], [], [])

    def user_profile(self):
        """Provides the visuals and option functionality for the user in their profile.
        parameter: user_object: user.User class OBJ
        returns: """
        while True: 
            print(f"Welcome {self._user_object.get_name()}!\n")
            print("Please select from the options below by typing the number and pressing ENTER\n")
            print("1) Add New Goal")
            print("2) One-Off Goal List")
            print("3) Recurring Habits List")
            print("4) Negative Habits List")
            print("5) Completed Goals List")
            print("5) Main Menu")
            print("6) Exit")
            self.user_profile_select()

    def user_profile_select(self):
        """User Profile Menu Selection"""
        print("")
        count = 1
        user_input = None
        while (user_input != "1" and user_input != "2" and user_input != "3" and
            user_input != "4" and user_input != "5" and user_input != "6"):
            user_input = input("Type the Associated Number and Press ENTER: ")

        if user_input == "1":
            # create new one-off goal and add it to the user one_off_goal list.
            return self.add_new_goal_menu()
        elif user_input == "2":
            for goal in self._user_object.get_one_off_goal_list():
                print(f"{count}) {goal}")
                count += 1
        elif user_input == "3":
            for goal in self._user_object.get_recurring_chore_list():
                print(f"{count}) {goal.get_name()}")
                count += 1
        elif user_input == "4":
            for goal in self._user_object.get_negative_habit_list():
                print(f"{count}) {goal.get_name()}")
                count += 1
        elif user_input == "5":
            for goal in self._user_object.get_completed_goal_dict():
                print(f"{goal.get_name()}: {self._user_object.get_completed_goal_dict()[goal]}")
        elif user_input == "6":
            self.exit_program(1)

    def add_new_goal_menu(self):
        """menu to add goal to specific list"""
        print("\nADD NEW GOAL\n")
        print("1) Add One-Off Goal")
        print("2) Add Recurring Goal")
        print("3) Add Negative Habit")
        print("4) Previous Menu")
        print("5) Exit")
        return self.add_new_goal_select()

    def add_new_goal_select(self):
        """user select for adding goals to the specific list"""
        print("")
        user_input = None
        while (user_input != "1" and user_input != "2" and user_input != "3" and
            user_input != "4" and user_input != "5"):
            user_input = input("Type the Associated Number and Press ENTER: ")

        if user_input == "1" or user_input == "2" or user_input == "3":
            return self.add_new_goal_input(user_input)
        elif user_input == 4:
            self.user_profile()
        elif user_input == 5:
            self.exit_program(2)

    def add_new_goal_input(self, goal_select):
        """helper function for add_new_goal_select
        Helps decide which function to use to fill out the rest of the goal info.
        parameter: goal_select (STR)
        1: One-Off Goal, 2: Reccurring Goal, 3: Negative Habit"""

        print("Fill out the information below for your new goal")
        print("Type the answer to each Prompt and press ENTER\n")
        name = input("Name of Goal: ")
        description = input("Description of Goal: ")
        if goal_select == "1":
            return self.one_off_goal_cash(name, description)
        elif goal_select == "2":
            return self.recurring_goal_cash(name, description)
        elif goal_select == "3":
            return self.negative_goal_cash(name, description)
        
    def recurring_goal_cash(self, name, description):
        cash = None
        check_binary = 0
        while check_binary == 0:
            cash = input("Amount of Money Earned Each Time the Goal is Completed: ")
            print("")
            try:
                int(cash)
                if int(cash) < 0:
                    raise Exception()
            except:
                print("Positive Integers or 0 only please\n")
            else:
                check_binary = 1
            
        recurring_goal = chores.OngoingChore(name, description, cash, 0)
        self._user_object.get_recurring_chore_list().append(recurring_goal)
        print("Your recurring goal has been added!")
        return

    def negative_goal_cash(self, name, description):
        cash = None
        check_binary = 0
        while check_binary == 0:
            cash = input("Amount of money you must pay whenever you do this habit: ")
            print("")
            try:
                int(cash)
                if int(cash) > 0:
                    raise Exception()
            except:
                print("Negative integers or 0 only please\n")
            else:
                check_binary = 1
        negative_habit = chores.NegativeHabit(name, description, cash, 0)
        self._user_object.get_negative_habit_list().append(negative_habit)
        print("Your negative habit has been added!")
        return

    def one_off_goal_cash(self, name, description):
        cash = None
        check_binary = 0
        goal_size = 0
        while check_binary == 0:
            cash = input("Amount of Money Earned for Completion (Integers Only): ")
            print("")
            try:
                int(cash)
            except:
                print("Integers Only Please\n")
            else:
                check_binary = 1
        while goal_size != "1" and goal_size != "2":
            goal_size = input("Goal Size (Type 1 for a Small Goal or 2 for a Large Goal and press ENTER): ")
            print("")       # an empty print to skip a line visually
        if goal_size == "1":
            goal_size = "Small"
        elif goal_size == "2":
            goal_size = "Large"
        return self.one_off_goal_deadline(name, description, cash, goal_size)
        
    def one_off_goal_deadline(self, name, description, cash, goal_size):
        deadline = "deadline"
        binary_check = 0
        while binary_check == 0 or len(deadline) != 8 and deadline != None and deadline[3] != "/" and deadline[5] != "/":
            deadline = input("Deadline in 0X/0X/XX format (If No Deadline, Just Press ENTER Without Typing): ")
            print("")       # an empty print to skip a line visually
            if deadline == "":
                return chores.OneOffGoal(name, description, cash, "None", goal_size)
            try:
                int(deadline[0])
                int(deadline[1])
                int(deadline[3])
                int(deadline[4])
                int(deadline[6])
                int(deadline[7])
            except:
                print("Please enter the deadline in the format provided or press ENTER if no Deadline\n")
            else:
                binary_check = 1
        one_off_goal = chores.OneOffGoal(name, description, cash, deadline, goal_size)
        self._user_object.get_one_off_goal_list().append(one_off_goal)
        print("Your one-off goal has been added!\n")
        return

    def load_user(self):
        pass

    def exit_program(self, return_menu):
        """Exit program function.
        parameter: return_menu (INT) [0: Start Menu, 1: User Profile, 2: Add New Goal Menu]"""
        print("Are you sure you want to EXIT?\n")
        exit_check = input("Type 1 for YES. Type Any Other Key For NO: ")
        if exit_check == "1":
            sys.exit()
        else:
            print("")       # an empty print to skip a line visually
            if return_menu == 0:
                return self.start_menu()
            elif return_menu == 1:
                return self.user_profile()
            elif return_menu == 2:
                return self.add_new_goal_menu()

    def show_user_list(self):
        pass

if __name__ == "__main__":
    main()