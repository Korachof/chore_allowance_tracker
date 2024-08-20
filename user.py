import json
import chores

class User:
    def __init__(self, name, spending_money, one_off_goal_list, recurring_chore_list, negative_habit_list, completed_goal_dict):
        self._name = name
        self._spending_money = spending_money
        self._one_off_goal_list = one_off_goal_list
        self._recurring_chore_list = recurring_chore_list
        self._negative_habit_list = negative_habit_list
        self._completed_goal_dict = completed_goal_dict

    def get_name(self):
        """returns name (STR)"""
        return self._name
    
    def set_name(self, new_name):
        """sets/edits name (STR)
        returns: UPDATED self._name (STR)"""
        self._name = new_name
        return self._name
    
    def get_spending_money(self):
        """returns spending money (FLOAT)"""
        return self._spending_money
    
    def add_spending_money(self, new_amount):
        """add new_amount to spending_money
        returns: UPDATED self._spending_money"""
        self._spending_money += new_amount

    def spend_money(self, name_of_purchase, amount_spent):
        """subtracts amount_spent from spending_money.
        Saves name_of_purchase and amount_spent to JSON file
        returns name_of_purchase: amount_spent (STR)"""
        self._spending_money -= amount_spent
        dict = {name_of_purchase: amount_spent}

        with open(f"{self._name}_purchases_made.json", "a") as outfile:
            json.dump(dict, outfile)

        return f"{name_of_purchase}: {amount_spent}"
    
    def load_purchases(self):
        """Loads the content from the json file and prints it"""
        with open('sample.json', 'r') as openfile:
            json_object = json.load(openfile)

    def get_one_off_goal_list(self):
        """returns one_off_goal_list (LIST)"""
        return self._one_off_goal_list
    
    def get_recurring_chore_list(self):
        """returns ongoing_chore_list (LIST)"""
        return self._recurring_chore_list
    
    def get_negative_habit_list(self):
        """returns negative_habit_list (LIST)"""
        return self._negative_habit_list
    
    def get_completed_goal_dict(self):
        """returns completed_goal_list (DICT)
        {goal.get_name(): date_completed}"""
        return self._completed_goal_dict
    
    


